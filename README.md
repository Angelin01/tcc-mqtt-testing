# tcc-mqtt-testing
Project for basic testing of the MQTT protocol for data transmission

---

## Results

Tests were done by monitoring port 1883 using Wireshark and checking the number of bytes sent.  
The Mosquitto broker was installed on a Raspberry Pi on the same network.  
All 3 QoS levels were tested. The results for how many bytes were in the message and how many were transmitted between
the broker and client are in the table below. All sizes are in bytes.

| Message Size | Size QoS 0 | Size QoS 1 | Size QoS 2 |
|:---:|:---:|:---:|:---:|
| 0     | 133   | 133   | 133   |
| 1     | 134   | 190   | 308   |
| 10    | 143   | 199   | 317   |
| 100   | 233   | 289   | 407   |
| 1000  | 1134  | 1190  | 1308  |
| 10000 | 10314 | 10370 | 10488 |

Apparently, empty messages will always send out a minimum of 133 (do note this includes the name of the topic,
which can vary and adds overhead).  
With QoS 0, the increase in bytes sent is exactly the size of the message sent.  
With QoS 1, there was an increase in how many bytes were transmitted due to the necessity of the ACK from the broker.  
With QoS 2, there was a large increase due to the necessary handshake between broker and client.

It should be noted that with QoS 1 and 2 additional bytes would be transmitted in case of failure in transmission.

## Conclusion

The TCP stack adds quite a bit of overhead. QoS 0 should be discarded due to it's fire and forget nature.  
QoS 1 should be considered if the message sizes are small and retransmission is not costly.  
QoS 2 should be considered only if message sizes are going to be very big and retransmission is a problem.

