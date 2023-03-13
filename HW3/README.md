# COEN_241_HW
COEN 241 Homework 3
COEN 241 - HW 3
Task 1: Defining custom topologies
Questions:
1. What is the output of “nodes” and “net”
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/1.png)
2. What is the output of “h7 ifconfig”
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/2.png)
Task 2: Analyze the “of_tutorial’ controller
Questions:
1. Draw the function call graph of this controller. For example, once a packet comes to the controller, which function is the first to be called, which one is the second, and so forth?
  order:
_handle_PacketIn() -> act_like_hub() -> resend_packet() -> self.connection.send()
2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long does it take (on average) to ping for each case?
b. What is the minimum and maximum ping you have observed?
c. What is the difference, and why?

h1 ping -c100 h2: Average is 3.113, minimum is 1.535, and maximum is 99.734
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/3.png)

h1 ping -c100 h8: Average is 9.616, minimum is 5.521, and maximum is 86.367
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/4.png)

I found the difference between these two cases that is the average time of the first case is less than the second case. I believe the reason for this is because h1 connects with h2 only by switch s2. However, if h1 wants to ping h8, it will go through s3, s2, s1, s5, and s7. So, the second case should take more time than the first case. 

3. Run “iperf h1 h2” and “iperf h1 h8”
a. What is “iperf” used for?
Iperf is a tool for network performance measurement and tuning. It is a cross-platform tool that can produce standardized performance measurements for any network. Iperf has client and server functionality and can create data streams to measure the throughput between the two ends in one or both directions.
b. What is the throughput for each case?
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/5.png)

c. What is the difference, and explain the reasons for the difference.
The throughput of the first case is more than the second case, I think it’s because of the same reason as the previous question, h1 pings to h8 has to go through more switches, so it will cause more packets to be dropped.
4. Which of the switches observes traffic? Please describe your way of observing such traffic on switches (e.g., adding some functions in the “of_tutorial” controller).
All switches observe traffic since the act_like_hub() function sends packets to all the switches in the network. For observing the traffic on switches, we can add a log statement in the _handle_packetln() to keep track of each packet.

Task 3: MAC Learning Controller
Questions:
1. Describe how the above code works, such as how the "MAC to Port" map is established. You could use a ‘ping’ example to describe the establishment process (e.g., h1 ping h2).
The code above shows two major parts. First, it will check if the source MAC address is in the “MAC to Port” map, if it’s a new source MAC, it will store the source MAC and the corresponding port as key-value pair in to the “MAC to Port” map, the process is learning the port for the source MAC. And then it will check if the destination is known, if so, it will only send the packet to the target port. Otherwise, it will also send the packet to all the ports.
For example, if we do “h1 ping h2”, if the h1 is unknown, it will learn the h1’s port from the packet, and then check if the h2 is known, if so, it can send the packet to h2 directly, otherwise, it will send the packet to all ports.

2. (Comment out all prints before doing this experiment) Have h1 ping h2, and h1 ping
h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long did it take (on average) to ping for each case?
b. What is the minimum and maximum ping you have observed?

h1 ping -c100 h2: Average is 2.184 ms, minimum is 1.288, and maximum is 8.131
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/6.png)

h1 ping -c100 h8: Average is 8.424 ms, minimum is 5.031, and maximum is 37.239
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/7.png)
c. Any difference from Task 2 and why do you think there is a change if there is?
As we can see, Task 3 costs less time than Task 2 for both cases(h1 ping h2 and h1 ping h8). I think the reason for this is because of the act_like_switch(). If the destination MAC address is found on the map, the switch will only resend the packet to the port that is mapped to in the “MAC to Port” mapping.
3. Q.3 Run “iperf h1 h2” and “iperf h1 h8”.
a. What is the throughput for each case?
![image](https://github.com/IsabellaLin325/COEN_241_HW/blob/main/HW3/screenshots/8.png)

b. What is the difference from Task 2 and why do you think there is a change if
there is?
	The throughput of Task 3 is greater than Task 2. I think it’s because of less network congestion. If “MAC to Port” map has learned all the ports, it can discard the flooding of packets which can improve the performance.
	

