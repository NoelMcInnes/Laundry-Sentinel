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

### Next Step
Add memory to the state detection logic so that multiple readings are considered before the appliance changes state.