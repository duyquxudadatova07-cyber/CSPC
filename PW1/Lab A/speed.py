import time
from decay import simulate, simulate_loop


N0 = 200000
lam = 0.4
dt = 0.05
steps = 200


# Pure Python version
start = time.perf_counter()

simulate_loop(N0, lam, dt, steps, seed=0)

loop_time = time.perf_counter() - start


# NumPy version
start = time.perf_counter()

simulate(N0, lam, dt, steps, seed=0)

numpy_time = time.perf_counter() - start


# Calculate speed-up
speed_up = loop_time / numpy_time


print(f"Python loop: {loop_time:.4f} seconds")
print(f"NumPy: {numpy_time:.4f} seconds")
print(f"NumPy is {speed_up:.2f} times faster")