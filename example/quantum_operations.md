# Quantum Operation Examples
- Not all examples featured here have been validated.

## Simple Quantum Circuit:

#### Operations:
- Apply Hadamard gate (H) to a qubit.
- Apply CNOT gate between qubits.
- Measure the qubits.
#### Purpose:
-Create superposition with the Hadamard gate.
-Entangle qubits with the CNOT gate.
-Perform a measurement to obtain classical information.

#### Code:
```python
surface_code_qubit.apply_gate('H', [(0, 0)])
surface_code_qubit.apply_gate('CNOT', [(0, 0), (0, 1)])
surface_code_qubit.measure([(0, 0), (0, 1)])
```
## Entanglement Creation:

#### Operations:
Apply Hadamard gate to the first qubit.
Apply CNOT gate between the first and second qubits.
Measure both qubits.
#### Purpose:
Create an entangled state between two qubits.
Observe quantum entanglement through measurements.
#### Code:
```python
surface_code_qubit.apply_gate('H', [(0, 0)])
surface_code_qubit.apply_gate('CNOT', [(0, 0), (0, 1)])
surface_code_qubit.measure([(0, 0), (0, 1)])
```
## Quantum Fourier Transform:

#### Operations:
Apply a series of Hadamard gates and controlled-phase (CPHASE) gates.
Perform measurements.
#### Purpose:
Implement the quantum Fourier transform for certain quantum algorithms.
Prepare the state for efficient quantum phase estimation.
#### Code:
```python
for qubit in range(size):
    surface_code_qubit.apply_gate('H', [(qubit, 0)])
    for target_qubit in range(qubit + 1, size):
        surface_code_qubit.apply_gate('CPHASE', [(qubit, 0), (target_qubit, 0)])
surface_code_qubit.measure([(0, 0), (1, 0), (2, 0)])
```

## Error Correction (Surface Code):

#### Operations:
Apply Hadamard and CNOT gates for syndrome extraction.
Measure stabilizers.
Apply X and Z corrections based on the syndrome information.
#### Purpose:
Implement surface code error correction.
Detect and correct errors using stabilizer measurements.
#### Code:
```python
num_rounds = 3  # Adjust as needed
for _ in range(num_rounds):
    surface_code_qubit.apply_gate('H', syndrome_qubits)
    surface_code_qubit.apply_gate('CNOT', [(syndrome_qubits[i], data_qubits[i]) for i in range(size)])
    syndromes = surface_code_qubit.measure_stabilizers()
    surface_code_qubit._correct_error(syndromes)
```
## Quantum Random Walk:

#### Operations:
Apply a sequence of Hadamard, CPHASE, and single-qubit rotation gates.
Perform measurements.
#### Purpose:
Simulate a quantum random walk for quantum algorithm development.
Explore quantum parallelism and interference in the walk.
#### Code:
```python
num_steps = 5  # Adjust as needed
rotation_angle = 0.2  # Adjust as needed
for step in range(num_steps):
    for qubit in range(size):
        surface_code_qubit.apply_gate('H', [(qubit, 0)])
        for target_qubit in range(size):
            if target_qubit != qubit:
                surface_code_qubit.apply_gate('CPHASE', [(qubit, 0), (target_qubit, 0)])
        surface_code_qubit.apply_gate('RX', [(qubit, 0)], angle=rotation_angle)
    surface_code_qubit.measure([(0, 0)])
```
These Python implementations demonstrate example quantum operations using the SurfaceCodeQubit class, along with explanations of their purposes. Adjust the parameters and gate configurations based on your specific goals.
