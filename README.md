# MIPS_assembler_with_Python
Python code that change assembly code to OP code.
###### 컴퓨터 구조 실습도중 어셈블리 코드를 op 코드로 손으로 바꿔야 하는 task가 있었고 사람들이 편하게 바꾸도록 파이썬 코드로 짰습니다.
--------------------------------------------------
### input assembly.txt
### output instruction_hex.txt, instruction_bin.txt &rarr; 각각 16진수, 2진수 .txt
--------------------------------------------------
## Available Assembly code

- R-type: add, sub
  * add   $a $b $c    &rarr;  000000 b_5bit c_5bit a_5bit 00000 100000
  * sub   $a $b $c    &rarr;  000000 b_5bit c_5bit a_5bit 00000 100010

- I-type : addi, lw, sw, beq
  * addi  $a $b #c    &rarr;  001000 b_5bit a_5bit c_16bit
  * lw    $a b($c)    &rarr;  100011 c_5bit a_5bit b_16bit
  * sw    $a b($c)    &rarr;  101011 c_5bit a_5bit b_16bit
  * beq   $a $b #c    &rarr;  000100 a_5bit b_5bit (c-PC+4)/4_16bit
  
 - No operation : nop (위 instruction이 없으면 nop으로 간주)
 
 - ###### J-type은 아직 안 넣음
