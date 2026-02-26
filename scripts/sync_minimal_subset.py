"""#!/usr/bin/env python3
"""
import argparse
import os
import pathlib
import sys
import urllib.request

REPO_OWNER = "ByteDance-Seed"
REPO_NAME = "bamboo_mixer"
COMMIT_SHA = "fd2ea327c01d5cafecbcae9a9dc83070091f54b9"

FILES = [
    "bamboo_mixer/mol/__init__.py",
    "bamboo_mixer/mol/conformer.py",
    "bamboo_mixer/mol/molecule.py",
    "bamboo_mixer/mol/moleculegraph.py",
    "bamboo_mixer/mol/topology.py",
    "bamboo_mixer/mol/rkutil/__init__.py",
    "bamboo_mixer/mol/rkutil/conformer.py",
    "bamboo_mixer/mol/rkutil/helper.py",
    "bamboo_mixer/mol/rkutil/information.py",
    "bamboo_mixer/mol/rkutil/match_and_map.py",
    "bamboo_mixer/mol/rkutil/plot.py",
    "bamboo_mixer/mol/rkutil/resonance.py",
    "bamboo_mixer/mol/rkutil/sanitize.py",
    "bamboo_mixer/mol/rkutil/symmetry.py",
    "bamboo_mixer/mol/rkutil/tables.py",
    "bamboo_mixer/utils/__init__.py",
    "bamboo_mixer/utils/model_utils.py",
    "bamboo_mixer/utils/mol_utils.py",
    "bamboo_mixer/utils/nested_data.py",
    "bamboo_mixer/utils/simple_unit.py",
    "bamboo_mixer/utils/utils.py",
    "bamboo_mixer/predictor/gnn.py",
    "bamboo_mixer/predictor/graph_block.py",
    "bamboo_mixer/predictor/readout.py",
    "scripts/prepare_data/prepare_data.py",
]

def build_raw_url(path: str) -> str:
    return (
        f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/"
        f"{COMMIT_SHA}/{path}"
    )

def download_file(path: str, destination_root: pathlib.Path) -> None:
    url = build_raw_url(path)
    dest_path = destination_root / path
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
    except Exception as exc:
        raise RuntimeError(f"Failed to download {url}: {exc}") from exc
    dest_path.write_bytes(content)

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Sync the minimal bamboo_mixer subset into this repository.",
    )
    parser.add_argument(
        "--dest",
        default=".",
        help="Destination root directory (defaults to current directory).",
    )
    args = parser.parse_args(argv)

    destination_root = pathlib.Path(args.dest).resolve()
    for rel_path in FILES:
        download_file(rel_path, destination_root)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
