# Imports
import os

# Generation start
print "Starting Verilog project generation..."

project_name = raw_input("Enter your project name: ")
device_type = raw_input("Enter your target device chip: ")

print "Generating Makefile.inc..."

with open("Makefile.inc", "w") as makefile:
    makefile.write("PROJ	= " + project_name + "\n\n")
    
    makefile.write("PIN_DEF	= pins.pcf\n")
    makefile.write("DEVICE	= " + device_type + "\n\n")

    makefile.write("### Directories\n")
    makefile.write("#\n")
    makefile.write("ROOT	= $(PWD)\n")
    makefile.write("DOC		= $(ROOT)/doc\n")
    makefile.write("LOADS	= $(ROOT)/loads\n")
    makefile.write("PAR		= $(ROOT)/par\n")
    makefile.write("SIM		= $(ROOT)/sim\n")
    makefile.write("SRC		= $(ROOT)/src\n")
    makefile.write("SYN		= $(ROOT)/syn\n")

print "Done generating Makefile.inc..."

top_level_path = "./src/" + project_name + ".v"
print "Creating top-level module: " + top_level_path

with open(top_level_path, "w") as top_level:
    # Top Level generation
    top_level.write("///////////////////////////////////////////////////////////////////////////////\n")
    top_level.write("///////////////////////////////////////////////////////////////////////////////\n")
    top_level.write("///\n")
    top_level.write("/// Top-Level Verilog Module\n")
    top_level.write("///\n")
    top_level.write("///////////////////////////////////////////////////////////////////////////////\n")
    top_level.write("///////////////////////////////////////////////////////////////////////////////\n")
    top_level.write("module " + project_name + " (\n")

    port_type = raw_input("Enter your port type (input, output). Enter nothing to go to the next step: ")

    while not port_type == "":
        if port_type == "output":
            is_reg = raw_input("Is this a register (Y/N)?: ")

            if is_reg.lower() == 'y':
                port_type += " reg"

        if port_type == "input" or port_type == "output" or port_type == "output reg":
            try:
                bits = raw_input("Enter the bit size: ")
            except:
                bits = '1'

            if bits == '1' or bits == '':
                port_bits = ""
            else:
                port_bits = "[" + bits + ":0]"

            port_name = raw_input("Enter your port name: ")
            top_level.write("    " + port_type + " " + port_bits + " " + port_name)

        port_type = raw_input("Enter your port type (input, output). Enter nothing to go to the next step: ")

        if port_type == "input" or port_type == "output":
            top_level.write(",\n")
        else:
            top_level.write("\n")

    top_level.write(");\n\n")
    top_level.write("// TODO: Write code here\n\n")
    top_level.write("endmodule\n")

print "Exiting Verilog project generation..."

top_level.close()
