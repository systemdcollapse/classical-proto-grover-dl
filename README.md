# Classical Proto-Grover/DL (Archival Evidence)

**Repository (target):** `github.com/systemdcollapse/classical-proto-grover-dl`

## Purpose
This repository is the **classical baseline archival evidence** for project traceability.
It documents early algorithmic design choices and provides a transparent baseline for comparison with the primary hybrid quantum Cirq version.

## Scope
- Classical workflow inspired by Grover-like search logic
- Deterministic preprocessing and ranking
- Reproducible baseline benchmark outputs

## Status
**Archival / Evidence Mode** (not primary Phase 2 artifact).

## Why it matters
- Preserves methodological continuity
- Supports fair side-by-side benchmark comparison
- Strengthens technical transparency in POP/HotCRP + paper

## Non-claims
- No standalone claim of quantum advantage
- No production-readiness claim
- No final-superiority claim without controlled benchmark evidence

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python benchmarks/run_benchmark.py
```

## Reproducibility
- Fixed random seeds
- Version-pinned dependencies
- Machine-readable outputs (JSON/CSV)

## Suggested Structure
- `src/` classical implementation
- `benchmarks/` scripts + outputs
- `docs/` assumptions, limitations, reproducibility

## Citation
To be added with companion pre-print paper release.

## License
MIT or Apache-2.0 before public release.
