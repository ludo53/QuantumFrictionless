# test_quantumfrictionless.py
"""
Tests for QuantumFrictionless module.
"""

import unittest
from quantumfrictionless import QuantumFrictionless

class TestQuantumFrictionless(unittest.TestCase):
    """Test cases for QuantumFrictionless class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumFrictionless()
        self.assertIsInstance(instance, QuantumFrictionless)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumFrictionless()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
