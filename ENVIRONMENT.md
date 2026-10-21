# Execution environment

The release Python package set was installed into an empty Python 3.11.8 virtual environment on macOS ARM64. Installation completed without dependency overrides, `pip check` passed, and all five checkpoint figure sections executed. The observed full package list is recorded in `requirements-tested-macos-arm64.txt`.

For an equivalent Python installation on that platform:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-tested-macos-arm64.txt
python -m pip check
python scripts/verify_data.py
python analysis/reproduce_manuscript_figures.py
```

`environment.yml` expresses the main dependencies for Conda users. The Conda solver and other platforms were not independently tested. Differences in numerical libraries can affect fresh PCA, neighbor graphs, Leiden partitions, and UMAP coordinates. The final plot command explicitly uses publication checkpoints; it must not be interpreted as evidence of fresh clustering identity.

## Compatibility correction

The historical installed environment has Seaborn 0.12.2 and statannotations 0.5.0 despite the latter package's declared Seaborn <0.12 requirement. Such a combination cannot be resolved by a normal fresh installation. The release uses statannotations 0.7.2, which permits the specified Seaborn and pandas versions. All five plot sections were rerun with this change, and comparisons retained 44 exact matching plot exports and the same text/significance annotations on the six violin plots. The numerical tests and plotting arguments in the notebooks were not changed.

## R calculation

The SHazaM script was executed with R 4.4.2, airr 1.6.1, shazam 1.3.1, and dplyr 1.2.0. R is a separate installation, and `Rscript` must be on PATH. These packages are available from CRAN; use a dedicated R library and verify the installed versions before attempting exact reproduction:

```r
install.packages(c("airr", "shazam", "dplyr"))
sapply(c("airr", "shazam", "dplyr"), packageVersion)
```

CRAN installation can select versions newer than those recorded above. A clean R installation and a complete R dependency lockfile have not been validated. This limitation remains distinct from the successful local R execution and numerical output comparisons.

## Figure comparisons

The optional `requirements-qa.txt` records the PDF/image packages used to compare plot exports. In an appropriate QA environment, run `python scripts/compare_figure_exports.py` to write per-file comparisons under `results/figure_comparison/`. Its successful exit means that comparison completed; inspect `pixel_exact` in the resulting JSON to determine which plots match.

After full notebook execution, `python scripts/compare_saved_objects.py` compares the newly saved matrices and cluster memberships to the preserved reference objects. It exits nonzero when expression or partition comparisons fail. UMAP differences are reported separately and do not disappear merely because partitions agree.
