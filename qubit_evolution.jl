using QuantumOptics, HDF5
b = SpinBasis(1//2)
H = 0.5 * sigmaz(b)
psi0 = normalize(spinup(b) + spindown(b))
times = collect(0:0.1:10.0)
tout, psi_t = timeevolution.schroedinger(times, psi0, H)
ex = [real(expect(sigmax(b), p)) for p in psi_t]
h5open("qubit_evolution.h5", "w") do f
    f["times"] = collect(tout)
    f["expect_X"] = ex
end
println("✓ Saved to qubit_evolution.h5")
