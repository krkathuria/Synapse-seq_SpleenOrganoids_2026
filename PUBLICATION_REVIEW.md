# Current manuscript review — 20 October 2026

The final publication notebooks reproduce the scientific content of all included Doublets 2/4 panels in the current assembled manuscript: Figure 2D–H, Figure 4B–G, Figure S3A–F, Figure S4A–D, Figure S5C, and Figure S6A–E. This is 27 labeled panels generated from 41 PDF exports. Atlas, SLE, and other non-sequencing experiments are outside the author-approved scope. Illustrator page assembly, panel letters, and manual annotations are not reconstructed by the notebooks.

## Verification against the actual manuscript

All six current assembled figure pages and every regenerated export were visually inspected. The exact figure source filenames and hashes, and a per-output panel map, are recorded in `validation/current_manuscript_panel_review.json` and `MANUSCRIPT_PANEL_MAP.tsv`.

Of 41 final PDF exports, 36 are pixel-identical to their latest matching saved standalone export. Four violin plots have matching distributions, group order, colors, labels, and significance annotations with different horizontal point jitter. Figure 2E was corrected from the older 11-marker standalone version to the 16-marker list in the current assembled manuscript: CD3E, MS4A1, FOXP3, IL2RA, TNFRSF18, PRF1, GZMA, GZMB, RGS13, BCL6, AICDA, BCL2A1, SOX5, ITGAX, ZEB2, and NRN1. Its new dot sizes, expression colors, and marker order were checked against the assembled panel. Figure 4F now uses the manuscript axis label, “IgH clonal expansion.”

## Publication cleanup

Removed obsolete Figure S2 exports, duplicate plots and superseded statistical comparisons, unpublished marker/isotype/stimulation screens, unused clone-selection queries, and the exploratory four-pair heatmap. The retained code contains no RNA-transfer, trogocytosis, exosome, vesicle, or future-idea sections. Required quality control and cell-type annotation diagnostics remain. The manuscript Discussion co-expression calculation is retained and tested: 53 of 57 IL10-positive interactions meet the existing scaled-expression positivity criterion for at least one of PRF1, GZMA, or GZMB (93.0%).

All filtering, preprocessing, clustering, receptor, and saved-object calculation cells preceding the publication checkpoint reloads are byte-for-byte unchanged from the fully tested versions. `validation/publication_cleanup_provenance.json` records source hashes, removed cell numbers, and the unchanged upstream prefix for each notebook. Earlier full-notebook reports intentionally retain their original source hashes. After cleanup, all five final figure sections were executed again in the clean Python environment and passed; their reports record the current source hashes. All source outputs and execution counts remain cleared.

## Numerical and data verification

The preceding isolated full run completed eight notebooks and the R SHazaM calculation using only manifest-listed inputs. All five fresh cluster partitions and named annotations match the manuscript references exactly (adjusted Rand index 1.0). Expression matrices and variable-gene flags match within numerical precision. Fresh UMAP coordinates differ for four Doublets 4 objects; final plotting explicitly loads preserved publication coordinates. Both SHazaM outputs match all mutation-frequency columns for 6,308 heavy-chain records. See `FINAL_RELEASE_AUDIT.md` and its linked numeric evidence.

The auxiliary bundle contains all 7,829 manifest-listed files needed by these retained count-matrix/AIRR-table workflows. Every archived member was read back and verified with no missing, extra, duplicated, or mismatched files. This is not a packaged FASTQ-to-count-matrix or BASIC/IgBLAST/Change-O pipeline. Conda solving, a fresh R installation, and other operating systems have not been tested. Python 3.11.8 dependencies were installed and verified on macOS ARM64.

The analysis repository remains private. The separate public information page contains only a README: https://github.com/krkathuria/Synapse-seq_SpleenOrganoids_2026-info. Private data-release status and reassembly instructions are in `DATA_DISTRIBUTION.md`. A public code/data release remains pending.
