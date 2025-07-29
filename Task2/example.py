# cpu_ram_load.py

import time


def cpu_stress():
    x = 0
    for i in range(10**7):
        x += i**2


def memory_stress():
    big_list = [i for i in range(10**6)]
    time.sleep(3)  

if __name__ == "__main__":
    cpu_stress()
    memory_stress()
