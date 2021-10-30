"""
"""
from math import *


class Series():
    """Class for a number sequence (series).
    """
    def __init__(self):
        """Constructor.
        """
    def __init__(self, start, end, f):
        """Constructor.

        Args:
        start (int): start index
        end (int): end index
        f (function): function
        """
        self.sequence=[f(i) for i in range(start, end+1)]

    def sum(self):
        """Get the sum of the sequence.

        Returns:
        number: the sum of the sequence 
        """
        return sum(self.sequence)
        
    def dump(self):
        """Print the sequence.
        """
        import pprint
        pprint.pprint(self.sequence)
            

