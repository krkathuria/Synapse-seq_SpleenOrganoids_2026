# Reproduction environment

Exact fresh clustering was tested on macOS ARM64 using Python 3.11.8, the historical conda-forge SciPy 1.11.2 build `py311h93d07a4_0`, OpenBLAS 0.3.23 with OpenMP for SciPy, and the PyPI NumPy 1.24.4 wheel (OpenBLAS 0.3.21). Package version numbers alone do not specify these numerical binaries.

## Tested installation for the full workflow

From the repository root on macOS ARM64:

```bash
conda create --yes --name synapse-seq --file conda-numerics-osx-arm64.txt
conda activate synapse-seq
python -m pip install --force-reinstall --no-deps numpy==1.24.4
python -m pip install -r requirements-tested-macos-arm64.txt
python -m pip check
python scripts/verify_data.py
python analysis/run_full_analysis.py
python scripts/compare_saved_objects.py
```

`conda-numerics-osx-arm64.txt` specifies exact artifact URLs and MD5 hashes for 43 numerical/runtime packages and their dependencies. The explicit installation avoids a new solver choice. The NumPy reinstall deliberately selects the PyPI wheel used by the historical analysis. The remaining pinned Python packages are then installed with pip; the already installed SciPy 1.11.2 satisfies its version requirement and must not be force-reinstalled from PyPI.

This procedure was tested in a new isolated prefix. Installation and `pip check` passed, followed by all eight final notebooks and the R SHazaM analysis using an isolated copy of the packaged inputs. All fresh cluster partitions and named labels were checked separately against the manuscript objects. The R installation was pre-existing; a clean R installation was not tested.

## Why the binary build matters

A fresh all-pip environment with the same SciPy version renders all five checkpoint-based figure sections successfully, but its fresh Sp55 clustering fails the exact-membership guard. That wheel links a different OpenBLAS build. In a controlled test, replacing only SciPy with the historical conda-forge build restored exact memberships and allowed the full Sp55 notebook to complete. The source code, filtering, gene selection, clustering resolution, and annotation guard were unchanged. `validation/numerical_environment.json` records the tested numerical libraries and the comparison.

The generic `environment.yml` remains useful for checkpoint figure rendering. It does not establish exact fresh clustering on other numerical builds or operating systems. Fresh UMAP coordinates can differ even when all cluster memberships match; publication figure sections explicitly use the supplied publication checkpoints.

## R calculation

The tested R installation was R 4.4.2 with `airr` 1.6.1, `shazam` 1.3.1, and `dplyr` 1.2.0. R is separate from the Python prefix, and `Rscript` must be on PATH. Install the required R packages into a dedicated library and check the recorded versions. Both SHazaM mutation-frequency outputs were compared with their references for all 6,308 heavy-chain records. A fresh R installation and other operating systems have not been validated.

## Plotting and verification

The release uses statannotations 0.7.2 because the historical 0.5.0 package declares an incompatible Seaborn requirement. The retained tests and plotting arguments were not changed to resolve that package conflict.

`python analysis/reproduce_manuscript_figures.py` renders the five final plotting sections from publication checkpoints. It generates 41 exports covering 27 included manuscript panels. See `PUBLICATION_REVIEW.md` for exact scientific-content and raster-comparison results.

The optional `requirements-qa.txt` supplies PDF/image comparison packages. `python scripts/compare_figure_exports.py` writes per-file comparisons; a successful command means the comparisons ran, not that every plot is pixel-identical. `python scripts/compare_saved_objects.py` instead checks newly computed matrices and cluster partitions after a full run.
