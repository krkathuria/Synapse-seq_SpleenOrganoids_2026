"""Build an integrity-checked data archive from the explicit release manifest."""
import argparse
import csv
import json
import tarfile
from pathlib import Path
from verify_data import REPO, sha256, verify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path, help='New .tar.gz archive path; existing files are not overwritten.')
    args = parser.parse_args()
    manifest = REPO / 'DATA_MANIFEST.tsv'
    report = verify(REPO, manifest)
    if report['errors']:
        raise SystemExit(json.dumps(report, indent=2))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('xb') as stream:
        with tarfile.open(fileobj=stream, mode='w:gz', compresslevel=1, format=tarfile.PAX_FORMAT) as archive:
            with manifest.open(newline='') as handle:
                rows = list(csv.DictReader(handle, delimiter='\t'))
            for row in rows:
                archive.add(REPO / row['path'], arcname=row['path'], recursive=False)
            archive.add(manifest, arcname='DATA_MANIFEST.tsv', recursive=False)
    digest = sha256(args.output)
    checksum = args.output.with_name(args.output.name + '.sha256')
    checksum.write_text(f'{digest}  {args.output.name}\n')
    print(json.dumps({'archive': str(args.output), 'sha256': digest, 'files': len(rows), 'bytes': args.output.stat().st_size}, indent=2))


if __name__ == '__main__':
    main()
