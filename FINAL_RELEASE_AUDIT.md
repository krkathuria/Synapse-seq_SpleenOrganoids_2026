# Final release verification

All retained Doublets 2/4 scientific figure panels were validated against the current assembled manuscript. The scope excludes atlas, SLE, and other non-sequencing experiments. Manual Illustrator page assembly is separate. See `PUBLICATION_REVIEW.md` and `MANUSCRIPT_PANEL_MAP.tsv` for all 27 included panels and 41 exports.

## Final code execution

After publication cleanup, all eight final notebooks and the R SHazaM script completed in an isolated copy containing only manifest-listed inputs. Python ran in the newly installed, explicitly pinned numerical environment on macOS ARM64; R used the installed R 4.4.2 packages. The current source SHA-256 hashes are in every `validation/full_*.json` report. All five figure sections also passed independently. Source notebooks retain cleared outputs and execution counts.

Both fresh preprocessing matrices match their reference cell sets, gene order, highly variable gene flags, and raw expression values, with scaled-expression differences below 1e-8. All five fresh cluster partitions and named cell assignments match exactly (adjusted Rand index 1.0). Explicit donor-subset copies before PCA preserve the historical Sp46/Sp55 partitions. Four Doublets 4 fresh UMAP layouts differ; final figures explicitly use preserved publication coordinates. `validation/fresh_object_comparison.json` compares newly saved objects before checkpoint reloads.

Both regenerated SHazaM tables match every mutation-frequency column for all 6,308 heavy-chain records. See `validation/fresh_R_comparison.json`. The final Sp55 Discussion calculation confirms 53/57 IL10-positive interactions overlap with at least one retained cytotoxic marker (93.0%).

## Manuscript figures

Thirty-six of 41 final exports are pixel-identical to their latest matching saved standalone references. Four violin plots retain horizontal point-jitter differences with matching distributions and statistics. Figure 2E was corrected to the 16 markers in the assembled manuscript, superseding the older 11-marker standalone export. All 41 outputs were visually checked against the six current assembled manuscript figure pages. Layout and manual annotations remain separate.

## Data deposit

All 7,829 archive files were streamed back and verified against DATA_MANIFEST.tsv, with no missing, extra, duplicate, or mismatched files. The 11,720,414,184-byte archive was split into 18 parts; each uploaded size and GitHub SHA-256 digest matches the corresponding local part. All three companion assets were also verified. See `DATA_DISTRIBUTION.md` for the release link and download/reassembly instructions.

Archive SHA-256: `45261b520de63aaa5921050546dd3b8659e2c183212ce16bb29f45cc3aceb262`.

The analysis repository and release assets are public. STAR Methods links this repository.

## Reproducibility boundaries

The retained workflow begins with supplied count matrices and receptor tables; it is not a complete FASTQ-to-figure pipeline. A clean Python installation and `pip check` passed on macOS ARM64. The exact numerical conda artifacts were installed and tested; generic Conda solving, a fresh R installation, and other platforms remain untested. An open-source license and final publication identifiers remain pending.

STAR Methods was corrected to reflect the implemented filtering, batch correction, clustering, receptor selection, and statistics, and now links the public analysis repository. The original open manuscript document was preserved.

Exact fresh clustering requires the tested numerical binaries in `ENVIRONMENT.md`; the same SciPy version installed from an all-pip wheel failed Sp55 membership validation. No scientific parameters or source calculations were altered to resolve this environment issue.
