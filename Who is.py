#this gives python an understanding of basic networking requests
import socket

# This function performs a WHOIS lookup for a given domain name
def whois_lookup(domain: str):
    # Create a socket connection to the WHOIS server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the IANA WHOIS server on port 43
    s.connect(("whois.iana.org", 43))
    # Send the domain name to the WHOIS server
    s.send(f"{domain}\r\n".encode())
    # Receive the response from the WHOIS server
    response = s.recv(4096).decode()
    # Close the socket connection
    s.close()
    return response

# Example usage of the whois_lookup function
print (whois_lookup("google.com"))