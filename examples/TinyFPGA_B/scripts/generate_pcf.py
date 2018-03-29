#Imports
import os
import sys

# Generation start
print "Starting PCF generation..."

project_name = raw_input("Enter your project name: ")
print "Opening top-level module..."

# File Paths
top_level_path = "./src/" + project_name + ".v"
pcf_path = "./par/pins.pcf"

ports = []

try:
    with open(top_level_path, "r") as top_level:
        print "Scanning for ports"

        # Parse top-level module for ports
        for line in top_level:
            temp = line.replace(',', ' ').split()

            if len(temp) > 0:
                if temp[0] == 'input':
                    if ':' in temp[1]:
                        ports.append((temp[2], int(temp[1][1])))
                    else:
                        ports.append((temp[1], 1))
                elif temp[0] == 'output':
                    if temp[1] == 'reg':
                        if ':' in temp[2]:
                            ports.append((temp[3], int(temp[2][1])))
                        else:
                            ports.append((temp[2], 1))
                    elif ':' in temp[1]:
                        ports.append((temp[2], int(temp[1][1])))
                    else:
                        ports.append((temp[1], 1))

        # Write pcf file
        with open(pcf_path, "w") as pcf:
            for port in ports:
                for i in range(0, port[1]):
                    if port[1] == 1:
                        pin = raw_input("Enter pin name for " + port[0] + ": ")
                        pcf.write("set_io --warn-no-port " + port[0] + " " + pin + "\n")
                    else:
                        pin = raw_input("Enter pin name for " + port[0] + "[" + str(i) + "]: ")
                        pcf.write("set_io --warn-no-port " + port[0] + "[" + str(i) + "] " + pin + "\n")

except IOError:
    print "Error opening file... make sure a top-level module exists!"
    sys.exit()
