# Current manuscript review — 20 October 2026

The final publication notebooks reproduce the scientific content of all included Doublets 2/4 panels in the current assembled manuscript: Figure 2D–H, Figure 4B–G, Figure S3A–F, Figure S4A–D, Figure S5C, and Figure S6A–E. This is 27 labeled panels generated from 41 PDF exports. Atlas, SLE, and other non-sequencing experiments are outside the author-approved scope. Illustrator page assembly, panel letters, and manual annotations are not reconstructed by the notebooks.

## Verification against the actual manuscript

All six current assembled figure pages and every regenerated export were visually inspected. The exact figure source filenames and hashes, and a per-output panel map, are recorded in `validation/current_manuscript_panel_review.json` and `MANUSCRIPT_PANEL_MAP.tsv`.

Of 41 final PDF exports, 36 are pixel-identical to their latest matching saved standalone export. Four violin plots have matching distributions, group order, colors, labels, and significance annotations with different horizontal point jitter. Figure 2E was corrected from the older 11-marker standalone version to the 16-marker list in the current assembled manuscript: CD3E, MS4A1, FOXP3, IL2RA, TNFRSF18, PRF1, GZMA, GZMB, RGS13, BCL6, AICDA, BCL2A1, SOX5, ITGAX, ZEB2, and NRN1. Its new dot sizes, expression colors, and marker order were checked against the assembled panel. Figure 4F now uses the manuscript axis label, “IgH clonal expansion.”

## Publication cleanup

Removed obsolete Figure S2 exports, duplicate plots and superseded statistical comparisons, unpublished marker/isotype/stimulation screens, unused clone-selection queries, and the exploratory four-pair heatmap. No unpublished future-project sections remain in the retained analysis code. Required quality control and cell-type annotation diagnostics remain. The manuscript Discussion co-expression calculation is retained and tested: 53 of 57 IL10-positive interactions meet the existing scaled-expression positivity criterion for at least one of PRF1, GZMA, or GZMB (93.0%).

All filtering, preprocessing, clustering, receptor, and saved-object calculation cells preceding the publication checkpoint reloads are byte-for-byte unchanged from the fully tested versions. `validation/publication_cleanup_provenance.json` records source hashes, removed cell numbers, and the unchanged upstream prefix for each notebook. After cleanup, all eight final notebooks and the R analysis were executed together from an isolated copy of the packaged inputs. All passed. The full-notebook reports now record the final source hashes. All five final figure sections also passed independently in the clean Python environment. All source outputs and execution counts remain cleared.

## Numerical and data verification

The final isolated full run completed all eight cleaned notebooks and the R SHazaM calculation using only manifest-listed inputs. All five fresh cluster partitions and named annotations match the manuscript references exactly (adjusted Rand index 1.0). Expression matrices and variable-gene flags match within numerical precision. Fresh UMAP coordinates differ for four Doublets 4 objects; final plotting explicitly loads preserved publication coordinates. Both SHazaM outputs match all mutation-frequency columns for 6,308 heavy-chain records. See `FINAL_RELEASE_AUDIT.md` and its linked numeric evidence.

The auxiliary bundle contains all 7,829 manifest-listed files needed by these retained count-matrix/AIRR-table workflows. Every archived member was read back and verified with no missing, extra, duplicated, or mismatched files. This is not a packaged FASTQ-to-count-matrix or BASIC/IgBLAST/Change-O pipeline. The exact conda artifact installation was tested on macOS ARM64; generic The exact conda artifact installation was tested on macOS ARM64; generic Conda solving, a fresh R installation, and other operating systems have not been tested. Python 3.11.8 dependencies were installed and verified on macOS ARM64.

The analysis repository remains private. The separate public information page contains only a README: https://github.com/krkathuria/Synapse-seq_SpleenOrganoids_2026-info. Private data-release status and reassembly instructions are in `DATA_DISTRIBUTION.md`. A public code/data release remains pending.

Exact fresh clustering requires the tested numerical binaries in `ENVIRONMENT.md`; the same SciPy version installed from an all-pip wheel failed Sp55 membership validation. No scientific parameters or source calculations were altered to resolve this environment issue.
