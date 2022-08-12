import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
#############################

import tspec.runner
from tspec.createsteps import extractSpecDeffromfile

filename = sys.argv[1]
steps = extractSpecDeffromfile(filename, '*')

tspec.runner.execute_steps(steps)
