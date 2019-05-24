import paho.mqtt.client as mqtt
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
		to_send = input("Input something to publish")
		mqtt_client.publish("/testing/things", payload=to_send, qos=0)


if __name__ == "__main__":
	main("127.0.0.1", 1883)