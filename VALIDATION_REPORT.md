# Local reproduction report — 20 October 2026

**The subsequent [final release audit](FINAL_RELEASE_AUDIT.md) supersedes readiness claims in this earlier report.** It adds an isolated full rerun, clean Python installation, archive verification, and resolution of the final non-spheromer Sp46 partition mismatch. All five fresh partitions and named labels now match the references. The figures below are checkpoint-based comparisons, not whole-paper reconstruction. The upload status below records the earlier preparation stage.

**The data bundle is complete for the retained notebook workflows, and all five final figure sections execute. Sp55's fresh-clustering failure is now resolved.** The author has approved retaining the historical 30% ERCC cutoff for Doublets 2, which reproduces its manuscript assignments exactly. The release code and Methods now agree; Doublets 4 retains 20%. See [the controlled diagnosis](CLUSTERING_DIAGNOSIS.md). Figure rendering from preserved manuscript objects is reported separately below.

## Data and source preservation

The `data/` folder contains 7,824 files copied from Doublets, totaling 14.23 GB before regeneration of intermediate copies. These include count tables and interaction annotations, 7,552 MiXCR AIRR exports, 43 index-sort CSVs, paired BCR annotations, seven manuscript reference checkpoints, two reference SHM tables, and 204 saved plot exports from several figure drafts.

[`data/INPUT_MANIFEST.tsv`](data/INPUT_MANIFEST.tsv) records each file's source, role, size, original checksum, and current checksum. Nine intermediate copies changed during execution, including the subsequently regenerated Sp55 object; raw inputs and preserved references passed the integrity check. Originals in Doublets were not edited. Source notebooks in `analysis/` retain empty outputs and null execution counts. Executed copies are separate, and nothing was uploaded.

This is a count-matrix/AIRR-table-to-analysis collection. It does not include a complete FASTQ-to-count-matrix or BASIC/IgBLAST/Change-O reconstruction pipeline. The paired heavy/light-chain `UniqueClones` table is a supplied input, not an output of the retained Step2 notebook.

## Actual execution results

| Workflow | Verified result |
| --- | --- |
| Doublets 2 preprocessing | Completed with the author-approved historical ERCC fraction <0.3. Retained all 3,363 cells in the historical checkpoint. |
| Doublets 2 Treg-B fresh clustering | Full rerun passed at the restored 30% ERCC cutoff. All 629 cell IDs and all five cluster memberships match the manuscript (adjusted Rand index 1.0). The freshly saved object was compared before the final plotting section reloads the preserved checkpoint. |
| Doublets 4 preprocessing | Completed. All 7,600 cell IDs, 41,763 genes, highly variable gene flags, scaled expression values, and raw expression values match the reference exactly; maximum matrix difference is zero. |
| Doublets 4 receptor import/annotation | Completed. All 18,904 records and all 69 retained columns match the reference. The obsolete exploratory `SHM_Rough` column is excluded. |
| R SHM analysis | Completed. Both the aggregate CDR/FWR table and the individual VDJ-region table match the saved mutation values for all 6,308 heavy-chain records exactly; maximum difference is zero. |
| Non-spheromer Sp46 | Full notebook execution completed during testing. Fresh UMAP coordinates can differ from the saved coordinates. |
| Non-spheromer Sp55 | Resolved: an explicit `.copy()` before PCA restores the partition; exact-membership matching applies the original annotations despite numeric-ID swaps. Full notebook execution passes. The newly saved object contains the same 2,170 cells and exactly matching cluster labels. |
| Spheromer Sp46 and Sp55 | Both full notebooks completed during testing. Cluster memberships matched their saved references in the tested runs; fresh UMAP layouts differed. |
| Five final figure sections | All passed using preserved manuscript checkpoints and the supplied receptor/SHM tables. This validates the plotting sections independently of fresh clustering. |

## Plot comparisons

The tested command is:

```bash
python analysis/reproduce_manuscript_figures.py
```

It loads `data/reference_checkpoints/`, executes the final plotting sections, writes PDFs under `results/`, and saves executed notebooks and per-cell execution reports under [`results/figure_validation/`](results/figure_validation/). It does not rerun clustering. The saved objects are used explicitly, rather than presenting preserved results as newly computed cluster assignments.

There are 54 generated plot files. Of these, 51 have a matching saved reference filename:

- **44 match the latest matching saved export pixel for pixel**, when rendered with PDFium at the same resolution.
- **Six violin plots have matching distributions, labels, colors, and significance annotations on visual inspection.** Their small raster differences are consistent with the random horizontal jitter of individual points. They are not pixel-identical.
- **One older SP17 dotplot, `dotplot_Fig_S2_SP17.pdf`, differs in marker set and layout.** It is not counted as a reproduced panel. The later `dotplot_Fig_S3_SP17.pdf` matches exactly.
- Three additional outputs have no matching reference filename and therefore have execution evidence only: the older SP17 Figure S2 barplot and UMAP, and the Sp55 Figure 3 isotype barplot.

The comparisons are against saved individual plot exports. They do not establish exact reproduction of the assembled manuscript figures, their Illustrator layouts, or non-sequencing experiments.

## What remains before claiming end-to-end reproduction

**IL10/cytotoxic overlap check resolved.** The earlier flag focused on a Doublets 2 helper that computes a union. The Sp55 notebook separately and directly counts IL10-positive interactions lacking all three cytotoxic markers. In its 301-interaction Cytotoxic Treg-B/CD25+ T-B subset, 57 interactions meet the existing IL10 positivity criterion and only four lack all three cytotoxic markers: 53/57 (93.0%) overlap. These recorded results support the Discussion co-expression statement for that analyzed subset. No analysis settings or results were changed. The misleading union-helper name can be handled in routine code cleanup; it is not a missing experimental method. Evidence: `results/validation_evidence/IL10_overlap_resolution.json`.

The retained workflows still begin with supplied count matrices and receptor tables rather than FASTQ files. Final author review and code/input-data distribution remain outstanding.

## Repairs made in publication copies

- Converted external paths to local `data/` paths and directed plots to `results/`.
- Removed an unused Doublets 3 workbook branch from Doublets 4 and obsolete scratch cells that required unavailable columns or variables.
- Removed the stale Doublets 2 reload of a 611-cell checkpoint; the preceding live subset contains the manuscript's 629 Treg-B cells.
- Corrected the spheromer day-3/day-5 directory comparison, initialized the revision-figure output path before use, and made the Sp55 observation index compatible with AnnData slicing.
- Retained SHM merges after the final checkpoint reload so those columns are not discarded.
- Generated aggregate SHM with the recorded `IMGT_V` region definition and individual-region SHM with `IMGT_VDJ_BY_REGIONS`, writing each to its intended filename. Both outputs were checked against the saved tables.
- Carried final marker lists, titles, two missing dotplots, and the final Sp55 SHM plotting cell over from the newer source notebooks. The Sp55 cell retains its original Mann–Whitney comparisons and Bonferroni correction.
- Removed obsolete SHM plot variants that overwrote a final export, and explicitly set the recorded four-group palette so a preceding two-group plot cannot change the HA colors.
- Added the figure-only runner. No scientific labels were invented to bypass a mismatch.
- Diagnosed and repaired Sp55's fresh-clustering failure. The removed scratch annotation had materialized an AnnData view before PCA; an explicit `.copy()` now preserves that behavior. Two equally sized clusters also swap numeric IDs. Published labels are applied from an annotation table only after checking exact membership of each computed cluster; the previously observed divergent partition is rejected. A full rerun confirms the same 2,170 retained cells and labels. Doublets 2's distinct QC-cutoff difference is resolved by restoring the author-approved historical 30% ERCC setting and documenting it in Methods.

## Environment and evidence

Validation used the existing Python 3.11.8 / Scanpy 1.9.4 environment, with anndata 0.9.2, numpy 1.24.4, scipy 1.11.2, pandas 2.1.0, matplotlib 3.7.3, seaborn 0.12.2, harmonypy 0.0.9, and leidenalg 0.10.1. Historical igraph 0.10.6 was tested in an isolated local overlay without changing the user's environment. R execution used R 4.4.2, airr 1.6.1, shazam 1.3.1, and dplyr 1.2.0. `environment.yml` has not been validated as a fresh cross-platform installation or lockfile.

Per-figure execution records accompany the generated results. Detailed local logs, matrix/table comparisons, source snapshots, and side-by-side plot comparisons are retained outside this release folder in `Code/.reproduction_20261020/`. The subsequent controlled diagnosis and successful Sp55 full rerun are in `Code/.clustering_diagnosis_20261020/`. `SOURCE_MANIFEST.tsv` records the current release-source checksums. After author approval of the 30% Doublets 2 setting, both full Doublets 2 notebooks passed again. Fresh preprocessing and clustering objects were compared with the preserved references; all 3,363 global cells and all 629 Treg-B assignments match. Logs and executed copies are in `results/full_validation/`; comparison evidence is in `results/validation_evidence/D2_FINAL_VALIDATION_20261020.json`. Local audit files are retained in `Code/.methods_finalize_20261020/`. Code review and selection of a data-distribution location remain necessary before upload.
