import numpy as np
import random

frog_calls = 0

def frog(x):
    global frog_calls
    frog_calls += 1
    x1, x2 = x
    return (
        x1 * np.sin(np.sqrt(abs(x2 + 1 - x1))) *
        np.cos(np.sqrt(abs(x1 + x2 + 1))) +
        (x2 + 1) * np.cos(np.sqrt(abs(x2 + 1 - x1))) *
        np.sin(np.sqrt(abs(x1 + x2 + 1)))
    )

def clip(value):
    return max(-512, min(512, value))

def RHC(start_point, z, p, seed):
    rng = random.Random(seed)

    current = np.array(start_point, dtype=float)
    current_value = frog(current)

    while True:
        best_neighbor = current
        best_value = current_value

        for _ in range(p):
            z1 = rng.uniform(-z, z)
            z2 = rng.uniform(-z, z)
            neighbor = np.array([clip(current[0] + z1), clip(current[1] + z2)])
            value = frog(neighbor)
            if value < best_value:
                best_neighbor = neighbor
                best_value = value

        # Stop when no neighbor improves the current solution
        if best_value >= current_value:
            break

        current = best_neighbor
        current_value = best_value

    return current, current_value

def RHCR2(sp, z, p, seed):
    global frog_calls
    frog_calls = 0

    sol1, val1 = RHC(sp, z, p, seed)
    calls1 = frog_calls

    sol2, val2 = RHC(sol1, z / 20, p, seed)
    calls2 = frog_calls - calls1

    sol3, val3 = RHC(sol2, z / 400, p, seed)
    calls3 = frog_calls - calls1 - calls2

    return {
        "sol1": (sol1, val1),
        "sol2": (sol2, val2),
        "sol3": (sol3, val3),
        "calls": {
            "run1": calls1,
            "run2": calls2,
            "run3": calls3,
            "total": frog_calls
        }
    }

if __name__ == "__main__":
    starting_points = [(-300, -400), (0, 0), (-222, -222), (-510, 400)]
    ps    = [120, 400]
    zs    = [9, 50]
    seeds = [1, 2]

    results = []

    for p in ps:
        for z in zs:
            for sp in starting_points:
                for seed in seeds:
                    result = RHCR2(sp, z, p, seed)
                    results.append({
                        "p": p, "z": z, "sp": sp, "seed": seed,
                        "sol1": result["sol1"],
                        "sol2": result["sol2"],
                        "sol3": result["sol3"],
                        "calls": result["calls"]
                    })

for r in results:
    c = r["calls"]

    sol1_xy = tuple(float(x) for x in np.round(r["sol1"][0], 4))
    sol2_xy = tuple(float(x) for x in np.round(r["sol2"][0], 4))
    sol3_xy = tuple(float(x) for x in np.round(r["sol3"][0], 4))

    print("\n--------------------------------------------")
    print(f"p = {r['p']}, z = {r['z']}")
    print(f"starting point = {r['sp']}")
    print(f"run (seed) = {r['seed']}")
    print()
    print(f"sol1 = {sol1_xy},   f(sol1) = {r['sol1'][1]:.6f}")
    print(f"sol2 = {sol2_xy},   f(sol2) = {r['sol2'][1]:.6f}")
    print(f"sol3 = {sol3_xy},   f(sol3) = {r['sol3'][1]:.6f}")
    print()
    print(
        f"calls: "
        f"r1 = {c['run1']}, "
        f"r2 = {c['run2']}, "
        f"r3 = {c['run3']}, "
        f"total = {c['total']}"
    )
    print("--------------------------------------------")

    # ================================
# 33rd Run: Preferred Choice
# ================================

print("\n============================================")
print("33rd Run (Preferred Choice)")
print("============================================")

preferred_sp = (-520, 40)
preferred_p  = 400
preferred_z  = 50
preferred_seed = 33

result_33 = RHCR2(
    sp=preferred_sp,
    z=preferred_z,
    p=preferred_p,
    seed=preferred_seed
)

sol1_33, val1_33 = result_33["sol1"]
sol2_33, val2_33 = result_33["sol2"]
sol3_33, val3_33 = result_33["sol3"]
calls_33 = result_33["calls"]

print(f"p = {preferred_p}, z = {preferred_z}")
print(f"starting point = {preferred_sp}")
print(f"run (seed) = {preferred_seed}\n")

sol1_xy = tuple(float(x) for x in np.round(sol1_33, 4))
sol2_xy = tuple(float(x) for x in np.round(sol2_33, 4))
sol3_xy = tuple(float(x) for x in np.round(sol3_33, 4))

print(f"sol1 = {sol1_xy},   f(sol1) = {val1_33:.6f}")
print(f"sol2 = {sol2_xy},   f(sol2) = {val2_33:.6f}")
print(f"sol3 = {sol3_xy},   f(sol3) = {val3_33:.6f}")

print(
    f"calls: "
    f"r1 = {calls_33['run1']}, "
    f"r2 = {calls_33['run2']}, "
    f"r3 = {calls_33['run3']}, "
    f"total = {calls_33['total']}"
)

print("============================================")