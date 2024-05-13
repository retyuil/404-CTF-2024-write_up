def convert_to_little_endian(address):
    # Supprime le préfixe '0x' et inverse la chaîne pour obtenir les octets en little-endian
    address_bytes = bytes.fromhex(address[2:])[::-1]
    # Convertit les octets en une chaîne hexadécimale
    little_endian_address = address_bytes.hex()
    return little_endian_address

def generate_gdb_commands():
    commands = []
    address = 0x7fffffffdc70
    values = list(range(256))  # Generate values from 0x00 to 0xFF

    for i in range(0, len(values), 8):
        chunk = values[i:i+8]
        command = "restart " + str(i//8 + 1) + "\n"
        command += "set {{unsigned char[8]}}{} = {{{}}}".format(hex(address), ', '.join(hex(v) for v in chunk))
        command += "\ncheckpoint"
        command += "\nn \nx/2x 0x7fffffffdc50 \n" 
        commands.append(command)

    return commands

gdb_commands = generate_gdb_commands()

with open('dump.txt' ) as f:
    data = f.read()

data = data.split('\n')

useful = []

for line in data:
    if '0x7fffffffdc50' in line:
        res = line[16:].split('\t')[0]
        res2 = line[16:].split('\t')[1]
        res3 = convert_to_little_endian(res)
        res4 = convert_to_little_endian(res2)
        useful.append([res3,res4])


print(useful)


merged_string = ''.join([item for sublist in [[''.join(subsublist) for subsublist in sublist] for sublist in useful] for item in sublist])

merged_string = merged_string.replace('0x','')
merged_string = merged_string.replace(' ','')
merged_string = merged_string.replace('\n','')
function ={}

print(merged_string)
for k in range(256):
    function[ merged_string[2*k:2*k+2]] = hex(k)[2:].zfill(2) 

print(function)


#target = "0xe2af4296 0xc754f68a"
target = convert_to_little_endian('0x40345b36')
target += convert_to_little_endian('0xa52da56f')
target += convert_to_little_endian('0x41e15bc7')
target += convert_to_little_endian('0x40341501')

print(target)

key = '' 
for k in range(16):
    key += function[target[2*k:2*(k+1)]]

print(key)


#4XHWTKLXbmujxB9QtI0mQ2zsV12LfdnvTaKm8JBJVaCix4Km