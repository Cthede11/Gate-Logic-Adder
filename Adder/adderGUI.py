import tkinter as tk
import gateAdder


def get_inputs():
    input1 = [int(i) for i in entry1.get().split(",")]
    input2 = [int(i) for i in entry2.get().split(",")]
    inputs = [val for pair in zip(input1, input2) for val in pair]
    sumList = []
    gateAdder.Adder(inputs, sumList)
    result_label.config(text=sumList)

root = tk.Tk()

label1 = tk.Label(root, text="Enter the first variable:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter the second variable:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Add", command=get_inputs)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()