
# Parent Gate Class
class Gate:
    def __init__(self, name):
        self.name = name
        self.output = None
        self.outputs = []

    def get_output(self):
        self.output = self.perform_gate_logic()
        for gate in self.outputs:
            gate.set_input(self.output)
        return self.output
    
# Child Logic Gates
class AndGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input1 = None
        self.input2 = None

    def set_input(self, input1, input2=None):
        self.input1 = input1
        self.input2 = input2

    def perform_gate_logic(self):
        if self.input1 == 1 and self.input2 == 1:
            return 1
        else:
            return 0
    

class OrGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input1 = None
        self.input2 = None

    def set_input(self, input1, input2=None):
        self.input1 = input1
        self.input2 = input2

    def perform_gate_logic(self):
        if self.input1 == 1 or self.input2 == 1:
            return 1
        else:
            return 0
    

class XorGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input1 = None
        self.input2 = None

    def set_input(self, input1, input2=None):
        self.input1 = input1
        self.input2 = input2

    def perform_gate_logic(self):
        if self.input1 == self.input2:
            return 0
        else:
            return 1


class NotGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input = None

    def set_input(self, input):
        self.input = input

    def perform_gate_logic(self):
        if input == 1:
            return 0
        else:
            return 1

#-------------------------------------------------
# Adder Logic


# Half Adder
def halfAdder(input1, input2, sumList):
    xor_gate1 = XorGate("XOR1")
    xor_gate1.set_input(input1, input2)
    sum_out = xor_gate1.get_output()
    and_gate1 = AndGate("AND1")
    and_gate1.set_input(input1, input2)
    carry_out = and_gate1.get_output()
    sumList.append(sum_out)
    sumList.append(carry_out)

    return sum_out, carry_out

# Full Adder
def fullAdder(inputList, sumList, x, y):
    carry_out1 = sumList.pop()
    xor_gate2 = XorGate("XOR2")
    xor_gate2.set_input(inputList[x], inputList[y])
    sum1 = xor_gate2.get_output()
    xor_gate3 = XorGate("XOR3")
    xor_gate3.set_input(sum1, carry_out1)
    sum_out = xor_gate3.get_output()
    and_gate2 = AndGate("AND2")
    and_gate2.set_input(sum1, carry_out1)
    carry1 = and_gate2.get_output()
    and_gate3 = AndGate("AND3")
    and_gate3.set_input(inputList[x], inputList[y])
    carry2 = and_gate3.get_output()
    or_gate = OrGate("OR1")
    or_gate.set_input(carry1, carry2)
    carry_out = or_gate.get_output()
    sumList.append(sum_out)
    sumList.append(carry_out)
    

def Adder(inputList, sumList):
    # First Half Adder
    halfAdder(inputList[0], inputList[1], sumList)
    # full adder loop
    x = 2
    y = 3
    while y < len(inputList):
        fullAdder(inputList, sumList, x, y)
        x += 2
        y += 2
    print(sumList)
    sumList.reverse()
    return sumList


def takeUserInput():
    # accidentally made the entire thing work on one input list
    userInput1 = input("Enter the first variable: ")
    userInput2 = input("Enter the second variable: ")
    userInputList1 = userInput1.split(",")
    userInputList2 = userInput2.split(",")
    userInputList1.reverse()
    userInputList2.reverse()
    # combine the two lists into one, iteratively
    finInputList = [item for sublist in zip(userInputList1, userInputList2) for item in sublist]
    finInputList = [int(i) for i in finInputList]
    print(finInputList)
    return finInputList


sumList = []
Adder(takeUserInput(), sumList)
print(*sumList)