# test_crewsentinel.py
"""
Tests for CrewSentinel module.
"""

import unittest
from crewsentinel import CrewSentinel

class TestCrewSentinel(unittest.TestCase):
    """Test cases for CrewSentinel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrewSentinel()
        self.assertIsInstance(instance, CrewSentinel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrewSentinel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
