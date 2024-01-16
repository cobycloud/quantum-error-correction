import unittest
import numpy as np
from surface_code_qubit import SurfaceCodeQubit

class TestSurfaceCodeQubit(unittest.TestCase):
    def setUp(self):
        self.qubit = SurfaceCodeQubit(size=3)

    def test_apply_x_gate(self):
        self.qubit.apply_gate('X', [(0, 0), (0, 1)])
        state_vector = self.qubit.get_state_vector()
        expected_state = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0], dtype=complex)
        np.testing.assert_array_almost_equal(state_vector, expected_state)

    def test_apply_z_gate(self):
        self.qubit.apply_gate('Z', [(1, 1), (2, 2)])
        state_vector = self.qubit.get_state_vector()
        expected_state = np.array([1, 0, 0, 0, -1, 0, 0, 0, 0], dtype=complex)
        np.testing.assert_array_almost_equal(state_vector, expected_state)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
