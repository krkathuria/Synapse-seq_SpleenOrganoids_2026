# Synapse-seq

Sequencing-analysis source for **Doublets 2 and Doublets 4**, accompanying *Synapse-seq reveals cytotoxic CD4+ T cell suppression of human antibody responses*, Kathuria et al.

## Current validation status

**Final manuscript review:** all 41 retained exports were checked against the current assembled figures, covering 27 included Doublets 2/4 panels. Obsolete and exploratory sections were removed. Read [PUBLICATION_REVIEW.md](PUBLICATION_REVIEW.md) for the final panel map, the Figure 2E correction, and precise limits (point jitter and manual page assembly).

The required local inputs have been copied into [`data/`](data/README.md). All five final manuscript figure sections execute successfully from preserved publication checkpoints. **Sp55's clustering issue is resolved.** An explicit copy before PCA restores the partition, and an exact-membership check applies the original labels despite swapped numeric cluster IDs. The author-approved historical 30% ERCC cutoff has been restored for Doublets 2 in both the release code and Methods; it reproduces all 629 manuscript cluster assignments. Doublets 4 retains 20%. Read [`CLUSTERING_DIAGNOSIS.md`](CLUSTERING_DIAGNOSIS.md) and [`VALIDATION_REPORT.md`](VALIDATION_REPORT.md) before running or releasing this collection.

Source notebooks have cleared outputs and execution counts. Executed copies and logs are saved separately. This repository covers the retained Doublets 2/4 analyses; **it does not completely reproduce all figures in the paper**. Atlas, SLE, and other non-sequencing experiments are excluded by the author. See [`PAPER_FIGURE_COVERAGE.tsv`](PAPER_FIGURE_COVERAGE.tsv) and [`MANUSCRIPT_PANEL_MAP.tsv`](MANUSCRIPT_PANEL_MAP.tsv) for exact coverage.

The final isolated rerun completed all eight notebooks and the R analysis. After explicitly copying the non-spheromer Sp46 donor subset before PCA, all five freshly computed cluster partitions and named cell assignments match the manuscript references exactly. Expression matrices and variable-gene flags also match within numerical precision. Fresh UMAP coordinates can differ; exact saved layouts are supplied for figure rendering. See [`FINAL_RELEASE_AUDIT.md`](FINAL_RELEASE_AUDIT.md).

## Contents

- [`analysis/README.md`](analysis/README.md): workflow and execution guide.
- [`data/README.md`](data/README.md): copied input files, reference checkpoints, and provenance.
- [`VALIDATION_REPORT.md`](VALIDATION_REPORT.md): actual execution and comparison results.
- [`environment.yml`](environment.yml): recorded dependency versions.
- [`SOURCE_MANIFEST.tsv`](SOURCE_MANIFEST.tsv): source provenance and current code checksums.
- [`CITATION.cff`](CITATION.cff): project citation metadata.
- [`DATA_DISTRIBUTION.md`](DATA_DISTRIBUTION.md): separate data archive and extraction instructions.
- [`DATA_MANIFEST.tsv`](DATA_MANIFEST.tsv): exact archive inventory and file checksums.

## Environment

For the tested full workflow on **macOS ARM64**, install the exact numerical builds:

```bash
conda create --yes --name synapse-seq --file conda-numerics-osx-arm64.txt
conda activate synapse-seq
python -m pip install --force-reinstall --no-deps numpy==1.24.4
python -m pip install -r requirements-tested-macos-arm64.txt
python -m pip check
```

Read [`ENVIRONMENT.md`](ENVIRONMENT.md) before installation. The historical SciPy 1.11.2 conda-forge build and its OpenBLAS dependency are necessary for exact fresh Sp55 clustering in the tested setup; the all-pip build with the same version number failed the membership check. A clean installation of the specified environment passed all eight final notebooks. The generic `environment.yml` and all-pip setup are validated for checkpoint figure rendering only.

R is separate and requires R 4.4.2 with `airr` 1.6.1, `shazam` 1.3.1, and `dplyr` 1.2.0 for the tested mutation analysis. A fresh R installation and other platforms were not tested. statannotations 0.7.2 resolves the historical package's Seaborn dependency conflict.

## Reproduce the manuscript figure sections

From the repository root:

```bash
python scripts/verify_data.py
python analysis/reproduce_manuscript_figures.py
```

This tested command loads the preserved manuscript AnnData objects and executes the final plotting sections of five notebooks. It writes PDFs under `results/<notebook-name>/`, and executed notebooks plus logs under `results/figure_validation/`. It does **not** rerun preprocessing or reclustering, and is not presented as a fresh reconstruction from sequencing reads.

To rerun all eight notebooks and the R calculation in dependency order, use `python analysis/run_full_analysis.py` after extracting an untouched data bundle and installing the R packages. It regenerates intermediate files inside `data/`. To inspect the notebooks interactively, launch Jupyter from `analysis/`. Doublets 2 preprocessing retains ERCC fraction <0.3, and Doublets 4 retains <0.2, matching the corrected Methods. BASIC/IgBLAST/Change-O processing upstream of the supplied tables is not packaged as a complete FASTQ-to-figure workflow. Final plotting cells explicitly reload preserved publication checkpoints even in full-notebook mode; fresh saved clustering objects must be compared separately.

## Data availability

Study sequencing data have GEO accession [GSE351507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE351507). Access depends on its release status. The prepared auxiliary data archive contains 7,829 files and approximately 14.27 GB before compression; its public download location is still pending. A GitHub clone alone cannot run the analyses. The accession should not be assumed to provide every auxiliary file. See [`DATA_DISTRIBUTION.md`](DATA_DISTRIBUTION.md).

## Citation and contact

Please cite the accompanying paper and archived code release when their publication identifiers are available. Repository: [Synapse-seq_SpleenOrganoids_2026](https://github.com/krkathuria/Synapse-seq_SpleenOrganoids_2026).

Code contact: [Karan R. Kathuria](https://github.com/krkathuria). Study lead contact: Mark M. Davis (mmdavis@stanford.edu).

## License

A license remains to be selected with the authors before public release. No open-source license is granted by the current private preparation repository.

Public information page (README only): https://github.com/krkathuria/Synapse-seq_SpleenOrganoids_2026-info. This analysis repository and its data remain private pending release.
