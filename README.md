# tcc-mqtt-testing
Project for basic testing of the MQTT protocol for data transmission

---

## Results

Tests were done by monitoring port 1883 using Wireshark and checking the number of bytes sent.  
The Mosquitto broker was installed on a Raspberry Pi on the same network.  
All 3 QoS levels were tested. The results for how many bytes were in the message and how many were transmitted
are in the table below. All sizes are in bytes.

| Message Size | Size QoS 0 | Size QoS 1 | Size QoS 2 |
|:---:|:---:|:---:|:---:|
| 0   | 133 | 133 | 133 |
| 1   | 134 | 190 | 308 |
| 10  | 143 | 199 | 317 |
| 100 | 233 | 289 | 407 |
