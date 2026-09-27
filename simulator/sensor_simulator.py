print("Laundry Sentinel Simulator")

threshold = 0.50

while True:
    vibration = float(input("Enter vibration level: "))
    print(vibration)

    if vibration > threshold:
        print("RUNNING")

    else:
     print("IDLE")
       
