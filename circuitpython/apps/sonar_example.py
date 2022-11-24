# sonar example 2022-02-21
import board, busio, time, math, digitalio, adafruit_hcsr04
from ssis_rvr   import pin
from sphero_rvr import RVRDrive

rvr   = RVRDrive(uart = busio.UART(pin.TX, pin.RX, baudrate=115200))
sonar = adafruit_hcsr04.HCSR04(trigger_pin=pin.TRIGGER, echo_pin=pin.ECHO)

time.sleep(0.5)

rvr.set_all_leds(255,0,0) #set leds to red
time.sleep(0.1)
rvr.set_all_leds(0,255,0) #set leds to green
time.sleep(0.1)
rvr.set_all_leds(0,0,255) #set leds to blue
time.sleep(0.1) #turn off
rvr.set_all_leds(255,255,255) #turn off leds or make them all black



print("starting up")

rvr.sensor_start()

print("sensor_start")

setpoint = 32
k = 5
MAX_SPEED = 100

sensor_distance = sonar.distance
print(sensor_distance)
error = 100
start_time = time.monotonic()
elapsed_time = time.monotonic() - start_time
rvr.update_sensors()

while(elapsed_time < 5.0):
    time.sleep(0.2)
    elapsed_time = time.monotonic() - start_time
    try:
        sensor_distance = sonar.distance
        # Add your proportional control code here.
        error = sensor_distance - setpoint
        output = k*error
        if(output > MAX_SPEED):
            output = MAX_SPEED
        elif(output < -MAX_SPEED):
            output = -MAX_SPEED

        rvr.setMotors(output, output)
        rvr.stop
        #set the power of the motors for both the left and right track
            # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
            # Use this command in the next line to send the output of your proportional
            # control to both the left and right motors.


    except RuntimeError:
        print("Retrying!")
        pass

rvr.drive(70,90)
rvr.stop
