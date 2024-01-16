# Quantum Error Correction Library User Guide

## Introduction

Welcome to the Quantum Error Correction Library user guide! This guide provides information on how to use the library to simulate quantum error correction using the surface code.

## Table of Contents

1. [Installation](#installation)
2. [Getting Started](#getting-started)
   - [Creating a SurfaceCodeQubit](#creating-a-surfacecodequbit)
   - [Applying Quantum Gates](#applying-quantum-gates)
   - [Measuring Qubits](#measuring-qubits)
3. [Advanced Usage](#advanced-usage)
   - [Error Detection and Correction](#error-detection-and-correction)
   - [State Retrieval](#state-retrieval)
4. [Example Usage](#example-usage)
5. [Conclusion](#conclusion)

## Installation

To use the Quantum Error Correction Library, follow these steps:

```bash
pip install quantum-error-correction
```
##  Getting Started
### Creating a SurfaceCodeQubit
To create a logical qubit in the surface code, instantiate the SurfaceCodeQubit class:


```python
from quantum_error_correction import SurfaceCodeQubit

size = 3  # Set your desired size
surface_code_qubit = SurfaceCodeQubit(size)
```

### Applying Quantum Gates
Apply quantum gates (X, Z, CNOT) to the logical qubits:

```python
# Example: Apply X gate to qubits at positions (0, 0) and (0, 1)
surface_code_qubit.apply_gate('X', [(0, 0), (0, 1)])

```
### Measuring Qubits
Simulate quantum measurements on specific qubits:
```python
# Example: Measure the state of the qubit at position (0, 0)
measurement_result = surface_code_qubit.measure((0, 0))
```
## Advanced Usage

### Error Detection and Correction
The library provides methods for simulating error detection and correction:

```python
# Example: Measure stabilizers and correct errors
syndromes = surface_code_qubit.measure_stabilizers()
surface_code_qubit.correct_errors(syndromes)

### State Retrieval
Retrieve the state vector of the logical qubits:

```python
# Example: Get the state vector
state_vector = surface_code_qubit.get_state_vector()
```

### Example Usage
See the provided example_usage.ipynb notebook for a detailed example of library usage.

### Conclusion
The Quantum Error Correction Library offers a convenient way to explore quantum error correction using the surface code. Experiment with different gate operations, error correction techniques, and analyze simulation outcomes.
