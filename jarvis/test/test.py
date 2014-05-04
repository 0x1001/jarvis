import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

##from braintest import *
##from trainertest import *
##from trainingdatabasetest import *
##from worddatabasetest import *
##from wordparsertest import *
##from lowleveltest import *
##from jarvistest import *
##from worddatabasebuildertest import *
##from trainingdatabasebuildertest import *
from databasebuildertest import *
##from neuraltrainertest import *
##from abilitiesdatabasetest import *
##from abilitiesdatabasebuilderstest import *
##from abilitytest import *
##from bodytest import *
##from recordtest import *
##from voicetest import *
##from consoletest import *
from innervoicetest import *
from innervoicedatabasebuildertest import *
from innervoicedatabasetest import *

if __name__ == "__main__":
    unittest.main()