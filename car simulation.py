command = ""
started = False
while True:
    command = input("> ")
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "red":
        print("stop the car")
    elif command == "green":
        print("start the car")
    elif command == "yellow":
        print("start the engine")
    elif command == "help":
        print("""
start = to start the car
stop = to stop the car
quit = to quit
green = start the car
yellow = start the engine
red = stop the car
""")
    elif command == "quit":
        break
    else:
        print("sorry i don't understand")
