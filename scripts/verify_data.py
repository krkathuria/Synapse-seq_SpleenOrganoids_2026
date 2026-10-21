"""Check every distributed input before running analyses (Python standard library)."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def verify(root, manifest, check_hashes=True):
    root = root.resolve()
    errors, seen, total = [], set(), 0
    with manifest.open(newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    if not rows:
        raise ValueError('The data manifest is empty.')
    for row in rows:
        relative = row['path']
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or relative in seen:
            errors.append({'path': relative, 'error': 'unsafe or duplicate manifest path'})
            continue
        seen.add(relative)
        if not path.is_file():
            errors.append({'path': relative, 'error': 'missing'})
        elif path.stat().st_size != int(row['bytes']):
            errors.append({'path': relative, 'error': 'size mismatch'})
        elif check_hashes and sha256(path) != row['sha256']:
            errors.append({'path': relative, 'error': 'SHA-256 mismatch'})
        total += int(row['bytes'])
    return {'status': 'failed' if errors else 'passed', 'files': len(rows),
            'bytes': total, 'hashes_checked': check_hashes, 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=REPO)
    parser.add_argument('--manifest', type=Path, default=REPO / 'DATA_MANIFEST.tsv')
    parser.add_argument('--size-only', action='store_true', help='Quick preflight; does not verify file contents.')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = verify(args.root, args.manifest, not args.size_only)
    output = json.dumps(result, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output)
    print(output)
    return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    raise SystemExit(main())
