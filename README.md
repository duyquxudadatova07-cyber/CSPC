# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

conda env create -f PW<n>/Lab\ <X>/environment.yml

conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**

* I created the CSPC repository, set up the Conda environment, added the decay simulation, tests, and speed comparison.

**Speed comparison (loop vs NumPy):**

* loop : 1.6616 s
* numpy : 0.0002 s
* speed-up: 7746.92 x faster

**Tests:** all passing? yes

**Conclusion:**

* I learned how to use Git, GitHub, Conda, pytest, and NumPy.
* The NumPy version was faster than the pure-Python loop.
**Reproducibility test:**
- The repository was cloned into a fresh test directory.
- The environment was recreated successfully from environment.yml.
- All 3 tests passed with no changes to the code.
- Result: reproducible on the test environment.
## PW2 — Lab A: Motion from Tracking Data

### Results

Mean acceleration: -8.57 m/s²

Standard deviation: 28.71 m/s²

Maximum position difference: 0.78 m

### Noise Observation

Acceleration is noisier than position because
differentiation amplifies measurement noise.
Since acceleration is calculated using two
derivatives, the noise becomes much larger.

### Integration

I integrated acceleration to recover velocity,
then integrated velocity to recover position.

The maximum difference was 0.78 metres,
showing that integration can recover position
with a relatively small error.

## PW2 — Lab B: Optimization in Chemistry

### Part 2 — Optimization Methods

We compared three optimization methods:
Gradient Descent, Newton's Method, and SLSQP.

For the simple function, all three methods found x = 3.

For the harder function, the results depended on the
starting point and the optimization method.

### Part 3 — Reaction Rate

We used SLSQP to estimate the reaction rate constant.

Fitted k = 0.26176

### Part 4 — Chemical Equilibrium

Newton Method: x = 0.66385
SLSQP Method: x = 0.66385

H2 = 0.33615 mol
I2 = 0.33615 mol
HI = 1.32770 mol

### Part 5 — Titration

We used np.gradient() and np.argmax() to find
the equivalence point.

Equivalence point: approximately 50 mL.

### Conclusion

We learned how optimization methods can be used
to solve different chemistry problems.

