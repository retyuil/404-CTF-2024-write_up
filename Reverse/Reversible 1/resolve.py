
with open('dump1.txt','r') as f:
    dump = f.read()


lines = dump.split('\n')

instruction = ''
target = ''


start = False
for line in lines:
    if '1275' in line:
        start = True
    if 'mov    -0x4(%rbp),%eax' in line:
        start = False
    if start:
        instruction += line + '\n' 

    if 'movabs' in line:
        line = (line.split('$'))[1]
        line = (line.split(','))[0]
        target += line[2:]




def MOVZX(src):
    return src

def MOV(src, dest):
    return src

def SAR(src, shift):
    return (src >> shift) & 0xff

def AND(src, mask):
    return src & mask

def SHL(src, shift):
    return (src << shift) & 0xff

def XOR(src1, src2):
    return src1 ^ src2 

def SHR(src, shift):
    return (src >> shift) & 0xff

def ADD(src1, src2):
    return (src1 + src2) & 0xff

def parse_assembly_instructions(instructions):
    python_code = ''
    for line in instructions.split('\n'):
        line = (line.split(' '))
        try:

            line = line[11:]
            operand1 = line[-1].split(',')[0]
            operand2 = line[-1].split(',')[1]
            line2 = []
            for element in ((line)):
                if element != "":
                    line2.append(element)
            opcode = line2[-2]
            operand1 = operand1.replace('%',"")
            operand2 = operand2.replace('%',"")

            operand1 = operand1.replace('-0x11(rbp)',"buff")
            operand2 = operand2.replace('-0x11(rbp)',"buff")

            operand1 = operand1.replace('al',"eax")
            operand2 = operand2.replace('al',"eax")
            
            operand1 = operand1.replace('$',"")
            operand2 = operand2.replace('$',"")

            if opcode == 'mov' or opcode == 'movzbl':
                python_code += operand2 + "=" + operand1 + "\n"
            if opcode == "shr":
                python_code += operand2 + "=" + "SHR(" +operand2 + "," + operand1 + ")" + "\n"
            if opcode == "shl":
                python_code += operand2 + "=" + "SHL(" +operand2 + "," + operand1  + ")" + "\n"
            if opcode == "sar":
                python_code += operand2 + "=" + "SAR(" +operand2 + "," + operand1 + ")" + "\n"
            if opcode == "xor" or opcode == "xorb":
                python_code += operand2 + "=" + "XOR(" +operand2 + "," + operand1 + ")" + "\n"
            if opcode == "and":
                python_code += operand2 + "=" + "AND(" +operand2 + "," + operand1 + ")" + "\n"
            if opcode == "add":
                python_code += operand2 + "=" + "ADD(" +operand2 + "," + operand1 + ")" + "\n"
        except:
            pass

    return(python_code)


print(target)
print(instruction)
res = ''
for k in range(16):
    targ = int(target[2*k:2*(k+1)],16)
    for i in range(256):
        python_code = parse_assembly_instructions(instruction)
        buff = 0
        eax = i
        edx = 0

        for line in python_code.split('\n'):
            exec(line)
        if eax == targ:
            res += (chr(i))

res = res[0:8][::-1] + res[8:][::-1]

print(res)



#nc challenges.404ctf.fr 31998 > chall.zip ; unzip chall.zip ; objdump -d crackme.bin | xclip -selection clipboard; cat token.txt > nc challenges.404ctf.fr 31999