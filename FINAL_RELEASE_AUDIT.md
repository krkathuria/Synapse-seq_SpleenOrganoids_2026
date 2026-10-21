# Final manuscript and execution audit

All retained Doublets 2/4 scientific figure panels were validated against the current assembled manuscript: 41 exports covering 27 panels. Atlas, SLE, and other non-sequencing experiments are excluded by the author. Manual Illustrator page assembly is separate. See PUBLICATION_REVIEW.md and MANUSCRIPT_PANEL_MAP.tsv.

## Full execution and numerical comparisons

All eight final cleaned notebooks and the R SHazaM analysis passed together in an isolated copy of the manifest-listed inputs. The current notebook hashes are recorded in validation/full_*.json. The exact tested macOS ARM64 numerical installation is specified in ENVIRONMENT.md and conda-numerics-osx-arm64.txt. The same SciPy version from an all-pip wheel failed Sp55 membership validation; its numerical build matters. Scientific parameters and source calculations were unchanged by the environment repair.

Both fresh preprocessing matrices match the reference cell sets, gene order, highly variable genes, and raw expression values, with scaled-expression differences below 1e-8. All five fresh cluster partitions and named assignments match exactly (adjusted Rand index 1.0). Four Doublets 4 fresh UMAP layouts differ; final plotting sections explicitly use preserved manuscript coordinates. See validation/fresh_object_comparison.json.

Both SHazaM tables match every mutation-frequency column for all 6,308 heavy-chain records. See validation/fresh_R_comparison.json. The Sp55 Discussion calculation confirms 53/57 IL10-positive interactions overlap with at least one retained cytotoxic marker under the existing positivity criterion (93.0%).

## Figure comparisons

All five final figure sections passed independently, and all 41 exports from the full run were compared again. Thirty-six match the latest saved standalone reference pixel for pixel. Four violin plots retain horizontal point-jitter differences with matching distributions and statistics. Figure 2E now uses the 16 markers in the assembled manuscript, replacing the older 11-marker standalone export. All exports were visually checked against the six current assembled manuscript figure pages. See validation/final_full_plot_comparison.json and PUBLICATION_REVIEW.md.

## Data and distribution

The auxiliary archive contains all 7,829 manifest-listed files required by the retained count-matrix/AIRR workflows. Every archive member was read back and verified, with no missing, extra, duplicate, or mismatched files. The archive is 11,720,414,184 bytes, SHA-256 45261b520de63aaa5921050546dd3b8659e2c183212ce16bb29f45cc3aceb262. GitHub release upload is still in progress; it is not yet a complete downloadable bundle.

The analysis repository is public. STAR Methods links this repository. A complete upstream FASTQ pipeline, a fresh R installation, other operating systems, remain outside this validation.

Exact fresh clustering requires the tested numerical binaries in `ENVIRONMENT.md`; the same SciPy version installed from an all-pip wheel failed Sp55 membership validation. No scientific parameters or source calculations were altered to resolve this environment issue.
