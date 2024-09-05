from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate, MCXGate
from qiskit.circuit.library import TwoLocal

mcx_gate = MCXGate(3) # Multi-controlled-X gate
hadamard_gate = HGate()

qc = QuantumCircuit(4)
qc.append(hadamard_gate, [0])
qc.append(mcx_gate, [0, 1, 2, 3])
qc.draw('mpl')

two_local = TwoLocal(3, 'rx', 'cz')
two_local.decompose().draw('mpl')
