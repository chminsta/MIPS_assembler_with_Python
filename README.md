# MIPS_assembler_with_Python
Python code that change assembly code to OP code.
###### 컴퓨터 구조 실습도중 어셈블리 코드를 op 코드로 손으로 바꿔야 하는 task가 있었고 사람들이 편하게 바꾸도록 파이썬 코드로 짰습니다.
--------------------------------------------------
### input:  assembly.txt
### output: instruction_hex.txt, instruction_bin.txt &rarr; 각각 16진수, 2진수 .txt
--------------------------------------------------
### Comments: comments after each instruction, no symbols required. The following format works well
* add $1 $1 $2 comments is ok! damn bro whats up
##### + You can write ',' and tab in start of line, python will remove that and assemble it
---------------------------------------------------
## Available Assembly code
- Branch Address
  * (branch address): (instruction), such as
    *  LOOP1: add $1 $1 $2 
- R-type: add, sub, and, or

  * add   $a $b $c    &rarr;  000000 b_5bit c_5bit a_5bit 00000 100000
  * sub   $a $b $c    &rarr;  000000 b_5bit c_5bit a_5bit 00000 100010
  * and   $a $b $c    &rarr;  000000 b_5bit c_5bit a_5bit 00000 100100
  * or    $a $b $c    &rarr;  000000 b_5bit c_5bit a_5bit 00000 100101

- I-type : addi, lw, sw, beq

  * addi  $a $b #c    &rarr;  001000 b_5bit a_5bit c_16bit
  * lw    $a b($c)    &rarr;  100011 c_5bit a_5bit b_16bit
  * sw    $a b($c)    &rarr;  101011 c_5bit a_5bit b_16bit
  * beq   $a $b LOOP1    &rarr;  000100 a_5bit b_5bit (LOOP1 address-(PC+4))/4_16bit

 - No operation : nop (위 instruction이 없으면 nop으로 간주)
 
 - ###### J-type은 아직 안 넣음


--------------------------------------------------------------------------
# HOW to use?
1. make assembly code in assembly_code.txt
2. run assembly_to_opcode.py
3. output will have binary and hex op codes.
4. if run verilog_helper.py, it will make a verilog_code.txt that define. For example,

```c#
Inst_mem[0] = 32'h8c410004;
Inst_mem[1] = 32'h0;
Inst_mem[2] = 32'h0;
Inst_mem[3] = 32'h0;
Inst_mem[4] = 32'h222020;
Inst_mem[5] = 32'h0;
Inst_mem[6] = 32'h0;
Inst_mem[7] = 32'h0;
Inst_mem[8] = 32'h294025;
Inst_mem[9] = 32'h0;
Inst_mem[10] = 32'h0;
Inst_mem[11] = 32'h0;
Inst_mem[12] = 32'h110afffc;
Inst_mem[13] = 32'h0;
Inst_mem[14] = 32'h0;
Inst_mem[15] = 32'h0;

```

# GOOD LUCK on your VERILOG!!
