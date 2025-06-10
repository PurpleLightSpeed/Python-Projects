#import statement in python is used to import modules or libraries that provide additional functionality.
#Used python3 -m pip install python-nmap in terminal to install the nmap library
import nmap

#Create an instance of the nmap.PortScanner class, and assign it to the variable nm to use later
nm = nmap.PortScanner()

#http://scanme.nmap.org/ IP Address
target = "45.33.32.156"

#options is how we want to use nmap on the target IP address or hostname
#-sV is used to detect service versions, -sC is used to run default scripts, and scan_results is the output file
options = "-sV -sC scan_results"

#This is calling the scan method of the nmap.PortScanner instance (nm) to perform a scan on the target with the specified options
nm.scan(target, arguments=options)

#This is a nested loop structure that iterates throught the results of the nmap scan
#And then print information on the host protocols, ports etc.

#This is the outer loop is going to iterate through all the hosts retured by the nmap scan
for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    #This is the inner loop that iterates through all the protocols for each host
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port in port_info.items():
            state = nm[host].state()  #Added this line to get the state of the port
            print("Port: %s\tState %s" % (port, state))


