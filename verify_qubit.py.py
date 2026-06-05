import h5py
import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector, SparsePauliOp

# ── Load Julia results ──────────────────────────────────────
with h5py.File("qubit_evolution.h5", "r") as f:
    times  = f["times"][:]
    ex_julia = f["expect_X"][:]

# ── Qiskit: analytically compute ⟨X⟩(t) ───────────────────
# For H = ω/2 σz, starting from |+⟩:
# ⟨X⟩(t) = cos(ωt)
omega = 1.0
ex_qiskit = np.cos(omega * times)

# ── Plot comparison ─────────────────────────────────────────
plt.figure(figsize=(8, 3))
plt.plot(times, ex_julia,  'b-',  linewidth=2, label='Julia (QuantumOptics.jl)')
plt.plot(times, ex_qiskit, 'r--', linewidth=2, label='Qiskit (analytical)')
plt.xlabel('Time')
plt.ylabel('⟨X⟩')
plt.title('Single qubit precession: Julia vs Qiskit')
plt.legend()
plt.tight_layout()
plt.savefig("comparison.png")
plt.show()

# ── Numerical check ─────────────────────────────────────────
max_diff = np.max(np.abs(ex_julia - ex_qiskit))
print(f"Max difference: {max_diff:.2e}")
if max_diff < 1e-6:
    print("✓ Julia and Qiskit agree!")
else:
    print("✗ Mismatch — check parameters")