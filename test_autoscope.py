# test_autoscope.py
"""
Tests for AutoScope module.
"""

import unittest
from autoscope import AutoScope

class TestAutoScope(unittest.TestCase):
    """Test cases for AutoScope class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoScope()
        self.assertIsInstance(instance, AutoScope)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoScope()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
