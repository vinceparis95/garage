from qiskit import QuantumCircuit, QuantumRegister, \
    ClassicalRegister, execute, BasicAer
import math

# Generate a random number using superposition
reg = QuantumRegister(1, name='reg')
reg_c = ClassicalRegister(1, name='regc')
qc = QuantumCircuit(reg, reg_c)

qc.reset(reg)           # write the value 0
qc.h(reg)               # put it into a superposition of 0 and 1
qc.measure(reg, reg_c)  # read the result as a digital bit

backend = BasicAer.get_backend('statevector_simulator')

job = execute(qc, backend)
result = job.result()

counts = result.get_counts(qc)
print('counts:', counts)

output_state = result.get_statevector(qc, decimals=3)
print(output_state)
qc.draw()

