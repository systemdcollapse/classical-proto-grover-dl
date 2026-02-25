# Benchmark Protocol (Classical vs Hybrid Quantum Cirq)

## Goal
Provide a fair and reproducible comparison between:
- Classical Proto-Grover/DL baseline
- Hybrid Quantum-Classical PoC (Cirq, DL/Grover)

## Fairness Rules (must-pass)
1. Same input datasets/splits
2. Same evaluation metrics
3. Same preprocessing pipeline
4. Fixed random seeds
5. Same reporting template
6. No post-hoc cherry-picking

## Minimum Run Matrix (v0)
- Seeds: `42, 1337, 2026`
- Dataset sizes: `S, M, L`
- Trials per config: `>= 10`
- Output format: JSON + CSV

## Metrics
- Primary task score (define explicitly)
- Runtime (wall-clock)
- Variance/std across trials
- Compute-cost proxy (where possible)

## Output Schema (JSON)
```json
{
  "experiment_id": "string",
  "method": "classical|hybrid_cirq",
  "dataset": "string",
  "seed": 42,
  "trial": 1,
  "task_score": 0.0,
  "runtime_s": 0.0,
  "notes": "optional"
}
```

## Reporting Rules
- Report mean ± std
- Include confidence interval where possible
- Explicitly list failure cases
- Separate empirical results from theoretical complexity claims

## Initial Advantage Signal (Preliminary)
For early internal checks only, classify as:
- `No signal`
- `Weak signal`
- `Promising signal`

Only upgrade language after repeated, reproducible evidence.
