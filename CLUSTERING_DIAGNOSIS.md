# Causes of the Doublets 2, Sp55, and Sp46 clustering differences

Controlled experiments performed on 20 October 2026 identified separate causes. Tests used copies and left the original Doublets files unchanged. After reviewing the diagnosis, the author approved reporting and restoring the historical 30% ERCC cutoff for Doublets 2; Doublets 4 retains 20%.

## Doublets 2: the historical analysis used a different QC cutoff

The original **Doublets 2** preprocessing notebook explicitly filters with `adata.obs.ercc_frac < 0.3`. Its saved output contains 3,363 cells, including four with ERCC fractions between 20% and 30%. The release copy was initially changed to `<0.2` following the author's instruction; it has now been restored to `<0.3` with author approval.

Repeating preprocessing and clustering while changing only this cutoff gives:

| Test | Global cells | Variable genes | Treg-B cells | Clusters | Agreement with manuscript assignments |
| --- | ---: | ---: | ---: | ---: | --- |
| Historical 30% cutoff | 3,363 | 10,101 | 629 | 5 | All 629 assignments match; adjusted Rand index 1.0 |
| Requested 20% cutoff | 3,359 | 10,107 | 629 | 6 | Different partition; adjusted Rand index 0.721 |

At 30%, the rebuilt normalized expression values are identical to the historical values, and scaled values agree to approximately 6 × 10⁻¹³. The PCA coordinates and all five cluster memberships reproduce the saved analysis.

The four removed cells are outside the Treg-B subset. Nevertheless, ComBat batch correction, variable-gene selection, and scaling are performed on the global dataset **before** taking that subset. Removing the four cells therefore changes the input to the later Treg-B clustering. Thirty-six genes change variable-gene status (a net increase of six), while the same 629 Treg-B cell IDs remain. This is a change to the analysis settings, not missing data or a new software-version failure.

**Resolved with author approval:** the release notebook now uses ERCC fraction <0.3 for Doublets 2. STAR Methods explicitly reports exclusion at ≥30% for Doublets 2 and ≥20% for Doublets 4. The controlled rerun at the restored setting reproduces all 629 manuscript cluster assignments. The 20% experiment above is retained as diagnostic evidence, not the final Doublets 2 workflow.

## Sp55: removing a scratch annotation changed AnnData materialization

The Sp55 input expression values, raw values, selected cells, and all 10,003 variable-gene flags match the saved analysis exactly. The difference begins at PCA.

The original notebook assigned a scratch column to `adata.obs` before PCA. AnnData implicitly materialized the filtered view into an independent object at that assignment. Removing the scratch annotation during publication cleanup removed that side effect as well. The retained subset stayed a view.

With Scanpy 1.9.4 / anndata 0.9.2, the variable-gene matrix passed to PCA has different memory layout in these two cases. Its numeric values are unchanged, but float32 PCA and graph weights acquire small rounding differences. Here, those small differences change the Leiden partition at the existing resolution of 0.9.

| Controlled test, same data and parameters | Clusters before removal of the two unknown groups | Agreement on the 2,170 manuscript cells |
| --- | ---: | --- |
| Filtered AnnData view | 15 | Adjusted Rand index 0.932 |
| Explicit independent copy before PCA | 14 | All cluster memberships match; adjusted Rand index 1.0. Numeric IDs of two groups swap. |
| Temporary observation assignment before PCA | 14 | All cluster memberships match; adjusted Rand index 1.0. Numeric IDs of two groups swap. |

The release Sp55 notebook now explicitly materializes the donor subset with `.copy()` before PCA. This restores the original behavior without restoring the scratch annotation. No filtering threshold, gene list, or clustering resolution was changed to obtain the matching partition.

The full check identified a second, distinct annotation problem: the two 22-cell clusters exchanged numeric IDs 11 and 12. One is the retained plasmablast group, and one is an excluded unknown group. The old positional label list would therefore retain the wrong 22 cells despite identical cluster sizes. The swap also occurs with igraph 0.10.6, so downgrading igraph alone does not solve it.

The notebook now reads the published manual annotations from `data/annotations/Sp55_manuscript_cluster_annotations.tsv`, derived from the preserved manuscript object. It assigns a label only when a freshly computed cluster's **entire cell set matches exactly** the set recorded for that label. If any retained cluster splits, merges, gains cells, or loses cells, execution stops for review. This handles numeric-ID permutations without changing or forcing the computed partition. The two originally excluded groups remain excluded.

With both corrections, the full Sp55 notebook executes, and the newly generated object has the same 2,170 retained cell IDs and exactly the same named cell assignments as the manuscript object. This check compares the newly written object before the final plotting section reloads the preserved object.

Small PCA/graph rounding differences from the historical checkpoint can remain, and a fresh UMAP can have different coordinates. Exact agreement of cell assignments should not be described as pixel-identical reproduction of a newly calculated UMAP. The existing figure command continues to use the preserved manuscript coordinates explicitly.

## Sp46: explicit donor-subset materialization

The final isolated rerun exposed a small non-spheromer Sp46 partition difference despite identical expression values and variable-gene flags (adjusted Rand index 0.994141 in the original environment and 0.994235 in the clean environment). A controlled clean-environment test changed only the donor subset from a view to an explicit `.copy()` before PCA. The resulting partition matched the manuscript exactly without changing the resolution, cell selection, or gene selection.

The release Sp46 notebook now makes that copy explicitly. Its full clean-environment rerun completed, and the saved 1,961-cell object has identical named labels and cluster memberships (adjusted Rand index 1.0), as well as identical expression values. Its freshly calculated UMAP coordinates differ from the preserved manuscript coordinates. This establishes the tested numerical remedy; it does not establish which historical notebook side effect originally materialized this subset. See `validation/sp46_materialization_comparison.json` and `validation/fresh_object_comparison.json`.

## Evidence

Local diagnostic scripts, before/after source copies, threshold experiments, cluster cross-tabulations, and execution logs are retained in `Code/.clustering_diagnosis_20261020/`. Compact numeric results are also copied into `results/validation_evidence/`, and the successful full executed Sp55 notebook is in `results/full_validation/`. These are diagnostic results, not replacements for the preserved manuscript checkpoints.

## Numerical-build validation after publication cleanup

A subsequent fresh all-pip installation completed the checkpoint figures but failed the Sp55 exact-membership guard during the full workflow. The SciPy version was still 1.11.2; its wheel used OpenBLAS 0.3.21.dev with pthreads, whereas the historical conda-forge SciPy build used OpenBLAS 0.3.23 with OpenMP. A controlled run changed only the SciPy package to the historical build and restored exact memberships. The final source code and all analysis parameters were unchanged.

The release now supplies `conda-numerics-osx-arm64.txt` and a tested installation sequence in `ENVIRONMENT.md`. A new isolated installation of those numerical binaries plus the pinned Python packages completed all eight final notebooks and passed the separate saved-object comparisons. This addresses binary-build reproducibility on the tested macOS ARM64 platform; other platforms remain unvalidated.
