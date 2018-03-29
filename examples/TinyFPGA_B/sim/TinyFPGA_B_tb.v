`timescale 1ns/1ps

module TinyFPGA_B_tb;
   // Inputs
   reg pin3_clk_16mhz = 0;
   reg pin4_reset     = 0;

   // Outputs
   wire pin1_usb_dp, pin2_usb_dn, pin13;

   // DUT definition
   TinyFPGA_B U0 (
		  .pin1_usb_dp    (pin1_usb_dp),
		  .pin2_usb_dn    (pin2_usb_dn),
		  .pin3_clk_16mhz (pin3_clk_16mhz),
		  .pin4_reset     (pin4_reset),
		  .pin13          (pin13)
		  );
   
   // Add stimulus here
   initial begin
      $dumpfile("TinyFPGA_B.vcd");
      $dumpvars(0, U0);

      // Resets the counter initially
      #5 pin4_reset     = 1;
      #5 pin4_reset     = 0;

      // Allows the counter to run for 100 ns before stopping
      #100; $finish;
   end

   // Add clock stimulus here
   always #1 pin3_clk_16mhz = !pin3_clk_16mhz;

   // Monitor statements for VVP file and output
   initial begin
      $monitor("Clock: %b", pin3_clk_16mhz);
   end
   
endmodule
   
