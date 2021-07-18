###### ____.BasicNetworkTerms

<br>
<!-- Table of Contents -->

### Table of Contents
- [What is a network](#what-is-a-network)
    - [Small description](#small-description)
    - [Summary of What is a network?](#summary-of-what-is-a-network)
- [Most basic type of network](#most-basic-type-of-network)
    - [NIC](#nic)
    - [MAC](#mac)
    - [Summary of basic type of network](#summary-of-basic-type-of-network)
- [Servers, Clients, Ports and Protocals](#servers-clients-ports-and-protocals)
    - [What is a server?](#what-is-a-server)
    - [What is a client?](#what-is-a-client)
    - [Network Automation & Network Programmability](#network-automation-and-network-programmability)
    - [What are Protocal & Ports?](#what-are-protocals-and-ports)
    - [Summary of Servers, Clients, Ports and Protocals](#summary-of-servers-clients-ports-and-protocals)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)

<br>
<br>
<br>
<br>

## What is a network?
### Small description
* A computer network is a digital telecommunications network for sharing resources between nodes, which are computing devices that use a common telecommunications technology.
* Data transmission between nodes is supported over data links consisting of physical cable media, such as twisted pair or fibre-optic cables, or by wireless methods, such as Wi-Fi, microwave transmission, or free-space optical communication.

### Summary of What is a network?

    The idea of a network is rather than having to physically transport a file via a usb drive, floppy or whatever other physical medium via sneakernet, we use a cable or some type of mechanism to transmit data from one device to another or from one device to many devices.

<br>

## Most basic type of network

* The biggest network we know of today is the internet. 
* Now a network doesnt have to be very big to be considered a network, it can be as simple as consisting of only 2 computers or devices as an example.

![basicNetwork](./src/basicNetwork.gif "A network between 2 computers")

* The image above displays the most basic of networks whereby it uses an unshielded twisted pair copper (UTP) cable with a RJ45 connector that connects directly into the network interface card or NIC for short. 
* You can achieve the same output with a wireless device such as wifi or bluetooth, It doesnt have to be a physical cable such as UTP or Fiber for instance.
    * The only difference being that wireless modulates a file in the air, which is then sent across through airwaves, from one device to another and the recieving device demodulates it and create the file.


### NIC
#### or Network interface card
* A Network interface card or NIC is how we connect to a physical network, or wireless.
    * Its basically a card that is either inserted into a laptop externally via a usb to rj45 convertor or computer, or its already built into the device, such as a phone or tablet.

### MAC 
#### or Media Access Control
* A network interface card, has what is known as a MAC Address or Media Access Control Address.
* On ethernet, which is the technology we generally use or wireless, devices are known by their MAC address and that is how ethernet can identify devices on a network.

### Summary of basic type of network
    
    The most basic of network can consist of only 2 devices. It can range from physical to wireless.

<br>

## Servers, Clients, Ports and Protocals
### What is a server?
* In computing, a server is a computer program or a device that provides functionality for other programs or devices, called "clients".
* This architecture is called the client–server model, and a single overall computation is distributed across multiple processes or devices for instance a website is distributed to many clients, hence a single service distributed over multiple processes or devices.

### What is a client?
* A client is a piece of computer hardware or software that accesses a service made available by a server.
* The server is often (but not always) on another computer system, in which case the client accesses the service by way of a network.
    * You dont need a server to provide a service, you can use the client machine to host a service, for example sharing a file with another pc, therefor hosting a file sharing service.

### Network Automation and Network Programmability 
### Very short description
* You basically have one program providing a service to another program typically using what is known as an API or Application Programming Interface.

### What are Protocals and Ports?
* Protocals are basically a set of rules used for communication between a set of devices, and a machine has to listen on certain port numbers for specific protocals, becaue unlike humans, computers need a very structured way of communicating which is why we use ports.
    *  As a example, a server is listening on port 80 knows the language http, your browser is already configured to talk on port 80 and therefor the server knows how to communicate with your browser based on packet based comminication.
* There various ports for different operations, as an example port 21 is for ftp or File Trasnfer Protocal, and port 22 is for ssh or secure shell.
* Overall a single server can run multiple services and provide multiple services to clients based on the protocal.

### Summary of Servers, Clients, Ports and Protocals
    
    Lets begin with the server-client model, A server provides a service to a client. 
    A single server can hold many different services or protocals for a array of clients, as an example a website hosted on a single server can be accessed by 100+ clients at the same time. 
    The server can also have a file transfering protocal or ftp server as well as other services and this is where protcals and ports come into play. 
    Protocals are just how devices communicate to each other based on what the packet being sent is from the client and on what port its being sent to as each port is a different language and unlike humans a computer cannot distinguish between language and therefor is told what to listen for on what ports. 


<br>

## Practical Demonstration Of A Network using Packet Tracer

![practicalExampleusingPacketTracer.gif](./src/practicalExampleusingPacketTracer.gif "Packet Tracer Example Of Network")

<br>

* In the gif above you see 2 end points being place on your dipology, one being a pc and another being a server.
    * These 2 devices cannot communicate with one another. We need to use either a physical cable or air.
* We then connect the 2 systems with a straight ethernet cable however we we notice that the 2 end points are red, indicating that there is no signal between the 2 devices. 
    * Therefor we need to use what is known as a crossover cable which allows to devices to speak to one another. In todays world we use what is know as MDI-X which will be discussed at a later time.
    * Here is a example of a straight ethernet cable and a crossover cable.

<br>

![ethernatCableStraightvsCrossover](./src/ethernatCableStraightvsCrossover.png "Diagram depicting how a crossopver cable works")