# test_streamllama.py
"""
Tests for StreamLlama module.
"""

import unittest
from streamllama import StreamLlama

class TestStreamLlama(unittest.TestCase):
    """Test cases for StreamLlama class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StreamLlama()
        self.assertIsInstance(instance, StreamLlama)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StreamLlama()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
