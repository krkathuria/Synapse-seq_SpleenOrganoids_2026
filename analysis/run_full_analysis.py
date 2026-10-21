"""Run the eight retained notebooks and SHazaM in dependency order.

Starts from supplied count matrices and receptor tables, not FASTQs.
Intermediate files under data/ are regenerated. Use a fresh extracted data bundle.
The final figure sections explicitly reload preserved publication checkpoints.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

ANALYSIS = Path(__file__).resolve().parent
REPO = ANALYSIS.parent
NAMES = [
    'Doublets_2_Step1_PreProcessing_halveSingletReads_with_DoubletScores_only_HugoGeneSymbols.ipynb',
    'Doublets_2_Treg-B.ipynb',
    'Doublets_4_Step1_PreProcessing_halveSingletReads_with_DoubletScores_only_HugoGeneSymbols.ipynb',
    'Doublets_4_Step2_add_BCR_TCR.ipynb',
    'Doublets_4_Clustering_Sp46.ipynb',
    'Doublets_4_Clustering_Sp55.ipynb',
    'Doublets_4_Clustering_Sphr_HA_PRTN3_Sp46_larger_fonts.ipynb',
    'Doublets_4_Clustering_Sphr_HA_PRTN3_Sp55_larger_fonts.ipynb',
]


def run_notebook(name):
    out = REPO / 'results/full_validation'
    for key, folder in [('NUMBA_CACHE_DIR', 'numba'), ('MPLCONFIGDIR', 'matplotlib'), ('IPYTHONDIR', 'ipython')]:
        path = out / 'cache' / folder
        path.mkdir(parents=True, exist_ok=True)
        os.environ[key] = str(path)
    for key in ['OPENBLAS_NUM_THREADS', 'NUMBA_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS']:
        os.environ[key] = '12'
    os.environ['MPLBACKEND'] = 'Agg'
    import nbformat
    import matplotlib.pyplot as plt
    from IPython.terminal.interactiveshell import TerminalInteractiveShell
    from IPython.utils.capture import capture_output

    source = ANALYSIS / name
    nb = nbformat.read(source, as_version=4)
    shell = TerminalInteractiveShell.instance()
    shell.run_line_magic('matplotlib', 'inline')
    os.chdir(ANALYSIS)
    report = {'notebook': name, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'mode': 'full_notebook_with_explicit_checkpoint_figure_section', 'status': 'running', 'cells': []}
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != 'code':
            continue
        start = time.time()
        with capture_output(stdout=True, stderr=True, display=True) as captured:
            result = shell.run_cell(cell.source, store_history=True)
        cell.execution_count = shell.execution_count - 1
        cell.outputs = []
        for stream in ('stdout', 'stderr'):
            if getattr(captured, stream):
                cell.outputs.append(nbformat.v4.new_output('stream', name=stream, text=getattr(captured, stream)))
        for item in captured.outputs:
            cell.outputs.append(nbformat.v4.new_output('display_data', data=item.data, metadata=item.metadata))
        error = result.error_before_exec or result.error_in_exec
        report['cells'].append({'cell': i + 1, 'seconds': round(time.time() - start, 3),
                                'status': 'failed' if error else 'passed', 'error': str(error) if error else None})
        plt.close('all')
        print(f'{name}: cell {i + 1}/{len(nb.cells)} ' + ('FAILED' if error else 'passed'), flush=True)
        if error:
            print(captured.stdout, captured.stderr)
            report['status'] = 'failed'
        nbformat.write(nb, out / name)
        (out / (Path(name).stem + '.json')).write_text(json.dumps(report, indent=2) + '\n')
        if error:
            return 1
    report['status'] = 'passed'
    (out / (Path(name).stem + '.json')).write_text(json.dumps(report, indent=2) + '\n')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--notebook', choices=NAMES, help='Run one notebook; prerequisites must already exist.')
    args = parser.parse_args()
    if args.notebook:
        return run_notebook(args.notebook)
    preflight = subprocess.run([sys.executable, str(REPO / 'scripts/verify_data.py')])
    if preflight.returncode:
        return preflight.returncode
    for i, name in enumerate(NAMES):
        if i == 4:
            result = subprocess.run(['Rscript', 'RStudio_Immcantation_Doublets_4.R'], cwd=ANALYSIS)
            if result.returncode:
                return result.returncode
        result = subprocess.run([sys.executable, str(Path(__file__).resolve()), '--notebook', name])
        if result.returncode:
            return result.returncode
    print('All eight notebooks and the R SHazaM analysis passed. Compare the fresh saved objects separately from the checkpoint figures.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
