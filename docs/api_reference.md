# Quantum Error Correction Library API Reference

## SurfaceCodeQubit Class

### `__init__(self, size: int) -> None`

- **Description:** Initializes a logical qubit in the surface code.

- **Parameters:**
  - `size` (int): Size of the surface code grid.

### `apply_gate(self, gate_type: str, target_qubits: List[Tuple[int, int]]) -> None`

- **Description:** Applies a quantum gate to the logical qubits.

- **Parameters:**
  - `gate_type` (str): Type of the gate ('X', 'Z', 'CNOT').
  - `target_qubits` (List[Tuple[int, int]]): List of target qubits for the gate.

### `measure(self, target_qubit: Tuple[int, int]) -> int`

- **Description:** Simulates a quantum measurement on a specific qubit.

- **Parameters:**
  - `target_qubit` (Tuple[int, int]): Coordinates of the target qubit.

- **Returns:**
  - `int`: Measurement result (0 or 1).

### `measure_stabilizers(self) -> np.ndarray`

- **Description:** Measures stabilizers on the surface code grid.

- **Returns:**
  - `np.ndarray`: Array of syndromes representing measured stabilizers.

### `correct_errors(self, syndromes: np.ndarray) -> None`

- **Description:** Corrects errors based on detected syndromes.

- **Parameters:**
  - `syndromes` (np.ndarray): Array of syndromes representing measured stabilizers.

### `get_state_vector(self) -> np.ndarray`

- **Description:** Retrieves the state vector of the logical qubits.

- **Returns:**
  - `np.ndarray`: State vector of the logical qubits.
