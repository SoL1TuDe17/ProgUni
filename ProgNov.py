import tkinter as tk

class SimpleRegisters:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Системы счисления")
        self.window.geometry("400x300")
        self.registers = [0, 0, 0, 0]
        self.create_widgets()
        
    def create_widgets(self):
        label = tk.Label(self.window, text="Щелкайте по квадратам чтобы изменить значения")
        label.pack(pady=10)
        frame = tk.Frame(self.window)
        frame.pack(pady=20)
        self.squares = []
        for i in range(4):
            btn = tk.Button(frame, text="0", width=4, height=2, 
                           font=("Arial", 14),
                           command=lambda idx=i: self.click_register(idx))
            btn.grid(row=0, column=i, padx=5)
            self.squares.append(btn)
        self.result_binary = tk.Label(self.window, text="Двоичное число: 0")
        self.result_binary.pack(pady=5)
        self.result_ternary = tk.Label(self.window, text="Троичное число: 0")
        self.result_ternary.pack(pady=5)
        self.result_mixed = tk.Label(self.window, text="Смешанное число: 0")
        self.result_mixed.pack(pady=5)
        self.result_decimal = tk.Label(self.window, text="Десятичное число: 0", font=("Arial", 12, "bold"))
        self.result_decimal.pack(pady=10)
        reset_btn = tk.Button(self.window, text="Сбросить все в 0", command=self.reset_all)
        reset_btn.pack(pady=10)
    
    def click_register(self, index):
        if self.registers[index] == 0:
            self.registers[index] = 1
            self.squares[index].config(text="1", bg="lightblue")
        else:
            self.registers[index] = 0
            self.squares[index].config(text="0", bg="lightgray")
        self.calculate_numbers()
    
    def calculate_numbers(self):
        binary = 0
        for i in range(4):
            if self.registers[i] == 1:
                binary += 2 ** (3 - i)  # 8, 4, 2, 1
        ternary = 0
        for i in range(4):
            ternary += self.registers[i] * (3 ** (3 - i))  # 27, 9, 3, 1
        mixed = 0
        mixed = (self.registers[3] * 1 + 
                self.registers[2] * 3 + 
                self.registers[1] * 6 + 
                self.registers[0] * 12)
        decimal = binary
        self.result_binary.config(text=f"Двоичное число: {binary}")
        self.result_ternary.config(text=f"Троичное число: {ternary}")
        self.result_mixed.config(text=f"Смешанное число: {mixed}")
        self.result_decimal.config(text=f"Десятичное число: {decimal}")
    
    def reset_all(self):
        for i in range(4):
            self.registers[i] = 0
            self.squares[i].config(text="0", bg="lightgray")
        self.calculate_numbers()
    
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    app = SimpleRegisters()
    app.run()

