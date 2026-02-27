import time
import json
import resource
import statistics
from importlib.machinery import SourceFileLoader

mod = SourceFileLoader("alg", "/home/node/.openclaw/workspace/hybrid_cirq_v1/00_classic_baseline.py").load_module()

DATASETS = {
    "ordinato_fib_like": [1, 1, 2, 3, 5, 8, 13, 21],
    "asintotico": [1, 2, 4, 8, 16, 32, 64, 128],
    "pseudo_caotico": [7, 3, 11, 2, 13, 5, 17, 1],
}
DEPTHS = [1, 2, 3, 4, 5, 6, 7, 8]
REPEATS = 3

rows = []

for ds_name, inp in DATASETS.items():
    for d in DEPTHS:
        times = []
        rss_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        last_c0 = None
        last_c1 = None

        for _ in range(REPEATS):
            t0 = time.perf_counter()
            traj, c0, c1 = mod.algoritmo_gravitazionale_aureo(inp, depth_max=d)
            dt = time.perf_counter() - t0
            times.append(dt)
            last_c0, last_c1 = c0, c1

        rss_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        p95_index = int(0.95 * (len(times) - 1))

        rows.append({
            "dataset": ds_name,
            "input_len": len(inp),
            "depth": d,
            "time_mean_s": round(statistics.mean(times), 6),
            "time_p95_s": round(sorted(times)[p95_index], 6),
            "time_max_s": round(max(times), 6),
            "num_colonne_c0_last": last_c0,
            "num_colonne_c1_last": last_c1,
            "num_colonne_tot_last": (last_c0 or 0) + (last_c1 or 0),
            "traj_len_final": len(traj),
            "ru_maxrss_before_kb": rss_before,
            "ru_maxrss_after_kb": rss_after,
        })

out = "/home/node/.openclaw/workspace/benchmark_v1_results.json"
with open(out, "w") as f:
    json.dump(rows, f, indent=2)

print(f"OK -> {out}")
for r in rows:
    print(r)
