!pip install qiskit
!pip install qiskit-aer
!pip install numpy
!pip install qiskit qiskit-aer numpy

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

np.random.seed(42)
n = 10

# Alice
a_bits = np.random.randint(2, size=n)
a_bases = np.random.randint(2, size=n)

print("Alice bits:", a_bits)
print("Alice bases:", a_bases)

qc = QuantumCircuit(n, n)

# Encoding
for i in range(n):
    if a_bits[i]: qc.x(i)
    if a_bases[i]: qc.h(i)

# Bob
b_bases = np.random.randint(2, size=n)
print("Bob bases:", b_bases)

for i in range(n):
    if b_bases[i]: qc.h(i)
    qc.measure(i, i)

# Run
sim = AerSimulator()
res = sim.run(transpile(qc, sim), shots=1).result().get_counts()
b_results = np.array(list(map(int, list(res.keys())[0][::-1])))

print("Bob results:", b_results)

# Key
match = a_bases == b_bases
a_key = a_bits[match]
b_key = b_results[match]

print("Alice key:", a_key)
print("Bob key:", b_key)

print("Secure key generated" if np.array_equal(a_key, b_key) else "Key mismatch")
