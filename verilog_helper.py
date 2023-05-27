file_path = "instruction_hex.txt"
with open(file_path) as f:
    codes = f.readlines()
    codes = list(map(lambda s: s.strip(), codes))
    
    
    
with open('verilog_project.txt','w',encoding='UTF-8') as f:
    i=0
    for code in codes:
        f.write("Inst_mem["+str(i)+"] = 32'h"+code.replace('0x','')+";"+'\n')
        i+=1
