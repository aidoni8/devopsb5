# Company wants to increase their server according to their CPU usage. 
# Create a python program that gets average cpu usage as an input 
# and prints True if we need to launch more servers for our application.
# When average cpu usage is between 40 and 70 inclusive
# we should launch a new server.

avg_cpu_utilization = int(input("Enter the avg.cpu utilization please:"))

# Print true when vg_cpu_utilization is in between 40 and 70 inclusive

should_launch = 70 >= avg_cpu_utilization >= 40

print(should_launch)