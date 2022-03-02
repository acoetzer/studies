###### ____.NetworkingBasics

<!-- Table of contents -->

- [IP Addressing](#ip-addressing)
  - [Network interfaces and what they mean](#network-interfaces-and-what-they-mean)
  - [Correlation between Linux and Windows](#correlation-between-linux-and-windows)


## **IP Addressing**
* First off to view your ip address in linux open the terminal and use the command **_ifconfig_**

<br>

### **Network interfaces and what they mean**

<br>

```
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::a00:27ff:fecb:2a0e  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:cb:2a:0e  txqueuelen 1000  (Ethernet)
        RX packets 135502  bytes 190950393 (182.1 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 28973  bytes 2503282 (2.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### **eth0:**
* You can see the **_eth0:_** is our physical network interface and it holds our ip address.

<br>
<br>

```
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 84  bytes 4960 (4.8 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 84  bytes 4960 (4.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### **lo:**
* Just below you see your second internface known as lo: or loopback the loopback address is just a special virtual network interface the device uses to communicate with itself. The is mainly for diagnostic and troubleshooting purposes and in some special cases can be used to communicate with some type of servers that could be running on the local machine.

<br>

### **Correlation between Linux and Windows**

<br>

|Linux|Windows|Info|
|:--|:--|:--|
|**inet**|**ipv4**| - Is in dotted decimal format|
|**inet6**|**ipv6**|Is in hexa Decimal format|
|**netmask**|**subnet mask**||
|**ether**|**Mac Address**||

<br>

### ****
