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
		dronekit.connect('connection_string', heartbeat_timeout=15)
	except  socket.error:
		print "No Vehicle in that address"
	except exceptions.OSError as e:
		print "No Serial Exists"
	except dronekit.APIException:
		print "Timeout. It took too long"
	except:
		print "Some other Error"
	finally:
		vehicle=connect(connection_string, wait_ready=True)

		return vehicle

vehicle=connecting_to_vehicle()