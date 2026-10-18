import random
import time

print("Laundry Sentinel - Automatic Simulator")

cycle_count = 0

while True:
    cycle_count += 1
    if cycle_count > 10:
        cycle_count = 1
    print("Cycle count:", cycle_count)
    if cycle_count <= 5:
        vibration = random.uniform(0.0, 0.2)
    else:
        vibration = random.uniform(0.7, 1.0)
    print("Vibration:", vibration)
    time.sleep(1)