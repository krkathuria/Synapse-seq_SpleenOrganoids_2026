"""Compare fresh saved analysis objects with publication references.

Run after run_full_analysis.py. This reads saved intermediate files, not the
in-memory object reloaded by the final publication plotting sections.
"""
import argparse
import json
from pathlib import Path
import numpy as np
import anndata
from sklearn.metrics import adjusted_rand_score


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    results = []
    for reference in sorted((root / 'data/reference_checkpoints').glob('*.h5ad')):
        folder = 'smartseq_doublets_2_analysis' if '3363cells' in reference.name or 'SP17' in reference.name else 'smartseq_doublets_4_analysis'
        fresh = root / 'data/Doublets/data' / folder / reference.name
        a, b = anndata.read_h5ad(fresh), anndata.read_h5ad(reference)
        row = {'file':reference.name, 'fresh_shape':list(a.shape), 'reference_shape':list(b.shape)}
        for obj in (a, b):
            if 'cell' in obj.obs:
                obj.obs_names = obj.obs['cell'].astype(str)
        row['same_cell_set'] = set(a.obs_names) == set(b.obs_names)
        row['same_gene_order'] = list(a.var_names) == list(b.var_names)
        if row['same_cell_set'] and row['same_gene_order']:
            a = a[b.obs_names].copy()
            row['X_max_difference'] = float(np.max(np.abs(a.X - b.X)))
            if a.raw is not None and b.raw is not None and list(a.raw.var_names) == list(b.raw.var_names):
                row['raw_X_max_difference'] = float(np.max(np.abs(a.raw.X - b.raw.X)))
            if 'highly_variable' in a.var and 'highly_variable' in b.var:
                row['HVG_differences'] = int((a.var.highly_variable != b.var.highly_variable).sum())
            if 'leiden' in a.obs and 'leiden' in b.obs:
                row['cluster_ARI'] = float(adjusted_rand_score(a.obs.leiden, b.obs.leiden))
                row['named_labels_identical'] = bool(np.array_equal(a.obs.leiden.astype(str), b.obs.leiden.astype(str)))
            if 'X_umap' in a.obsm and 'X_umap' in b.obsm:
                row['UMAP_max_difference'] = float(np.max(np.abs(a.obsm['X_umap'] - b.obsm['X_umap'])))
        row['expression_and_partition_match'] = (
            row['same_cell_set'] and row['same_gene_order'] and
            row.get('X_max_difference', float('inf')) < 1e-8 and
            row.get('raw_X_max_difference', float('inf')) < 1e-8 and
            row.get('HVG_differences', 0) == 0 and row.get('cluster_ARI', 1.0) == 1.0)
        results.append(row)
        del a, b
    if not results:
        raise SystemExit('No reference checkpoints found.')
    out = root / 'results/full_validation/fresh_object_comparison.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))
    return 0 if all(row['expression_and_partition_match'] for row in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
