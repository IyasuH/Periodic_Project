import serial


def commands():
    user_input = input("\ntype command to get result on the periodic table:\n ")
    try:
        arduino = serial.Serial(port='COM4', baudrate=9800, timeout=.1)
    except:
        print("Could not open port")

    if user_input == "":
        arduino.write(b'')
        commands()
    elif user_input == "":
        arduino.write(b'')
        commands()
    elif user_input == "exit" or user_input == "Exit":
        arduino.close()
    else:
        print("Invalid command")
        commands()
