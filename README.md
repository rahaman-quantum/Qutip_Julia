# QuTiP + Julia + Qiskit: Hybrid Quantum HPC Benchmarks

A hands-on exploration of running **Julia and Python side-by-side** in VS Code
for quantum simulation and HPC workflows — comparing speed, accuracy, and
ease of use across three ecosystems.

---

## Why Julia + Python Together?

Python has the best quantum libraries (QuTiP, Qiskit).
Julia has the best raw compute speed (LAPACK, ITensors).
Together they cover the full quantum HPC pipeline:

| Julia | Python |
|-------|--------|
| Heavy linear algebra | QuTiP (open systems) |
| MPS / tensor networks | Qiskit (circuits, IBM hardware) |
| ODE / time evolution | scikit-learn (ML readout) |
| Fast eigensolvers | matplotlib (plotting & analysis) |

---

## Environment Setup

### 1. Python Virtual Environment
```bash
python3 -m venv julia_qiskit
source julia_qiskit/bin/activate
pip install qutip qiskit>=2.3 qiskit-aer numpy scipy \
            matplotlib h5py jupyter jupyterlab ipykernel
python -m ipykernel install --user --name julia_qiskit \
            --display-name "Python (julia_qiskit)"
```

### 2. Julia Installation (Mac)
```bash
brew install julia
```

### 3. Julia Packages
Open Julia REPL:
```bash
julia
```
Then inside the REPL:
```julia
using Pkg
Pkg.add(["QuantumOptics", "ITensors", "ITensorMPS",
         "DifferentialEquations", "KrylovKit",
         "HDF5", "LinearAlgebra", "DelimitedFiles",
         "Plots", "IJulia"])
using IJulia
installkernel("Julia")
exit()
```

---

## Dual Kernel Setup in VS Code

This is the core workflow — **two kernels, one project.**
Run Julia and Python in separate notebooks, share data via HDF5.

### Step 1: Install VS Code Extensions
```
Cmd+Shift+X → search and install:
  ├── "Python"  by Microsoft
  ├── "Jupyter" by Microsoft
  └── "Julia"   by julialang
```

### Step 2: Create a New Notebook
```
Cmd+Shift+P → type "Create: New Jupyter Notebook" → Enter
```

### Step 3: Select Kernel Per Notebook
```
Top right corner → "Select Kernel":
  ├── For QuTiP / Qiskit  → Python Environments → julia_qiskit
  └── For Julia code      → Jupyter Kernel      → Julia 1.12
```

### Step 4: Share Data Between Julia and Python via HDF5
Julia computes and saves:
```julia
using HDF5, LinearAlgebra
A = rand(4, 4); A = A + A'
evals = eigvals(Hermitian(A))
h5open("results.h5", "w") do f
    f["eigenvalues"] = evals
end
```
Python loads and plots:
```python
import h5py, numpy as np
with h5py.File("results.h5", "r") as f:
    evals = f["eigenvalues"][:]
print("Eigenvalues from Julia:", evals)
```

---

## Notebooks

| File | Kernel | Description |
|------|--------|-------------|
| `julia_1.ipynb` | Julia + Python | Eigenvalue decomposition benchmark: NumPy vs QuTiP vs Julia on a 4×4 Hermitian matrix |

---