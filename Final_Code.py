from dronekit import connect, VehicleMode
import dronekit_sitl
import time
import socket,exceptions
import argparse

'''
parser = argparse.ArgumentParser(description='By default SITL connects to local PC')
parser.add_argument('--connection_id', help='connection string for the drone')
args = parser.parse_args()

connection_string = args.connection_id
sitl = None
'''

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
	vehicle.mode=VehicleMode(GUIDED)
	vehicle.armed=True 

	#take off function allows the vehicle to take to that certain altitude
	vehicle.simple_takeoff(Altitude)

	#Restrict any other commands to the vehicle until it reaches the certain height

	while True:
		print "Altitude: %s" %vehicle.location.global_relative_frame.alt
		# if the below condition doesn't comply with the practical scenarios, then multiply Altitude with 0.95
		if vehicle.location.global_relative_frame.alt > Altitude
			print "Altitude Reached"
			break
		time.sleep(2)


def main:
	vehicle=connecting_to_vehicle()
	arm_takeoff_vehicle(100)


