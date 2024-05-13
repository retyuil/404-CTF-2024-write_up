

exemple = {"gates": [["CNOT", [0, 1]], ["NOT", [1]], ["CNOT", [2, 0]], ["TOFFOLI", [1, 2, 0]], ["NOT", [0]], ["NOT", [0]], ["TOFFOLI", [2, 0, 1]], ["TOFFOLI", [1, 2, 0]]], "bits": 3}

def TOFFOLI(state,control):
	state[control[2]] =  ((state[control[0]] and state[control[1]]) ^ state[control[2]])

def not_gate(state,control):
	state[control[0]] =  int(not state[control[0]])

def cnot(state,control):
	if state[control[0]]:
		state[control[1]] = int(not state[control[1]])



def apply(state,circuit):
	for gate in circuit:
		if gate[0] == 'TOFFOLI':
			TOFFOLI(state,gate[1])
		if gate[0] == 'CNOT':
			cnot(state,gate[1])
		if gate[0] == 'NOT':
			not_gate(state,gate[1])
	return state


def calculate_effect(circuit):
	truth_table = []
	for i in range(2**3):
		entry = list(bin(i)[2:].zfill(3))
		for i in range(3):
			entry[i] = int(entry[i])
		truth_table.append(apply(entry,circuit))
	return truth_table

truth_table = calculate_effect(exemple['gates'])

control_T = {0 : [0,1,2],
1 : [2,1,0],
2 : [0,2,1] 
}

control_C = {0 : [0,2],
1 : [0,1],
2 : [1,2],
3 : [1,0],
4 : [2,0],
5 : [2,1] 
}

control_N = {
	0 : [0],
	1 : [1],
	2 : [2]
}

def brute_force_one():
	circuits = []
	for k in range(3):
		if k == 0:
			circuit = ["TOFFOLI",[0,0,0]]
			for i in range(3):
				circuit[1] = control_T[i]
				circuits.append([(circuit.copy())])
		if k == 1:
			circuit = ["CNOT",[0,0]]
			for i in range(6):
				circuit[1] = control_C[i]
				circuits.append([(circuit.copy())])
		if k == 2:
			circuit = ["NOT",[0]]
			for i in range(3):
				circuit[1] = control_N[i]
				circuits.append([(circuit.copy())])
	return circuits




def brute_force(nb_gates,truth_table):
	one = brute_force_one()
	print(one)
	circuits = one.copy()
	for k in range(nb_gates):
		temp = []
		for gate in one:
			for circuit in circuits:
				temp.append(circuit + gate)
		circuits = temp.copy()
	for circuit in circuits:
		if calculate_effect(circuit) == truth_table:
			print('{"gates": '  + str(circuit).replace("'",'"') +  ', "bits": 3}')

for k in range(5):
	res = brute_force(k,truth_table)
	print(res)

