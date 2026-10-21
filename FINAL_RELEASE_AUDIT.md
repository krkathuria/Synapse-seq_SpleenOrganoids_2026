# Release verification on 20 October 2026

The retained Doublets 2/4 workflows execute with the packaged inputs. **Complete reproduction of the paper has not been established.** Figure 1 atlas analyses, Figure 6 SLE analyses, non-sequencing experiments, and final assembled panel layouts are outside this collection; see `PAPER_FIGURE_COVERAGE.tsv`.

## Execution and numeric checks

- All eight notebooks and the R SHazaM script completed in an isolated copy containing only manifest-listed inputs. Source notebooks remain unexecuted; execution uses separate copies.
- Both rebuilt preprocessing matrices match their reference cell sets, gene order, highly variable gene flags, and raw expression values. Doublets 4 scaled values match exactly; the maximum Doublets 2 scaled difference is below 7e-13.
- All five rebuilt cluster partitions and named cell assignments match their references exactly (adjusted Rand index 1.0). Explicitly copying the non-spheromer Sp46 donor subset before PCA resolved the final small partition difference; its full notebook was rerun in the clean environment. Fresh UMAP layouts still differ for the four Doublets 4 objects. `validation/fresh_object_comparison.json` records the direct comparison of saved outputs before any figure-section checkpoint reload.
- Both regenerated SHazaM tables match every mutation-frequency column for all 6,308 heavy-chain records. See `validation/fresh_R_comparison.json`.
- The release Python dependencies installed in a fresh Python 3.11.8 environment on macOS ARM64 and passed `pip check`. All five figure sections passed in that environment. The exact installed set is in `requirements-tested-macos-arm64.txt`.

## Figure comparisons

The figure command generated 54 PDFs. Of these, 51 have saved exports with the same filename: 44 match the latest matching reference pixel for pixel; six violin plots preserve the distributions, labels, colors, and significance annotations, with horizontal point-jitter differences; one older SP17 dotplot differs in marker set and layout. The later SP17 Figure S3 dotplot matches. Three outputs lack a matching saved reference filename. These latter four outputs are not counted as reproduced panels.

The same comparison counts were obtained after correcting the plotting dependency conflict and rerunning in the clean environment. This is a comparison of individual saved exports, not a validation of the final assembled manuscript figures. See `validation/plot_comparison.json` and `validation/violin_text_comparison.json`.

## Data archive

The prepared archive `Synapse-seq_Doublets_data_20261020.tar.gz` contains 7,829 data/documentation files plus the release manifest, with 14,272,895,072 uncompressed file bytes. The compressed archive is 11,720,414,184 bytes. Every archive member was streamed back and checked against the manifest: no missing files, extra files, duplicates, or checksum differences were found.

Archive SHA-256:

```text
45261b520de63aaa5921050546dd3b8659e2c183212ce16bb29f45cc3aceb262
```

The archive is local; its public upload location remains unassigned. GitHub contains code, documentation, and the data inventory, not the large archive. GEO GSE351507 has not been verified to supply this complete auxiliary input set. A code clone alone is therefore not yet runnable without obtaining the archive.

## STAR Methods corrections

The accompanying local review copy now describes the implemented Doublets 2 count filter and sequencing-run ComBat correction, gene-selection and clustering settings, first-record MiXCR selection, and statistical tests. It distinguishes initial QC totals from the five final analysis objects: 7,478 distinct events from Sp17, Sp46, and Sp55, with a mean of 6,144 detected genes per event. The original open Word document was preserved.

## Remaining release work

Complete the other paper workflows and panel-level mapping if whole-paper reproduction is required; publish the auxiliary data archive at a persistent location; test a clean R installation and additional platforms; finalize the license and citation/archive identifiers; and make the repository public when appropriate. This private code upload is not a public, fully reproducible paper release.
