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

* loop : 1.6662 s
* numpy : 0.0002 s
* speed-up: 7055.01 x faster

**Tests:** all passing? yes

**Conclusion:**

* I learned how to use Git, GitHub, Conda, pytest, and NumPy.
* The NumPy version was faster than the pure-Python loop.
