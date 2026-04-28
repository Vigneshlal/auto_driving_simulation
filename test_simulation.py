import unittest
from simulation import Car, run_simulation

class TestSimulation(unittest.TestCase):
    def test_single_car(self):
        carA = Car("A", 1, 2, "N", "FFRFFFFRRL")
        result = run_simulation(10, 10, [carA])
        self.assertIn(("A", 5, 4, "S"), result)

    def test_collision(self):
        carA = Car("A", 1, 2, "N", "FFRFFFFRRL")
        carB = Car("B", 7, 8, "W", "FFLFFFFFFF")
        result = run_simulation(10, 10, [carA, carB])
        # Both cars should stop at collision
        self.assertFalse(carA.active)
        self.assertFalse(carB.active)

if __name__ == "__main__":
    unittest.main()
