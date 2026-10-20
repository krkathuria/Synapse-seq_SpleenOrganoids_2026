# Synapse-seq

Analysis code accompanying **Synapse-seq reveals cytotoxic CD4+ T cell suppression of human antibody responses**, Kathuria et al.

Synapse-seq couples index sorting of interacting cells with single-cell RNA sequencing to study T–B cell interactions. This repository contains study notebooks for transcriptomic preprocessing, clustering, antigen-binding cell-pair analyses, immune-receptor integration, and B-cell receptor somatic hypermutation analyses.

## Status

This is a private repository being prepared for the paper's code release. It contains an initial source-code snapshot; it is not yet a versioned, end-to-end reproduction release. Notebook outputs have been cleared, and the analysis source text has been preserved. Some notebooks contain exploratory sections and original local paths. The final paper DOI, archived code DOI, and license will be added before public release.

## Repository contents

- [`analysis/`](analysis/): Python notebooks and R scripts, with a workflow guide.
- [`environment.yml`](environment.yml): Python environment specification using recorded or author-confirmed core versions. Additional dependencies are not fully pinned.
- [`SOURCE_MANIFEST.tsv`](SOURCE_MANIFEST.tsv): source-file provenance and SHA-256 checksums.
- [`CITATION.cff`](CITATION.cff): machine-readable project citation.
- [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md): remaining preparation steps for the public release.

## Data

Study sequencing data have been assigned GEO accession [GSE351507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE351507). Access depends on the repository's release status. This accession should not be assumed to contain every auxiliary input used by the notebooks.

Raw sequencing files, count matrices, processed AnnData objects, flow-cytometry data, and donor-level source data are not stored in this code repository. Notebook inputs include gene-count tables, index-sort/interaction annotations, immune-receptor calls, and processed matrices. Retain the relative directory layout referenced by each notebook when preparing inputs. The complete file-to-accession input map will accompany the final code release.

## Installation

Use a separate Conda environment:

```bash
conda env create -f environment.yml
conda activate synapse-seq
jupyter lab
```

The recorded Python version is 3.11.8, with Scanpy 1.9.4, harmonypy 0.0.9, and leidenalg 0.10.1. The environment specification is a reconstruction of recorded dependencies, not a fully tested lockfile. R scripts additionally use the Immcantation ecosystem; inspect their package imports and installation commands before running them in a dedicated R environment. BASIC, IgBLAST, Change-O, and other upstream command-line tools are separate dependencies where required.

## Running the analyses

1. Obtain the inputs for the workflow of interest and work from copies of the source data.
2. Open the relevant notebook or R script from [`analysis/README.md`](analysis/README.md).
3. Set the input and output paths to your local directories. The source snapshot retains the original paths, including individual file paths outside the main `path_data` variable.
4. Run the preprocessing and integration steps required by that workflow before running clustering or plotting sections. Some notebooks load saved intermediate files and contain alternative analysis branches; they should be reviewed section by section.
5. Save processed matrices, tables, and plots outside the tracked source-code directory.

Expected outputs include filtered and normalized AnnData objects, cluster annotations, UMAP and gene-expression plots, and immune-receptor/SHM tables. Notebooks may write intermediate files back to their configured data directories. Full runtime and memory requirements have not yet been benchmarked for this release; they depend on dataset size and workflow.

## Reproducibility notes

- Original analysis code and parameter values were preserved when assembling this snapshot; stored notebook outputs and execution metadata were removed.
- The saved preprocessing workflows have dataset-specific QC cutoffs. These are being reconciled with the final Methods before release; do not assume one common ERCC threshold for all datasets.
- File integrity, notebook structure, and absence of stored outputs were checked. The full analyses were not rerun during repository preparation.
- See the source manifest for the exact files included. This initial snapshot is not a claim that every cell corresponds to a final published panel.

## Citation

Please cite the accompanying paper when its publication details are available. For the code, cite a versioned release and its archived DOI once issued. The current repository can be identified as:

> Kathuria, K. R. Synapse-seq analysis code. https://github.com/krkathuria/Synapse-seq_SpleenOrganoids_2026

## Contact

For code questions, contact Karan R. Kathuria through [GitHub](https://github.com/krkathuria). The study's lead contact is Mark M. Davis (mmdavis@stanford.edu).

## License

A license has not yet been selected. No open-source license is granted by this private preparation repository; the license will be specified before public release.
