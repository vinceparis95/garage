from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ, BasicAer
import math

# Set up the program
alice = QuantumRegister(1, name='alice')
ep = QuantumRegister(1, name='ep')
bob = QuantumRegister(1, name='bob')
alice_c = ClassicalRegister(1, name='alicec')
ep_c = ClassicalRegister(1, name='epc')
bob_c = ClassicalRegister(1, name='bobc')
qc = QuantumCircuit(alice, ep, bob, alice_c, ep_c, bob_c)

# entangle
qc.h(ep)
qc.cx(ep, bob)
qc.barrier()

# prep payload
qc.reset(alice)
qc.h(alice)
qc.rz(math.radians(45), alice)
qc.h(alice)
qc.barrier()

# send
qc.cx(alice, ep)
qc.h(alice)
qc.measure(alice, alice_c)
qc.measure(ep, ep_c)
qc.barrier()

# receive
qc.z(bob).c_if(alice_c, 1)
qc.x(bob).c_if(ep_c, 1)

# verify
qc.h(bob)
qc.rz(math.radians(-45), bob)
qc.h(bob)
qc.measure(bob, bob_c)

# Everything below runs and draws it.
backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()

counts = result.get_counts(qc)
print('counts:',counts)

outputstate = result.get_statevector(qc, decimals=3)
print(outputstate)
qc.draw()        # draw the circuit