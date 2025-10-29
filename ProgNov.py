import tkinter as tk

class SimpleRegisters:
    def __init__(self):
        # Создаем главное окно
        self.window = tk.Tk()
        self.window.title("Системы счисления")
        self.window.geometry("400x300")
        
        # Здесь хранятся значения регистров (0 или 1)
        self.registers = [0, 0, 0, 0]
        
        # Создаем все элементы
        self.create_widgets()
        
    def create_widgets(self):
        # Надпись вверху
        label = tk.Label(self.window, text="Щелкайте по квадратам чтобы изменить значения")
        label.pack(pady=10)
        
        # Фрейм для регистров
        frame = tk.Frame(self.window)
        frame.pack(pady=20)
        
        # Создаем 4 квадрата-регистра
        self.squares = []
        for i in range(4):
            # Создаем квадрат (на самом деле кнопка)
            btn = tk.Button(frame, text="0", width=4, height=2, 
                           font=("Arial", 14),
                           command=lambda idx=i: self.click_register(idx))
            btn.grid(row=0, column=i, padx=5)
            self.squares.append(btn)
        
        # Надписи с результатами
        self.result_binary = tk.Label(self.window, text="Двоичное число: 0")
        self.result_binary.pack(pady=5)
        
        self.result_ternary = tk.Label(self.window, text="Троичное число: 0")
        self.result_ternary.pack(pady=5)
        
        self.result_mixed = tk.Label(self.window, text="Смешанное число: 0")
        self.result_mixed.pack(pady=5)
        
        self.result_decimal = tk.Label(self.window, text="Десятичное число: 0", font=("Arial", 12, "bold"))
        self.result_decimal.pack(pady=10)
        
        # Кнопка сброса
        reset_btn = tk.Button(self.window, text="Сбросить все в 0", command=self.reset_all)
        reset_btn.pack(pady=10)
    
    def click_register(self, index):
        # Меняем 0 на 1 или 1 на 0
        if self.registers[index] == 0:
            self.registers[index] = 1
            self.squares[index].config(text="1", bg="lightblue")
        else:
            self.registers[index] = 0
            self.squares[index].config(text="0", bg="lightgray")
        
        # Пересчитываем все числа
        self.calculate_numbers()
    
    def calculate_numbers(self):
        # 1. Двоичное число
        binary = 0
        for i in range(4):
            if self.registers[i] == 1:
                binary += 2 ** (3 - i)  # 8, 4, 2, 1
        
        # 2. Троичное число (простое, не уравновешенное)
        ternary = 0
        for i in range(4):
            ternary += self.registers[i] * (3 ** (3 - i))  # 27, 9, 3, 1
        
        # 3. Смешанное основание (2,3,2,3)
        mixed = 0
        # Идем справа налево: разряд0*1 + разряд1*2 + разряд2*6 + разряд3*12
        mixed = (self.registers[3] * 1 + 
                self.registers[2] * 3 + 
                self.registers[1] * 6 + 
                self.registers[0] * 12)
        
        # 4. Десятичное (берем двоичное)
        decimal = binary
        
        # Обновляем надписи
        self.result_binary.config(text=f"Двоичное число: {binary}")
        self.result_ternary.config(text=f"Троичное число: {ternary}")
        self.result_mixed.config(text=f"Смешанное число: {mixed}")
        self.result_decimal.config(text=f"Десятичное число: {decimal}")
    
    def reset_all(self):
        # Все регистры в 0
        for i in range(4):
            self.registers[i] = 0
            self.squares[i].config(text="0", bg="lightgray")
        self.calculate_numbers()
    
    def run(self):
        # Запускаем программу
        self.window.mainloop()

# Запускаем программу
if __name__ == "__main__":
    app = SimpleRegisters()
    app.run()
