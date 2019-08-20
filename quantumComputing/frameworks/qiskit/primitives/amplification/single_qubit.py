
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ, BasicAer
import math

# Set up the two registers
reg = QuantumRegister(4, name='reg')
scratch = QuantumRegister(1, name='scratch')
# create the circuit from the registers
qc = QuantumCircuit(reg, scratch)


# define the mirror operation
def main():
    # set the marked value
    number_to_flip = 9
    # set the flip number
    number_of_iterations = 2
    # place the whole register into a superposition
    qc.h(reg)

    for i in range(number_of_iterations):
        qc.barrier()
        x_bits = number_to_flip

        x_list = [reg[x] for x in range(len(reg)) if x_bits & (1 << x)]

        # set up the nots, multi-phase, and nots
        qc.x(x_list)
        multi_cz([x for x in reg])
        qc.x(x_list)
        qc.barrier()

        # run the Grover
        Grover(reg)

###############################################

## Some utility functions

# this is the beautiful mirror operation
def Grover(qreg, condition_qubits=None):
    if condition_qubits is None:
        condition_qubits = []
    qc.h(qreg)
    qc.x(qreg)
    multi_cz([x for x in qreg] + condition_qubits)
    qc.x(qreg)
    qc.h(qreg)

def multi_cz(qubits):
    # This will perform a CCCCCZ on as many qubits as we want,
    # as long as we have enough scratch qubits
    multi_cx(qubits, do_cz=True)

def multi_cx(qubits, do_cz=False):
    # This will perform a CCCCCX with as many conditions as we want,
    # as long as we have enough scratch qubits
    # The last qubit in the list is the target.
    target = qubits[-1]
    conds = qubits[:-1]
    scratch_index = 0
    ops = []
    while len(conds) > 2:
        new_conds = []
        for i in range(len(conds)//2):
            ops.append((conds[i * 2], conds[i * 2 + 1], scratch[scratch_index]))
            new_conds.append(scratch[scratch_index])
            scratch_index += 1
        if len(conds) & 1:
            new_conds.append(conds[-1])
        conds = new_conds
    for op in ops:
        qc.ccx(op[0], op[1], op[2])
    if do_cz:
        qc.h(target)
    if len(conds) == 0:
        qc.x(target)
    elif len(conds) == 1:
        qc.cx(conds[0], target)
    else:
        qc.ccx(conds[0], conds[1], target)
    if do_cz:
        qc.h(target)
    ops.reverse()
    for op in ops:
        qc.ccx(op[0], op[1], op[2])

main()

# That's the program. Everything below runs and draws it.

backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()

outputstate = result.get_statevector(qc, decimals=3)
total_prob = 0
for i,amp in enumerate(outputstate):
    if abs(amp) > 0.000001:
        prob = abs(amp) * abs(amp)
        total_prob += prob
        print('|{}> {} probability = {}%'.format(i, amp, round(prob * 100, 5)))
print('Total probability: {}%'.format(int(round(total_prob * 100))))
qc.draw()        # draw the circuit
