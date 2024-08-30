module alu (
  input  logic [3:0] A,
  input  logic [3:0] B,
  input  logic [1:0] Sel,
  output logic [7:0] F
);

  always_comb begin
    case (Sel)
      2'b00:	F = A + B;						// Addition
      2'b01:	F = A - B;  					// Subtraction
      2'b10:	F = A * B;  					// Multiplication
      2'b11:	F = (B != 0) ? A / B : 8'b0;    // Division with zero-check
      default:	F = 8'b0; 					    // Default value
    endcase
  end

endmodule
