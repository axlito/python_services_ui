import os
import subprocess

command = subprocess.Popen('ping 10.0.0.1')
response = command.communicate()

print(response)
