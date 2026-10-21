# Doublets 2 and 4 analysis inputs

These local copies were copied from the study's Doublets folder for execution and comparison. The original files in Doublets are unchanged. Large data files remain excluded from Git. The code repository carries the release data manifest and download instructions separately.

- `Doublets/`: input files in the directory layout expected by the notebooks. This includes gene-count matrices, imaging-quality annotations, MiXCR AIRR exports, paired BCR annotations, and index-sort CSVs. Notebook runs may regenerate intermediate files here.
- `reference_checkpoints/`: preserved manuscript-era AnnData objects for comparison with regenerated results.
- `reference_receptor_tables/`: preserved SHM tables used to check the R calculation.
- `annotations/`: published Sp55 cluster labels extracted from the preserved object. Fresh clustering must reproduce each labeled group's complete cell membership before the label is applied. This derived table avoids relying on arbitrary numeric cluster IDs.
- `manuscript_plot_references/`: saved plot exports, grouped by their original figure-draft directory.
- `INPUT_MANIFEST.tsv`: source-relative filenames, roles, byte sizes, and checksums at the time of copying. Generated outputs may subsequently differ from their copied source checksum; the execution report records those comparisons.

Run notebooks with `analysis/` as the working directory. Their relative paths resolve to this folder. The release inventory is `../DATA_MANIFEST.tsv`; run `python scripts/verify_data.py` from the repository root before analysis. The bundle is prepared for distribution; the public download location is pending.
