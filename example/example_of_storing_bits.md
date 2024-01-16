Create instance load a bit string, then check the qubit value, 
```python
surface_code_qubit = SurfaceCodeQubit(size=8)


# Load a 4-bit string
bit_string = "1010"
surface_code.load_bit_string(bit_string)

print(f"qubit value: {surface_code.logical_qubits[0,0,0,0]}")

# Check current measurement
measurement_result = surface_code.measure((0, 0, 0, 0))
print(f"measurement_result: {measurement_result}")

# Apply gates
surface_code.apply_gate('H', target_qubits=(0, 0, 0, 0))
surface_code.apply_gate('X', target_qubits=(0, 0, 0, 0))

# Check current qubit value
print(f"qubit value: {surface_code.logical_qubits[0,0,0,0]}")

# Error Correct
syndromes = surface_code.measure_stabilizers()
surface_code._correct_error(syndromes)

# Measure again
measurement_result = surface_code.measure((0, 0, 0, 0))
print(measurement_result)
```
