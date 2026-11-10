# IPv4 Multicast Addressing

## 1. Introduction

Multicast is a communication method in which one sender transmits data to a group of receivers.

Unlike unicast, which sends a separate copy to each destination, multicast allows multiple receivers to receive the same transmission through a multicast group.

## 2. Given Multicast Address

IPv4 multicast group:

`239.1.2.3`

IPv4 multicast addresses belong to the range `224.0.0.0` to `239.255.255.255`.

## 3. Multicast MAC Address Calculation

The Ethernet multicast MAC address is formed using the prefix:

`01:00:5E`

The lower 23 bits of the IPv4 multicast address are mapped into the final three MAC address bytes.

Given IPv4 address:

`239.1.2.3`

The lower 23 bits correspond to:

`01:02:03`

Therefore:

**Multicast MAC address:**

`01:00:5E:01:02:03`

## 4. Multicast for Camera Streaming

Consider a surveillance system where multiple control rooms need to receive the same camera stream.

### Unicast

The camera sends a separate copy of the video stream to every control room.

If there are multiple receivers, the camera and network must handle multiple copies of the same data.

### Multicast

The camera sends one stream to a multicast group. Interested receivers join that group and receive the stream.

Multicast reduces unnecessary duplicate traffic from the sender and can improve bandwidth efficiency.

IGMP snooping helps switches forward multicast traffic only to ports with interested receivers. Multicast routing protocols such as PIM can support delivery across different IP networks.

## 5. Advantages

- Efficient one-to-many communication.
- Reduces duplicate traffic from the sender.
- Useful for live video, audio and streaming applications.
- Can reduce bandwidth usage when many receivers need the same content.

## 6. Conclusion

Multicast enables efficient communication with multiple receivers. For the given group `239.1.2.3`, the corresponding Ethernet multicast MAC address is `01:00:5E:01:02:03`. It is useful for applications such as surveillance video streaming.