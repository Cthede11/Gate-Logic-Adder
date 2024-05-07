
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

    def connect(self, gate):
        self.outputs.append(gate)
    
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
        return self.input1 and self.input2
    

class OrGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input1 = None
        self.input2 = None

    def set_input(self, input1, input2=None):
        self.input1 = input1
        self.input2 = input2

    def perform_gate_logic(self):
        return self.input1 or self.input2
    

class XorGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input1 = None
        self.input2 = None

    def set_input(self, input1, input2=None):
        self.input1 = input1
        self.input2 = input2

    def perform_gate_logic(self):
        if self.input1 == self.input2 or self.input1:
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
        return not self.input

#-------------------------------------------------
# Test the classes

# Inputs
input1 = 1
input2 = 1

#-----------------------------------------------
# HALF ADDER
# XOR gate for input1 and input2
xor_gate1 = XorGate("XOR1")
xor_gate1.set_input(input1, input2)
out1 = xor_gate1.get_output()
print("Output1: ", out1)

# AND gate for input1 and input2
and_gate1 = AndGate("AND1")
and_gate1.set_input(input1, input2)
carry_out1 = and_gate1.get_output()

#-----------------------------------------------

# AND gate for sum_out and carry_in
and_gate2 = AndGate("AND2")
and_gate2.set_input(sum_out, carry_in)
carry_out2 = and_gate2.get_output()

# OR gate for carry_out1 and carry_out2
or_gate = OrGate("OR1")
or_gate.set_input(carry_out1, carry_out2)
carry_out = or_gate.get_output()

print("Sum:", sum_out)
print("Carry:", carry_out)