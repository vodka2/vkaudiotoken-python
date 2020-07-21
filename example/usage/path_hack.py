import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
packagedir = os.path.join(os.path.dirname(currentdir), '..', 'src')
sys.path.insert(0, packagedir)
