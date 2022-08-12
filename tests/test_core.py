import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
########

import tspec.runner

def test_dummy():
    assert tspec.runner.dummy()

def test_runner_execute_steps():
    assert True

