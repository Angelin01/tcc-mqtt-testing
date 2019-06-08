import paho.mqtt.client as mqtt
from os import urandom
from signal import signal, SIGINT
from time import sleep


# Callback on receiving a CONNACK from the server
def on_connect(client, userdata, flags, rc):
	print(f"Connected to server: {rc}\n")

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

	qos_level = None
	while qos_level is None:
		qos_in = input("Input the QoS level for the messages\n0 - Fire and Forget\n1 - Retry until ACK received\n2 - Exactly one copy received\n")
		if qos_in.isdigit() and 0 <= int(qos_in) <= 2:
			qos_level = int(qos_in)
		else:
			print("Invalid QoS")

	while True:
		bytes_to_send = input("Input the number of bytes to publish\n")

		if bytes_to_send.isdigit():
			bytes_to_send = int(bytes_to_send)
			if bytes_to_send > 0:
				print(f"Sending {bytes_to_send} random bytes 100 times")
				for _ in range(100):
					mqtt_client.publish("/testing/things", payload=urandom(bytes_to_send), qos=qos_level)
					sleep(0.1)
			elif bytes_to_send == 0:
				print("Sending empty message")
				mqtt_client.publish("/testing/things", qos=qos_level)
			else:
				print("Number of bytes must not be negative")
		else:
			print("Invalid number")



if __name__ == "__main__":
	main("192.168.100.2", 1883, 6000)
