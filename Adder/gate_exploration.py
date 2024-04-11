
# Parent Gate Class
class Gate:
    def __init__(self, name):
        self.name = name
        self.next_gate = None

    def set_next_gate(self, gate):
        self.next_gate = gate

    def get_output(self):
        output = self.perform_gate_logic()
        if self.next_gate:
            return self.next_gate.perform_gate_logic()
        return output
    
# Child Logic Gates
class AndGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input1 = None
        self.input2 = None

    def set_input(self, input1, input2):
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

    def set_input(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def perform_gate_logic(self):
        return bool(self.input1) != bool(self.input2)


class NotGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.input = None

    def set_input(self, input):
        self.input = input

    def perform_gate_logic(self):
        return not self.input


# Child Connector Class for connecting gates
class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        if isinstance(to_gate, NotGate):
            to_gate.set_input(from_gate.get_output())
        else:
            to_gate.set_input(from_gate.get_output(), None)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate
    


    #-------------------------------------------------
    # Test the classes

# Create gates
and_gate = AndGate("AND1")
or_gate = OrGate("OR1")
xor_gate = XorGate("XOR1")
not_gate = NotGate("NOT1")

# Set inputs for the AND gate
and_gate.set_input(1, 1)
#1

# Connect AND gate to OR gate
conn1 = Connector(and_gate, or_gate)

# Set another input for the OR gate
or_gate.set_input(conn1.get_to().get_output(), 0)
#1

# Connect OR gate to XOR gate
conn2 = Connector(or_gate, xor_gate)

# Set another input for the XOR gate
xor_gate.set_input(conn2.get_to().get_output(), 1)
#0

# Connect XOR gate to NOT gate
conn3 = Connector(xor_gate, and_gate)

and_gate.set_input(conn3.get_to().get_output(), 0)
#0

conn4 = Connector(and_gate, not_gate)

# Get output from the NOT gate
output = not_gate.get_output()

print(output)  # prints: True