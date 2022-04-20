# building car game
# modified problems

is_started = False
is_stopped = False
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit program
        """)
    elif command == "start":
        if is_started:
            print("car has already started")
        else:
            print("car has started")
            is_started = True
            is_stopped = False
    elif command == "stop":
        if is_stopped:
            print("car has already stopped")
        else:
            print("car has stopped")
            is_stopped = True
            is_started = False
    elif command == "quit":
        break
    else:
        print("I don't understand that...")

# is stopped is redundant here just use is_started
# or not started (not operator)
