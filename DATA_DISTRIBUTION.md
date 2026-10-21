# Input data distribution

The complete auxiliary bundle for the retained Doublets 2/4 workflows contains **7,829 files (14,272,895,072 uncompressed bytes)**, plus DATA_MANIFEST.tsv. It is supplied as 18 parts in the [GitHub release](https://github.com/krkathuria/Synapse-seq_SpleenOrganoids_2026/releases/tag/doublets2-4-20261020). The analysis repository and this data release are public.

`DATA_MANIFEST.tsv` records every file path, size, SHA-256, and role. It includes the Sp55 cluster-annotation lookup. The earlier `data/INPUT_MANIFEST.tsv` records source provenance; its original and regenerated checksums serve a different purpose.

## Download, reassemble, and verify

Download the 18 data-part files listed in `PARTS.json` (`.part01`, `.part02`, and `.part03.001` through `.part06.004`), `SHA256SUMS`, `PARTS.json`, and `README.txt` from the release into one directory. The first two parts are 2 GB each; the remaining parts are at most 500 MB to avoid large-transfer timeouts.

```bash
cat Synapse-seq_Doublets_data_20261020.tar.gz.part0[1-6]* > Synapse-seq_Doublets_data_20261020.tar.gz
shasum -a 256 -c SHA256SUMS
# Linux alternative: sha256sum -c SHA256SUMS
tar -xzf Synapse-seq_Doublets_data_20261020.tar.gz -C /path/to/Synapse-seq_SpleenOrganoids_2026
```

The complete archive is 11,720,414,184 bytes, with SHA-256:

```text
45261b520de63aaa5921050546dd3b8659e2c183212ce16bb29f45cc3aceb262
```

At the repository root, before running any analysis:

```bash
python scripts/verify_data.py
```

This hashes every manifest-listed file and fails on absence, size mismatch, or checksum mismatch. `--size-only` checks presence and size only. The full analysis regenerates intermediates, so retain an untouched bundle for integrity validation.

All 18 uploaded part sizes and GitHub's server-side SHA-256 digests were checked against the local parts. The three companion assets were checked likewise. Before splitting, every archive member was read back and checked against DATA_MANIFEST.tsv, with no missing, extra, duplicate, or mismatched files. Compact upload evidence is in `validation/release_assets.json`.

## Included starting points and scope

- Count tables and imaging-quality annotations for Doublets 2 and 4.
- MiXCR AIRR exports, paired heavy/light-chain annotations, and the Change-O germline-alignment table.
- Index-sort CSVs and the Sp55 annotation lookup.
- Preserved manuscript checkpoints, SHM tables, and plot references.

These are all required inputs for the packaged count-matrix/AIRR-table workflows. FASTQs, alignment indices, and a complete BASIC/IgBLAST/Change-O reconstruction pipeline are outside the bundle. The paired UniqueClones table is supplied as an input. Atlas, SLE, and other non-sequencing experiments are outside the author-approved scope. GEO GSE351507 is the sequencing accession, not a verified replacement for this auxiliary bundle.

To rebuild the archive from an unchanged local data directory, run `python scripts/build_data_bundle.py ../Synapse-seq_Doublets_data_20261020.tar.gz`.

For the tested numerical environment and full-analysis commands, see `ENVIRONMENT.md` and `analysis/README.md`.
