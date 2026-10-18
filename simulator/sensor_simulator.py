print("Laundry Sentinel Simulator")

threshold = 0.50
quiet_count = 0
active_count = 0
state = "RUNNING"

while True:
    vibration = float(input("Enter vibration level: "))
    print("Vibration:", vibration)

    if vibration > threshold:
        if state == "IDLE":
            active_count += 1

            if active_count >= 3:
                state = "RUNNING"
                print("STATE CHANGE:", state)
        quiet_count = 0
      


    else:
        active_count = 0
        if state == "RUNNING":
            quiet_count += 1
         
     
        if quiet_count >= 3:
            state = "IDLE"
            print("STATE CHANGE:", state)
    
    
    print("Current State:", state)
    print("Active Count:", active_count)
    print("Quiet Count:", quiet_count)