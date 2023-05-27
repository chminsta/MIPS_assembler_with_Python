# MIPS_assembler_with_Python
Python code that change assembly code to OP code.
###### 컴퓨터 구조 실습도중 어셈블리 코드를 op 코드로 손으로 바꿔야 하는 task가 있었고 사람들이 편하게 바꾸도록 파이썬 코드로 짰습니다.
--------------------------------------------------
### input:  assembly.txt
### output: instruction_hex.txt, instruction_bin.txt &rarr; 각각 16진수, 2진수 .txt
--------------------------------------------------
### 주의 
### 1. , 넣지말것
### 2. 각 줄앞에 tab 하지 말것 (고칠 수 있으나 굳이 귀찮음) 
### 3. 각 instruction 뒤에 주석 써도 됨! 기호 안써도 됨. 아래와 같은 형식으로 써도 잘 돌아감
* add $1 $1 $2 1에 2랑 1 더한거 넣기
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
