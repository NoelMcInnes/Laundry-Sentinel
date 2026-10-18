# Development Log

## Prototype 1 - Software Simulator

### Goal
Build a simple Python simulator to test appliance state detection before connecting real hardware.

### Current Features

- Accepts simulated vibration readings from the user.
- Uses a configurable vibration threshold
- Classifies the appliance 'IDLE' or 'RUNNING'.
- Continuously accepts new readings using a loop.

### Current Limitations

A single vibration reading can immediately change the appliance state.  Real appliances may breifly become quiet during a cycle, so one low reading could incorrectly freport that the appliance has stopped.


### Progress Update - State Detection

- Added separate counters for active and quiet readings.
- Requires three consecutive active readings to enter RUNNING.
- Requires three consecutive quiet readings to enter IDLE.
- Resets counters when an opposite reading interrupts a streak.
- Successfully tested interrupted vibration and quiet sequences.


### Progress Update - Diagnostic Logging

- Added labels to vibration readings.
- Added current state reporting after every reading.
- Added active and quiet counter reporting.
- Added separate STATE CHANGE messages.
- Tested both state transitions and verified counter behavior.

## Progress Update - Automatic Sensor Simulation

- Created auto_simulator.py.
- Added random vibration generation.
- Added automatic readings with a one-second delay.
- Simulated IDLE and RUNNING vibration ranges.
- Added a repeating 10-reading test cycle.
- Verified transitions between simulated conditions.

Next: Connect automatic readings to the state detector.