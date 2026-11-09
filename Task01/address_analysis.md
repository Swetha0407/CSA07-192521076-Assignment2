# IPv4 Address Calculations

## 1. Admission PC – 172.16.45.200/20

Subnet mask: 255.255.240.0

Block size in the third octet:

256 - 240 = 16

The third-octet range containing 45 is 32–47.

- Network address: 172.16.32.0
- Broadcast address: 172.16.47.255
- First usable host: 172.16.32.1
- Last usable host: 172.16.47.254
- Given address: 172.16.45.200
- Status: Valid host address

## 2. Lab Printer – 10.0.15.255/21

Subnet mask: 255.255.248.0

Block size in the third octet:

256 - 248 = 8

The third-octet range containing 15 is 8–15.

- Network address: 10.0.8.0
- Broadcast address: 10.0.15.255
- First usable host: 10.0.8.1
- Last usable host: 10.0.15.254
- Given address: 10.0.15.255
- Status: Invalid – broadcast address

## 3. X-ray Server – 192.168.4.0/23

Subnet mask: 255.255.254.0

Block size in the third octet:

256 - 254 = 2

The third-octet range containing 4 is 4–5.

- Network address: 192.168.4.0
- Broadcast address: 192.168.5.255
- First usable host: 192.168.4.1
- Last usable host: 192.168.5.254
- Given address: 192.168.4.0
- Status: Invalid – network address

## 4. Clinic Router – 203.0.113.10/29

Subnet mask: 255.255.255.248

Block size in the fourth octet:

256 - 248 = 8

The fourth-octet range containing 10 is 8–15.

- Network address: 203.0.113.8
- Broadcast address: 203.0.113.15
- First usable host: 203.0.113.9
- Last usable host: 203.0.113.14
- Given address: 203.0.113.10
- Status: Valid host address

## Conclusion

The lab printer and X-ray server have invalid host addresses because they use the broadcast and network addresses respectively. The Admission PC and clinic router have valid host addresses within their subnets.