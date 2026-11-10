# Software Defined Networking and OpenFlow Analysis

## 1. Introduction to SDN

Software Defined Networking (SDN) is a networking architecture that separates the control plane from the data plane.

- **Control plane:** Makes routing and forwarding decisions.
- **Data plane:** Forwards packets based on the rules installed by the controller.

The SDN controller manages network policies and installs flow rules in compatible switches using protocols such as OpenFlow.

## 2. OpenFlow Rules

The following flow rules are considered:

| Priority | Match Condition | Action |
|---:|---|---|
| 200 | Destination IP: 10.5.0.0/16 | Forward to port 3 |
| 100 | TCP destination port: 80 | Send to controller |
| 0 | Any unmatched packet | Drop |

Higher-priority rules are evaluated before lower-priority rules.

## 3. HTTP Traffic Analysis

Destination IP:

`10.5.1.1`

Protocol:

`TCP port 80`

The packet matches:

- Rule 1: Destination belongs to `10.5.0.0/16`.
- Rule 2: TCP destination port is 80.

Rule 1 has priority 200, which is higher than Rule 2's priority 100.

**Result:** The HTTP packet is forwarded through port 3.

## 4. SSH Traffic Analysis

Destination IP:

`10.6.1.1`

Protocol:

`TCP port 22`

The packet does not match the destination network rule or the HTTP port rule.

It therefore matches the default rule.

**Result:** The SSH packet is dropped.

## 5. Advantages of SDN

- Centralised network management.
- Programmable forwarding rules.
- Easier implementation of network policies.
- Flexible traffic management.
- Improved visibility and control.

## 6. Limitations of SDN

- Controller failure can affect network control.
- Controller security is important.
- Integration with existing infrastructure can be complex.
- Deployment and maintenance may increase costs.

Controller redundancy, access controls and secure communication channels can help reduce these risks.

## 7. Conclusion

OpenFlow allows SDN controllers to manage packet forwarding through priority-based flow rules. In the given example, HTTP traffic to `10.5.1.1` is forwarded through port 3, while SSH traffic to `10.6.1.1` is dropped by the default rule.