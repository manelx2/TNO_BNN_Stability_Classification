#!pip install rebound
import rebound
import numpy as np
import pandas as pd
import os
from datetime import datetime
from multiprocessing import Pool, cpu_count

# Disable SSL verification for rebound horizons if needed
rebound.horizons.SSL_CONTEXT = "unverified"

# Configuration
n_new_samples = 40  # Number of new simulations to run this batch
simulation_time_years = 1e6  # 1 million years
max_a_for_ejection = 100  # AU threshold for ejection
file_prefix = "kuiper_dataset_part"
output_csv = f"{file_prefix}.csv"  # Use fixed file name to keep appending to same file

def setup_simulation():
    sim = rebound.Simulation()
    sim.add("Sun")
    sim.add("Jupiter")
    sim.add("Saturn")
    sim.add("Uranus")
    sim.add("Neptune")
    sim.move_to_com()
    sim.dt = 0.05
    return sim

def run_simulation(_):
    sim = setup_simulation()

    a_rand = np.random.uniform(15.0, 28.0)
    e_rand = np.random.uniform(0.6, 0.95)
    i_rand = np.random.uniform(20.0, 90.0)

    sim.add(a=a_rand, e=e_rand, inc=np.radians(i_rand), primary=sim.particles[0])

    try:
        sim.integrate(simulation_time_years * 2 * np.pi)
        test_particle = sim.particles[-1]
        is_stable = 1 if test_particle.a < max_a_for_ejection else 0
    except rebound.Escape:
        is_stable = 0
    except Exception:
        is_stable = 0

    return [a_rand, e_rand, i_rand, is_stable]

def main():
    # Load existing data if any
    if os.path.exists(output_csv):
        print(f"Loading existing data from {output_csv}...")
        df_existing = pd.read_csv(output_csv)
        print(f"Existing samples: {len(df_existing)}")
    else:
        print("No existing data found. Starting fresh.")
        df_existing = pd.DataFrame(columns=["a", "e", "i", "is_stable"])

    print(f"Running {n_new_samples} new simulations on {cpu_count()} CPUs...")

    with Pool(processes=cpu_count()) as pool:
        new_data = pool.map(run_simulation, range(n_new_samples))

    df_new = pd.DataFrame(new_data, columns=["a", "e", "i", "is_stable"])

    # Combine old and new data
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)

    df_combined.to_csv(output_csv, index=False)
    print(f"✅ Saved total {len(df_combined)} samples to {output_csv}")

if __name__ == "__main__":
    main()

