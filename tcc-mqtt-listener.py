import paho.mqtt.client as mqtt
from signal import signal, SIGINT


# Callback on receiving a CONNACK from the server
def on_connect(client, userdata, flags, rc):
	print(f"Connected to server: {rc}")

	# Will resubscribe if the connection is lost
	# client.subscribe("$SYS/#")
	client.subscribe("/testing/things")


# Callback on receiving a PUBLISH from the server
def on_publish(client, userdata, msg):
	print(f"{msg.topic}: {msg.payload}")


def main(server_ip : str, server_port : int, keep_alive : int=60):
	mqtt_client = mqtt.Client()
	mqtt_client.on_connect = on_connect
	mqtt_client.on_message = on_publish

	def disconnect(s, f):
		print("Received SIGINT")
		mqtt_client.disconnect()

	signal(SIGINT, disconnect)

	mqtt_client.connect(server_ip, server_port, keep_alive)
	mqtt_client.loop_forever(timeout=1.0, max_packets=1, retry_first_connection=False)


if __name__ == "__main__":
	main("192.168.100.2", 1883)
