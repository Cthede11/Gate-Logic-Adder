
# Convert all to object oriented programming
# Could eventually make a gui for this
def and_gate(input1, input2):
    if input1 != 1 or 0 or input2 != 1 or 0:
        print("AND gate error: invalid input")
        print("Input type:", type(input1))
    elif input1 == 1 and input2 == 1:
        return 1
    else:
        input1 == 0 or input2 == 0
        return 0

def or_gate(input1, input2):
    if input1 != 1 or 0 or input2 != 1 or 0:
        print("OR gate error: invalid input")
        print("Input type:", type(input1))
    else:
        input1 == 1 or input2 == 1
        return 1
    
def xor_gate(input1, input2):
    if input1 != 1 or 0 or input2 != 1 or 0:
        print("XOR gate error: invalid input")
        print("Input type:", type(input1))
    elif input1 == 1 and input2 == 0:
        return 1
    elif input1 == 0 and input2 == 1:
        return 1
    else:
        return 0
    
def not_gate(input1:type = int):
    if input1 != 1 or 0:
        print("NOT gate error: invalid input")
        print("Input type:", type(input1), "\nInput: ", input1)
    elif input1 == 1:
        print(0)
        return 0
    elif input1 == 0:
        print(1)
        return 1
    
def connection(input_connect, output_connect_list):
    for i in output_connect_list:
        if i not in gate_list:
            print("-------------------\nCONNECTION error: invalid input or output")
            print("Output type:", type(i), "\nOutput: ", i)
            print("Gate list:", gate_list)
            print("Input type:", type(input_connect), "\nInput: ", input_connect, "\n-------------------")
            
            return False
        return i == input_connect

gate_list = [and_gate, or_gate, xor_gate, not_gate]

not_gate(int(0))
connection(1, [and_gate, or_gate, xor_gate, not_gate])