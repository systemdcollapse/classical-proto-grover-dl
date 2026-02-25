# Hybrid Quantum-Classical PoC (Cirq, DL/Grover)

**Repository (target):** `github.com/systemdcollapse/hybrid-quantum-cirq-poc`

## Overview
This is the **primary Phase 2 artifact**:
- Hybrid quantum-classical PoC in **Cirq**
- Reproducible benchmark protocol vs classical baseline
- Submission-grade documentation for POP/HotCRP

## Objective
Evaluate whether a DL/Grover-inspired hybrid strategy improves search/ranking efficiency under controlled, reproducible conditions.

## Contribution Type
**Novel Algorithm** (hybrid quantum-classical, Cirq simulation-first).

## Core Components
- **Classical Baseline**: fair reference model
- **Hybrid PoC (Cirq)**: quantum subroutine + classical orchestration
- **Benchmark Suite**: same datasets, same metrics, same constraints

## Benchmark Policy
No overclaiming. Any quantum-advantage statement must include:
1. Explicit setup
2. Reproducible scripts
3. Stated limitations and uncertainty

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python benchmarks/run_benchmark.py
```

## Reproducibility
- Pinned dependencies
- Fixed seeds
- Environment notes in `docs/reproducibility.md`
- Machine-readable benchmark outputs

## Current Status
**Active hardening (pre-submission).**

## Short Roadmap
- Lock benchmark protocol
- Publish first comparative results
- Tag submission release
- Sync with companion paper on moltbook.com

## Limitations
- Simulation-first evidence
- Context-dependent performance
- Robustness tests still in progress

## Citation
To be added with paper publication on moltbook.com.

## License
MIT or Apache-2.0 before public release.
