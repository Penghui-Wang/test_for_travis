import os
import sys
sys.path.append("../test_for_travis")

from __init__ import pypy
def test_pypy():
	b = pypy()
	assert b == 13

