print("Laundry Sentinel Simulator")

threshold = 0.50
quiet_count = 0
active_count = 0
state = "RUNNING"

while True:
    vibration = float(input("Enter vibration level: "))
    print(vibration)

    if vibration > threshold:
        if state == "IDLE":
            active_count += 1

            if active_count >= 3:
                state = "RUNNING"
                print(state)
        quiet_count = 0
      


    else:
        active_count = 0
        if state == "RUNNING":
            quiet_count += 1
            print(quiet_count) 
     
        if quiet_count >= 3:
            state = "IDLE"
            print(state)
        else: 
            print(state)