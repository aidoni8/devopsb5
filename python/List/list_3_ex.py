# Given a list of server IP addresses, 
# write a Python program to create a new list 
# that contains only those IPs which are in the 
# subnet '192.168.x.x'. Assume the original list is
# of the format ['192.168.1.1', '10.0.0.1', '172.16.0.1', '192.168.0.25'].
#If the IP address starts with 192.168 it means it is subnet of 192.168.x.x
# If the main network contains smaller networks that depends on the main one, 
#small networks are called subnets. 


ip_addresses = ['192.168.1.1', '10.0.0.1', '172.16.0.1', '192.168.0.25']

subnet_192_168 = []

for ip in ip_addresses:
    if ip .startswith("192.168"):
        subnet_192_168.append(ip)
print(f"The subnets of network 192.168 is {subnet_192_168}")



