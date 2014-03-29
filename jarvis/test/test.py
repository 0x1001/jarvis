import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from braintest import *
from trainertest import *
from trainingdatabasetest import *
from worddatabasetest import *
from wordparsertest import *
from lowleveltest import *

if __name__ == "__main__":
    unittest.main()