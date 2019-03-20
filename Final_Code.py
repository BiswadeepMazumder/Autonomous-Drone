from dronekit import connect, VehicleMode
import dronekit_sitl
import time
import socket,exceptions
import argparse


#if connection string is not entered by the user then
def connecting_to_vehicle():

	#parser to get the connection string

	parser = argparse.ArgumentParser(description='By default SITL connects to local PC')
	parser.add_argument('--connection_id', help='connection string for the drone')
	args = parser.parse_args()

	connection_string = args.connection_id
	sitl = None

	if not connection_string:
		sitl=dronekit_sitl.start_default()
		connection_string= sitl.connection_string()

		#if connection string is present then connect to that specific vehicle with hte ip/udp address

	print "Connecting to vehicle on %s" %connection_string
	try:
		vehicle=connect(connection_string, wait_ready=True)	except  socket.error:
		print "No Vehicle in that address"
	except exceptions.OSError as e:
		print "No Serial Exists"
	except dronekit.APIException:
		print "Timeout. It took too long"
	except:
		print "Some other Error"

		return vehicle

vehicle=connecting_to_vehicle()



def arm_takeoff_vehicle(Altitude):
	print "Pre ARM Checking"

	#wait for the vehicle to get ready before Arming.
	while not vehicle.is_armable:
		print "Vehicle still not initialized. Please wait"
		time.sleep(2)


	print "Arming the Vehicle"
	#Vehicle should be in guided mode before TAKE-OFF
	vehicle.mode=VehicleMode("GUIDED")
	vehicle.armed=True 

	#take off function allows the vehicle to take to that certain altitude
	vehicle.simple_takeoff(Altitude)

	#Restrict any other commands to the vehicle until it reaches the certain height

	while True:
		print "Altitude: %s" %vehicle.location.global_relative_frame.alt:
		# if the below condition doesn't comply with the practical scenarios, then multiply Altitude with 0.95
		if vehicle.location.global_relative_frame.alt > Altitude
			print "Altitude Reached"
			break
		time.sleep(5)

#from one point to another and lands there
def vehicle_goto_location(land):
	arm_takeoff_vehicle(10)

	#LocationGlobalRealative(latitude,longitude,altitude)
	targetPoint1=LocationGlobalRelative(-35.361354,149.165218,20)

	#setting airspeed attribute to 3 to move to that particular point
	vehicle.airspeed = 3

	vehicle.simple_goto(targetPoint1)

	time.sleep(30) #sleep funtion prevents other meaages to interfere the ongoing function and also in battery saving

	# Now to land the drone in that particular location
	if land is True:
		while True:
			print "Landing.."
			if vehicle.location.global_relative_frame.alt < 0.12: #if height from ground to drone becomes less than 12 cm
				vehicle.isarmed = False	
				print "Succesfully Landed and disarmed motors"
				break
	time.sleep(3)

print "Stop Vehicle"
#CLOSE vehicle object
vehicle.close()

#Drone goes hrough multiple points
def vehicle_goto_multiple_points()



def main:
	vehicle=connecting_to_vehicle()
	arm_takeoff_vehicle(input("Enter the altitude:"))


