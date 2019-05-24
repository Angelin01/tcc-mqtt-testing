import paho.mqtt.client as mqtt
from os import urandom
from signal import signal, SIGINT


# Callback on receiving a CONNACK from the server
def on_connect(client, userdata, flags, rc):
	print(f"Connected to server: {rc}")

	# Will resubscribe if the connection is lost
	# client.subscribe("$SYS/#")


def main(server_ip : str, server_port : int, keep_alive: int=60):
	mqtt_client = mqtt.Client()
	mqtt_client.on_connect = on_connect

	def disconnect(s, f):
		mqtt_client.loop_stop()

	signal(SIGINT, disconnect)

	mqtt_client.connect(server_ip, server_port, keep_alive)
	mqtt_client.loop_start()

	while True:
		bytes_to_send = input("Input the number of bytes to publish\n")

		if bytes_to_send.isdigit():
			bytes_to_send = int(bytes_to_send)
			if bytes_to_send > 0:
				print(f"Sending {bytes_to_send} random bytes")
				mqtt_client.publish("/testing/things", payload=urandom(bytes_to_send), qos=0)
			elif bytes_to_send == 0:
				print("Sending empty message")
				mqtt_client.publish("/testing/things")
			else:
				print("Number of bytes must not be negative")
		else:
			print("Invalid number")



if __name__ == "__main__":
	main("192.168.100.2", 1883)
