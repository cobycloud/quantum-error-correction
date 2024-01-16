

## Import the SurfaceCodeQubit Class
```python
from surface_code_quit import SurfaceCodeQubit
```
## Function to store classical bits in the logical qubits
```python
def store_bits(surface_code_qubit, num_bits):
    # Generate random sequence of bits (0s and 1s)
    random_bits = np.random.randint(2, size=num_bits)

    # Store each bit in the corresponding logical qubit
    for idx, bit in enumerate(random_bits):
        row = idx // surface_code_qubit.size
        col = idx % surface_code_qubit.size

        # Apply X gate if the bit is 1
        if bit == 1:
            surface_code_qubit.apply_gate('X', (row, col))

    return random_bits
```

## Create SurfaceCodeQubit
- This creates an 8x8 array of logical qubits.
- Each logical qubit is a 2x2 array of qubits.
  
```python
surface_code_qubit = SurfaceCodeQubit(size=8)

```

## Store Bits
```python
stored_bits = store_bits(surface_code_qubit, num_bits=64)

print(stored_bits)

```
```python
# Result
[0 0 0 1 0 1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 1 1 1 0 1 0 0 1 0 1 0 0 1 1 1 1 1
     0 1 1 1 0 0 0 1 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 1 1 0 1]
```

    

## Get measurements of all logical qubits
```python
measurement_results = np.zeros(64, dtype=int)
for idx in range(64):
    row = idx // 8
    col = idx % 8
    measurement_results[idx] = surface_code_qubit.measure((row, col))

print(measurement_results)
```
```python
# Result
[0 0 3 1 2 2 3 3 1 0 2 0 2 2 0 2 2 2 0 2 3 0 3 3 2 1 3 0 1 0 0 2 2 3 2 2 1
     1 1 0 1 2 1 1 0 0 2 3 1 1 2 3 2 1 1 1 0 3 0 2 1 1 0 2]
```

    
    
