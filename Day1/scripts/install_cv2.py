import subprocess, sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python', 'opencv-python-stubs'])
import cv2
print('\n'.join([n for n in dir(cv2) if not n.startswith('_')]))
