#Imports
import os
import sys

# Generation start
print "Starting testbench generation..."

top_level_name = raw_input("Enter your top-level name: ")
print "Opening DUT file..."

# File Paths
top_level_path = "./src/" + top_level_name + ".v"
testbench_path = "./sim/" + top_level_name + "_tb.v"

inputs = []
outputs = []

try:
    with open(top_level_path, "r") as top_level:
        print "Scanning DUT properties..."

        # Parse top-level module for ports
        for line in top_level:
            temp = line.replace(',', ' ').split()
            print temp

            if len(temp) > 0:
                if temp[0] == 'input':
                    if ':' in temp[1]:
                        inputs.append(('input', temp[2], int(temp[1][1])))
                    else:
                        inputs.append(('input', temp[1], 1))
                elif temp[0] == 'output':
                    if temp[1] == 'reg':
                        if ':' in temp[2]:
                            outputs.append(('output', temp[3], int(temp[2][1])))
                        else:
                            outputs.append(('output', temp[2], 1))
                    elif ':' in temp[1]:
                        outputs.append(('output', temp[2], int(temp[1][1])))
                    else:
                        outputs.append(('output', temp[1], 1))

        # Write testbench file
        with open(testbench_path, "w") as testbench:
            print "Generating testbench..."

            testbench.write("`timescale 1ns/1ps\n\n")
            testbench.write("module " + top_level_name + "_tb;\n")

            # Create inputs
            testbench.write("    //Inputs\n")
            
            for input_port in inputs:
                if input_port[2] == 1:
                    testbench.write("    reg " + input_port[1] + " = 0;\n")
                else:
                    testbench.write("    reg " + "[" + str(input_port[2]) + ":0] " + input_port[1] + " = 0;\n")

            testbench.write("\n")
                        
            # Create outputs
            testbench.write("    //Outputs\n")
            
            for output_port in outputs:
                if output_port[2] == 1:
                    testbench.write("    wire " + output_port[1] + " = 0;\n")
                else:
                    testbench.write("    wire " + "[" + str(output_port[2]) + ":0] " + output_port[1] + " = 0;\n")

            testbench.write("\n")
                        
            # Create DUT
            testbench.write("    //DUT definition\n")
            testbench.write("    " + top_level_name + " U0 (\n")

            # Create inputs for DUT
            for input_port in inputs:
                testbench.write("        ." + input_port[1] + " (" + input_port[1] +"),\n")

            i = 0
                
            # Create outputs for DUT
            for output_port in outputs:
                testbench.write("        ." + output_port[1] + " (" + output_port[1] + ")")
                i += 1

                if not i == len(outputs):
                    testbench.write(",")

                testbench.write("\n")

            testbench.write("        );\n\n")

            # Create main procedure
            testbench.write("    // Add stimulus here\n")
            testbench.write("    initial begin\n")
            testbench.write("        $dumpfile(\"" + top_level_name + ".vcd\");\n")
            testbench.write("        $dumpvars(0, U0);\n\n")
            
            testbench.write("        // TODO: Write stimulus\n\n")
            
            testbench.write("        #100; $finish;\n")
            testbench.write("    end\n\n")

            testbench.write("endmodule\n")

            print "Done..."

except IOError:
    print "Error opening file... make sure a DUT module exists!"
    sys.exit()
