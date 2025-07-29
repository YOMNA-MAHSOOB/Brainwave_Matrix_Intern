# suspicious_script.py

import os
import subprocess
import time

# simulate cpu and memory usage
def consume_resources():
    data = [i for i in range(1000000)]
    result = 0
    for i in range(1000000):
        result += i ** 2
    time.sleep(2)

# suspicious behavior
os.system("rm -rf /tmp/suspicious_folder")
subprocess.Popen(["ls", "-la"])
consume_resources()
