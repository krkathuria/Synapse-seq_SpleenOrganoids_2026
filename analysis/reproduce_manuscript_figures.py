"""Render manuscript figures from the bundled, preserved analysis checkpoints.

Run from the repository root:
    python analysis/reproduce_manuscript_figures.py
This executes only the marked final figure sections, not fresh clustering.
"""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys
import time
import hashlib
import importlib

ANALYSIS = Path(__file__).resolve().parent
REPO = ANALYSIS.parent
NAMES = [
    'Doublets_2_Treg-B.ipynb',
    'Doublets_4_Clustering_Sp46.ipynb',
    'Doublets_4_Clustering_Sp55.ipynb',
    'Doublets_4_Clustering_Sphr_HA_PRTN3_Sp46_larger_fonts.ipynb',
    'Doublets_4_Clustering_Sphr_HA_PRTN3_Sp55_larger_fonts.ipynb',
]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--notebook', choices=NAMES, help='Render one notebook instead of all five.')
args = parser.parse_args()
if not args.notebook:
    failures = []
    for name in NAMES:
        result = subprocess.run([sys.executable, str(Path(__file__).resolve()), '--notebook', name])
        if result.returncode:
            failures.append(name)
    if failures:
        raise SystemExit('Figure execution failed: ' + ', '.join(failures))
    print('All five manuscript figure sections executed successfully.')
    raise SystemExit(0)

out = REPO / 'results' / 'figure_validation'
cache = out / 'cache'
for key, folder in [('NUMBA_CACHE_DIR', 'numba'), ('MPLCONFIGDIR', 'matplotlib'), ('IPYTHONDIR', 'ipython')]:
    path = cache / folder
    path.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(path)
os.environ['OPENBLAS_NUM_THREADS'] = '12'
os.environ['NUMBA_NUM_THREADS'] = '12'
os.environ['MPLBACKEND'] = 'Agg'
import nbformat
import matplotlib.pyplot as plt
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.utils.capture import capture_output

nb = nbformat.read(ANALYSIS / args.notebook, as_version=4)
start = next(i for i, c in enumerate(nb.cells)
             if c.cell_type == 'code' and "sc.read_h5ad('../data/reference_checkpoints/" in c.source)
shell = TerminalInteractiveShell.instance()
shell.run_line_magic('matplotlib', 'inline')
os.chdir(ANALYSIS)
report = {'notebook': args.notebook, 'mode': 'preserved_manuscript_checkpoint_figures',
          'fresh_clustering_executed': False, 'status': 'running', 'cells': [],
          'source_sha256': hashlib.sha256((ANALYSIS / args.notebook).read_bytes()).hexdigest(),
          'python': sys.version,
          'packages': {name: getattr(importlib.import_module(name), '__version__', 'unknown')
                       for name in ['scanpy', 'anndata', 'numpy', 'pandas', 'scipy', 'igraph',
                                    'matplotlib', 'seaborn', 'statannotations']}}
for i, cell in enumerate(nb.cells):
    if cell.cell_type != 'code' or (i >= 5 and i < start):
        continue
    t = time.time()
    with capture_output(stdout=True, stderr=True, display=True) as captured:
        result = shell.run_cell(cell.source, store_history=True)
    cell.execution_count = shell.execution_count - 1
    cell.outputs = []
    for stream in ('stdout', 'stderr'):
        value = getattr(captured, stream)
        if value:
            cell.outputs.append(nbformat.v4.new_output('stream', name=stream, text=value))
    for item in captured.outputs:
        cell.outputs.append(nbformat.v4.new_output('display_data', data=item.data, metadata=item.metadata))
    error = result.error_before_exec or result.error_in_exec
    report['cells'].append({'cell': i + 1, 'seconds': round(time.time() - t, 3),
                            'status': 'failed' if error else 'passed', 'error': str(error) if error else None})
    plt.close('all')
    if error:
        report['status'] = 'failed'
        print(captured.stdout, captured.stderr)
        break
else:
    report['status'] = 'passed'
nbformat.write(nb, out / args.notebook)
(out / (Path(args.notebook).stem + '.json')).write_text(json.dumps(report, indent=2) + '\n')
print(args.notebook + ': ' + report['status'], flush=True)
raise SystemExit(0 if report['status'] == 'passed' else 1)
