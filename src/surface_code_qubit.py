import networkx as nx
import numpy as np
from scipy.linalg import expm

class SurfaceCodeQubit:
    def __init__(self, size):
        self.size = size
        self.graph = nx.grid_2d_graph(size, size)
        self.logical_qubits = np.full((size, size, 2, 2, 2), 
                                      [[[1e-10j, 1e-10j], [1e-10j, 1e-10j]], 
                                       [[1e-10j, 1e-10j], [1e-10j, 1e-10j]]], dtype=complex)

    def load_bit_string(self, bit_string):
        # Iterate through the logical qubits and store each bit in the next qubit
        current_bit_index = 0
        for logical_qubit_row in range(self.size):
            for logical_qubit_col in range(self.size):
                for qubit_row in range(self.logical_qubits.shape[2]):
                    for qubit_col in range(self.logical_qubits.shape[3]):
                        # Check if there are still bits in the bit string
                        if current_bit_index < len(bit_string):
                            # Set the qubit value based on the bit in the bit string
                            bit_value = int(bit_string[current_bit_index])
                            self.logical_qubits[logical_qubit_row, logical_qubit_col, qubit_row, qubit_col, 0] = bit_value
                            current_bit_index += 1
                        else:
                            # If the bit string is exhausted, break out of the loop
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break

    
    def apply_gate(self, gate_type, target_qubits, angle=None):
        # Apply a gate to the qubits based on gate type
        if len(target_qubits) == 2:  # Two-qubit gate
            self._apply_two_qubit_gate(gate_type, target_qubits, angle)
        else:  # Single qubit gate
            self._apply_single_qubit_gate(gate_type, target_qubits, angle)

    def _apply_single_qubit_gate(self, gate_type, target_qubit, angle=None):
        # Apply a single qubit gate to the target qubit
        row, col, qubit_row, qubit_col = target_qubit
        target_qubit_state = self.logical_qubits[row, col, qubit_row, qubit_col]

        if gate_type == 'X':
            self._apply_x_gate(target_qubit_state)
        elif gate_type == 'Z':
            self._apply_z_gate(target_qubit_state)
        elif gate_type == 'H':
            self._apply_hadamard_gate(target_qubit_state)
        elif gate_type == 'RX':
            self._apply_rx_gate(target_qubit_state, angle)
        elif gate_type == 'RY':
            self._apply_ry_gate(target_qubit_state, angle)
        elif gate_type == 'RZ':
            self._apply_rz_gate(target_qubit_state, angle)
        elif gate_type == 'CPHASE':
            self._apply_cphase_gate(target_qubit_state, angle)

        # Update the state of the target qubit
        self.logical_qubits[row, col, qubit_row, qubit_col] = target_qubit_state

    def _apply_two_qubit_gate(self, gate_type, target_qubits, angle=None):
        # Apply a two-qubit gate to the target qubits
        control_row, control_col, control_qubit_row, control_qubit_row = target_qubits[0]
        target_row, target_col, target_qubit_row, target_qubit_row = target_qubits[1]

        control_qubit_state = self.logical_qubits[control_row, control_col, control_qubit_row, control_qubit_row]
        target_qubit_state = self.logical_qubits[target_row, target_col, target_qubit_row, target_qubit_row]

        if gate_type == 'CNOT':
            self._apply_cnot_gate(control_qubit_state, target_qubit_state)
        elif gate_type == 'CPHASE':
            self._apply_cphase_gate(control_qubit_state, target_qubit_state, angle)

        # Update the states of the target qubits
        self.logical_qubits[control_row, control_col, control_qubit_row, control_qubit_row] = control_qubit_state
        self.logical_qubits[target_row, target_col, target_qubit_row, target_qubit_row] = target_qubit_state

    def _apply_x_gate(self, target_qubit_state):
        # Apply X gate to the target qubit state
        x_gate_matrix = np.array([[0, 1], [1, 0]])
        target_qubit_state = np.dot(x_gate_matrix, target_qubit_state)

    def _apply_z_gate(self, target_qubit_state):
        # Apply Z gate to the target qubit state
        z_gate_matrix = np.array([[1, 0], [0, -1]])
        target_qubit_state = np.dot(z_gate_matrix, target_qubit_state)

    def _apply_hadamard_gate(self, target_qubit_state):
        # Apply Hadamard gate to the target qubit state
        hadamard_matrix = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
        target_qubit_state = np.dot(hadamard_matrix, target_qubit_state)

    def _apply_cnot_gate(self, control_qubit_state, target_qubit_state):
        # Apply CNOT gate to the target qubits
        cnot_matrix = np.zeros((4, 4), dtype=complex)
        cnot_matrix[0, 0] = cnot_matrix[1, 1] = cnot_matrix[2, 3] = cnot_matrix[3, 2] = 1
    
        # Apply CNOT gate to the control qubit state
        control_qubit_state = np.dot(cnot_matrix, control_qubit_state)
    
        # Apply X gate to the target qubit state if the control qubit is |1⟩
        if control_qubit_state[1] != 0:
            x_gate_matrix = np.array([[0, 1], [1, 0]])
            target_qubit_state = np.dot(x_gate_matrix, target_qubit_state)
            self.logical_qubits[control_row, control_col, control_qubit_row, control_qubit_row]
    


    def _apply_cphase_gate(self, control_qubit_state, target_qubit_state, angle):
        # Apply CPHASE gate to the target qubits
        cphase_matrix = expm(-1j * angle / 2 * np.array([[1, 0], [0, -1]]))

        control_qubit_state = np.dot(cphase_matrix, control_qubit_state)

    def _apply_rx_gate(self, target_qubit_state, angle):
        # Apply RX gate to the target qubit state
        rx_gate_matrix = expm(-1j * angle / 2 * np.array([[0, 1], [1, 0]]))
        target_qubit_state = np.dot(rx_gate_matrix, target_qubit_state)

    def _apply_ry_gate(self, target_qubit_state, angle):
        # Apply RY gate to the target qubit state
        ry_gate_matrix = expm(-1j * angle / 2 * np.array([[0, -1], [1, 0]]))
        target_qubit_state = np.dot(ry_gate_matrix, target_qubit_state)

    def _apply_rz_gate(self, target_qubit_state, angle):
        # Apply RZ gate to the target qubit state
        rz_gate_matrix = expm(-1j * angle / 2 * np.array([[1, 0], [0, -1]]))
        target_qubit_state = np.dot(rz_gate_matrix, target_qubit_state)



    def _compute_stabilizer_value(self, row, col):
        # Compute stabilizer value for a given qubit
        neighbors = list(self.graph.neighbors((row, col)))
        stabilizer_value = np.prod([self.logical_qubits[n[0], n[1]] for n in neighbors])
        return stabilizer_value

    def _compute_stabilizer_value(self, row, col):
        # Compute stabilizer value for a given qubit
        neighbors = list(self.graph.neighbors((row, col)))
        stabilizer_value = np.prod([self.logical_qubits[n[0], n[1]] for n in neighbors])
        return stabilizer_value

    def _compute_cphase_stabilizer_value(self, row, col):
        # Compute CPHASE stabilizer value for a given qubit
        neighbors = list(self.graph.neighbors((row, col)))
        stabilizer_value = np.prod([self.logical_qubits[n[0], n[1]] for n in neighbors])
        return stabilizer_value

    def measure_stabilizers(self):
        # Measure stabilizers and return the syndromes
        syndromes = np.zeros((self.size, self.size), dtype=int)
    
        for row in range(self.size):
            for col in range(self.size):
                stabilizer_value = self._compute_stabilizer_value(row, col)
                error = self._measure_stabilizer(stabilizer_value)
                syndromes[row, col] = error
    
        return syndromes
    
    # Inside measure_cphase_stabilizers function
    def measure_cphase_stabilizers(self):
        # Measure CPHASE stabilizers and return the syndromes
        syndromes = np.zeros((self.size, self.size), dtype=int)
        for node in self.graph.nodes:
            row, col = node
            stabilizer_value = self._compute_cphase_stabilizer_value(row, col)
            error = self._measure_stabilizer(stabilizer_value)
            syndromes[row, col] = error
    
        return syndromes
    
    # Inside measure_rx_stabilizers function
    def measure_rx_stabilizers(self):
        # Measure RX stabilizers and return the syndromes
        syndromes = np.zeros((self.size, self.size), dtype=int)
        for node in self.graph.nodes:
            row, col = node
            stabilizer_value = self._compute_rx_stabilizer_value(row, col)
            error = self._measure_stabilizer(stabilizer_value)
            syndromes[row, col] = error
    
        return syndromes
    
    # Inside measure_ry_stabilizers function
    def measure_ry_stabilizers(self):
        # Measure RY stabilizers and return the syndromes
        syndromes = np.zeros((self.size, self.size), dtype=int)
        for node in self.graph.nodes:
            row, col = node
            stabilizer_value = self._compute_ry_stabilizer_value(row, col)
            error = self._measure_stabilizer(stabilizer_value)
            syndromes[row, col] = error
    
        return syndromes
    
    # Inside measure_rz_stabilizers function
    def measure_rz_stabilizers(self):
        # Measure RZ stabilizers and return the syndromes
        syndromes = np.zeros((self.size, self.size), dtype=int)
        for node in self.graph.nodes:
            row, col = node
            stabilizer_value = self._compute_rz_stabilizer_value(row, col)
            error = self._measure_stabilizer(stabilizer_value)
            syndromes[row, col] = error
    
        return syndromes
    
    # Inside measure_hadamard_stabilizers function
    def measure_hadamard_stabilizers(self):
        # Measure Hadamard stabilizers and return the syndromes
        syndromes = np.zeros((self.size, self.size), dtype=int)
        for node in self.graph.nodes:
            row, col = node
            stabilizer_value = self._compute_hadamard_stabilizer_value(row, col)
            error = self._measure_stabilizer(stabilizer_value)
            syndromes[row, col] = error
    
        return syndromes

    def _measure_stabilizer(self, stabilizer_value):
        # Measure stabilizer value and return 1 if an error is detected, 0 otherwise
        probability = np.abs(stabilizer_value)**2
        result = np.random.choice([0, 1], p=[1 - probability, probability])
        return result

    def _detect_error_type(self, syndromes, row, col):
        # Implement logic to analyze syndromes and determine error type
        # Return the identified error type (e.g., 'X', 'Z', 'H', 'CPHASE', 'Phase', ...)
        cphase_error_type = self._detect_cphase_error_type(syndromes, row, col)
        if cphase_error_type == 'CPHASE':
            return 'CPHASE'
        # Add more conditions for other error types
        else:
            # Implement logic for other error types (X, Z, H, Phase, etc.)
            if syndromes[row, col] == 1:
                # Check additional conditions to identify the error type
                x_stabilizer_value = self._compute_rx_stabilizer_value(row, col)
                z_stabilizer_value = self._compute_rz_stabilizer_value(row, col)
    
                # Determine error type based on stabilizer values
                if x_stabilizer_value == 1 and z_stabilizer_value == -1:
                    return 'X'
                elif x_stabilizer_value == -1 and z_stabilizer_value == 1:
                    return 'Z'
                elif x_stabilizer_value == 1 and z_stabilizer_value == 1:
                    return 'H'
                else:
                    return 'Phase'
            else:
                return None

    def _detect_cphase_error_type(self, syndromes, row, col):
        # Implement logic to analyze CPHASE syndromes and determine error type
        # Return the identified error type (e.g., 'CPHASE', ...)
        if syndromes[row, col] == 1:
            # Check additional conditions to identify the error type
            cphase_stabilizer_value = self._compute_cphase_stabilizer_value(row, col)

            # Determine error type based on stabilizer values
            if cphase_stabilizer_value == 1:
                return 'CPHASE'
            else:
                return 'NoError'
        else:
            return None

    def _correct_error(self, syndromes):
        # Correct errors for each logical qubit based on syndromes
        for row in range(self.size):
            for col in range(self.size):
                self._correct_logical_qubit(row, col, syndromes)
    
    def _correct_logical_qubit(self, row, col, syndromes):
        # Apply correction strategy for a specific logical qubit
        logical_qubit_qubits = self.logical_qubits[row, col, :, :]
    
        for qubit_row in range(logical_qubit_qubits.shape[0]):
            for qubit_col in range(logical_qubit_qubits.shape[1]):
                self._apply_correction(row, col, qubit_row, qubit_col, syndromes)
    
    # Inside _apply_correction function
    def _apply_correction(self, row, col, qubit_row, qubit_col, syndromes):
        # Apply a correction strategy based on detected syndromes
        error_type = self._detect_error_type(syndromes, row, col)
        # Pass all parameters to correction functions
        self._apply_x_correction(row, col, qubit_row, qubit_col)
        self._apply_z_correction(row, col, qubit_row, qubit_col)
        self._apply_hadamard_correction(row, col, qubit_row, qubit_col)
        self._apply_cphase_correction(row, col, qubit_row, qubit_col)
        self._apply_phase_correction(row, col, qubit_row, qubit_col)
    
    # Inside _apply_x_correction function
    def _apply_x_correction(self, row, col, qubit_row, qubit_col):
        # Apply X correction to the qubit at (row, col)
        gate_matrix = np.array([[0, 1], [1, 0]])
        self.logical_qubits[row, col, :, :] = np.dot(
            gate_matrix, self.logical_qubits[row, col, :, :]
        )
    
    # Inside _apply_z_correction function
    def _apply_z_correction(self, row, col, qubit_row, qubit_col):
        # Apply Z correction to the qubit at (row, col)
        gate_matrix = np.array([[1, 0], [0, -1]])
        self.logical_qubits[row, col, :, :] = np.dot(
            gate_matrix, self.logical_qubits[row, col, :, :]
        )
    
    # Inside _apply_hadamard_correction function
    def _apply_hadamard_correction(self, row, col, qubit_row, qubit_col):
        # Apply Hadamard correction to the qubit at (row, col)
        hadamard_correction_matrix = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
        self.logical_qubits[row, col, :, :] = np.dot(
            hadamard_correction_matrix, self.logical_qubits[row, col, :, :]
        )
    
    # Inside _apply_cphase_correction function
    def _apply_cphase_correction(self, row, col, qubit_row, qubit_col):
        # Apply CPHASE correction to the qubit at (row, col)
        cphase_correction_matrix = expm(-1j * np.pi / 2 * np.array([[1, 0], [0, 0]]))
        self.logical_qubits[row, col, :, :] = np.dot(
            cphase_correction_matrix, self.logical_qubits[row, col, :, :]
        )
    
    # Inside _apply_phase_correction function
    def _apply_phase_correction(self, row, col, qubit_row, qubit_col):
        # Apply phase correction to the qubit at (row, col)
        phase_correction_angle = np.pi / 4  # Adjust the angle as needed
        phase_correction_matrix = expm(-1j * phase_correction_angle * np.array([[1, 0], [0, 0]]))
        self.logical_qubits[row, col, :, :] = np.dot(
            phase_correction_matrix, self.logical_qubits[row, col, :, :]
        )

    
    # Inside measure function
    def measure(self, target_qubit):
        # Measure the state of a specific qubit
        # Returns a 1x4 array representing eigenstates |00⟩, |01⟩, |10⟩, |11⟩
        logical_qubit_row, logical_qubit_col = target_qubit[:2]
        qubit_row, qubit_col = target_qubit[2:]
    
        # Get the probabilities of the individual qubit within the logical qubit
        probabilities = np.abs(self.logical_qubits[logical_qubit_row, logical_qubit_col, qubit_row, qubit_col]).flatten() ** 2
    
        # Normalize probabilities to ensure they sum to 1
        probabilities /= probabilities.sum()
        
        # Binary representations of eigenstates
        eigenstate_choices = [0, 1]
        outcomes = np.random.choice(eigenstate_choices, p=probabilities, size=1)
        return outcomes

    
    def get_state_vector(self):
        # Get the state vector of the logical qubits
        state_vector = self.logical_qubits.flatten()
        return state_vector
