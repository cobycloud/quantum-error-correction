SurfaceCodeQubit
================

The `SurfaceCodeQubit` class represents a logical qubit in a surface code quantum error correction scheme. It supports various gate operations, error correction, and measurement functionalities.

Initialization
--------------

.. code-block:: python

    # Example of usage:
    size = 3  # Set your desired size
    surface_code_qubit = SurfaceCodeQubit(size)

The logical qubits are initialized with small complex values to avoid issues during gate operations.

Gate Operations
---------------

X Gate
^^^^^^

.. code-block:: python

    surface_code_qubit.apply_gate('X', target_qubits)

Applies an X gate to the specified target qubits.

Z Gate
^^^^^^

.. code-block:: python

    surface_code_qubit.apply_gate('Z', target_qubits)

Applies a Z gate to the specified target qubits.

CNOT Gate
^^^^^^^^^

.. code-block:: python

    surface_code_qubit.apply_gate('CNOT', target_qubits)

Applies a Controlled-NOT (CNOT) gate to the specified target qubits.

Add more gate types as needed.

Measurement and Error Correction
---------------------------------

Measure Stabilizers
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    syndromes = surface_code_qubit.measure_stabilizers()

Measures stabilizers and returns the syndromes.

Correct Errors
^^^^^^^^^^^^^^

.. code-block:: python

    surface_code_qubit._correct_error(syndromes)

Enhanced error correction based on detected syndromes.

Measurement
------------

Measure Qubit State
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    result = surface_code_qubit.measure(target_qubit)

Measures the state of a specific qubit and returns the measurement result (0 or 1).

Get State Vector
^^^^^^^^^^^^^^^^

.. code-block:: python

    state_vector = surface_code_qubit.get_state_vector()

Gets the state vector of the logical qubits.

Example Usage and Notebooks
---------------------------

The `example_usage.ipynb` notebook provides a detailed example of how to use the `SurfaceCodeQubit` class. It covers various operations, measurements, and error correction procedures. Check the notebook for a step-by-step guide on working with the class.

License
-------

This project is licensed under the `MIT License <https://opensource.org/licenses/MIT>`

Contribution
------------

Contributions are welcome! Please submit a pull request to start contributing to this project.

This README provides a comprehensive guide on using the `SurfaceCodeQubit` class, including licensing and contribution details. Feel free to customize and expand it based on your specific requirements.
