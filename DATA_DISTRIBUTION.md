# Input data distribution

The prepared Doublets 2/4 bundle contains **7,829 files (14,272,895,072 bytes)**, including reference plots and documentation. This is the input set for the workflows in `analysis/`; it is not a source-data deposit for every figure in the paper. `PAPER_FIGURE_COVERAGE.tsv` identifies the additional analyses required for that broader claim.

`DATA_MANIFEST.tsv` is the authoritative archive inventory and records the path, size, SHA-256 checksum, and role of each file. It includes the Sp55 cluster annotation table required to label a freshly computed partition. The earlier provenance manifest remains inside the data bundle as `data/INPUT_MANIFEST.tsv`; its original and regenerated checksums must not be confused.

## Obtain and verify inputs

The archive is prepared locally. **A public download location has not yet been assigned.** GEO accession GSE351507 is the sequencing-data accession and must not be treated as a verified substitute for this auxiliary input bundle. A GitHub clone alone cannot execute these analyses until the separate data archive is supplied.

Extract the data archive at the repository root, preserving its `data/` layout. Before running anything:

```bash
python scripts/verify_data.py
```

This reads and hashes every manifest-listed file, and exits unsuccessfully if any file is absent, has the wrong size, or has a different checksum. `--size-only` is a faster presence check, not an integrity check. Full analysis regenerates some intermediate files, so an integrity check after a full run may report expected changes; retain an untouched extracted bundle for validation.

## Build the distribution archive

```bash
python scripts/build_data_bundle.py ../Synapse-seq_Doublets_data_20261020.tar.gz
```

The builder first verifies all input hashes, packages only explicitly listed files, preserves relative paths, and writes a SHA-256 sidecar for the compressed archive. It excludes operating-system metadata, caches, unlisted intermediates, and generated figures. The release is separate from the code repository because of its size. Select a persistent data-repository destination, upload the archive and checksum, then add the exact download URL here.

## Included starting points

- Original count tables and imaging-quality annotations for Doublets 2 and 4.
- MiXCR AIRR exports, paired heavy/light-chain annotations, and the Change-O germline-alignment table.
- Index-sort CSVs and the Sp55 annotation lookup.
- Preserved manuscript expression/coordinate checkpoints, reference SHM tables, and saved individual plot exports.

FASTQs, alignment reference indices, and a complete BASIC/IgBLAST/Change-O reconstruction pipeline are outside this bundle. The paired `UniqueClones` table is a supplied input. These boundaries must remain explicit in any data availability statement.
