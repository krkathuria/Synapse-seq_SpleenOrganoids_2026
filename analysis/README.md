# Doublets 2 and 4 workflows

Run notebooks with this `analysis/` directory as their working directory. All source outputs and execution counts remain cleared; validation uses separate executed copies.

Before running, install the tested numerical environment described in [`../ENVIRONMENT.md`](../ENVIRONMENT.md). Exact fresh clustering was validated on macOS ARM64 with the specified SciPy/OpenBLAS builds; package version numbers alone are insufficient. All eight final cleaned notebooks and the R analysis passed together using the packaged inputs in that environment.

| Workflow | Inputs | Execution result |
| --- | --- | --- |
| Doublets 2 Step1 | Gene-count table and interaction-score workbook | Completed with the author-approved historical ERCC <0.3; all 3,363 historical cells are retained. |
| Doublets 2 Treg-B | Preprocessed matrix | Full rerun passes at 30% ERCC. All 629 cells and all five cluster memberships match the manuscript; the final figure section uses preserved manuscript coordinates. |
| Doublets 4 Step1 | Gene-count table | Completed; all values in the 7,600-cell scaled and raw-expression matrices match the historical object exactly. |
| Doublets 4 Step2 | MiXCR AIRR exports and metadata | Completed; 18,904 receptor records and all 69 retained columns match. |
| Doublets 4 R SHM script | Change-O/AIRR germline-alignment table | Completed; both mutation-summary tables match all 6,308 heavy-chain records exactly. |
| Non-spheromer Sp46 | Preprocessed matrix and receptor tables | Completed; manuscript figure section also passes. Fresh UMAP coordinates can differ. |
| Non-spheromer Sp55 | Preprocessed matrix and receptor tables | Resolved by materializing the donor subset before PCA and mapping labels only after exact cell-membership checks; all 2,170 cells and labels match. The figure section uses the preserved manuscript object. |
| Spheromer Sp46 and Sp55 | Preprocessed matrix, index-sort CSVs, receptor tables | Both completed during testing; final figure sections pass using preserved manuscript objects. |

## Tested figure command

```bash
python reproduce_manuscript_figures.py
```

Optional single-notebook example:

```bash
python reproduce_manuscript_figures.py --notebook Doublets_2_Treg-B.ipynb
```

The command deliberately executes the final plotting blocks after loading `data/reference_checkpoints/`. It is distinct from recomputing cluster assignments. It leaves the source notebooks unexecuted and saves executed figure-only copies under `results/figure_validation/`.

## Full analysis order

Automated command from the repository root: `python analysis/run_full_analysis.py`.
It checks the complete data manifest before starting, runs all eight notebooks and the R calculation in the order below, and saves executed copies under `results/full_validation/`. Run it on a fresh extracted data bundle because intermediate files are regenerated. Install the R packages separately as described in [`ENVIRONMENT.md`](../ENVIRONMENT.md#r-calculation).

1. Doublets 2 Step1, then Doublets 2 Treg-B.
2. Doublets 4 Step1, then Doublets 4 Step2.
3. Run `Rscript RStudio_Immcantation_Doublets_4.R` for aggregate and individual-region SHM tables.
4. Run the four Doublets 4 clustering notebooks.

Doublets 2 now uses the author-approved historical 30% ERCC cutoff, which reproduces the original assignments. Doublets 4 retains 20%. Sp55's materialization issue is resolved. See `../CLUSTERING_DIAGNOSIS.md`. Do not force the saved label lists onto a different clustering result. The paired heavy/light-chain `UniqueClones` table is supplied as an input; reconstructing it from upstream receptor calls is outside this collection.
