import tkinter as tk
from tkinter import messagebox

class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
            'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
        }

    def to_roman(self, num):
        if not 0 < num < 4000:
            return 'Número fora do intervalo (1-3999)'

        result = ''
        for symbol, value in sorted(self.roman_numerals.items(), key=lambda x: x[1], reverse=True):
            while num >= value:
                result += symbol
                num -= value
        return result

    def to_decimal(self, roman):
        result = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i + 2] in self.roman_numerals:
                result += self.roman_numerals[roman[i:i + 2]]
                i += 2
            else:
                result += self.roman_numerals[roman[i]]
                i += 1
        return result


def convert_decimal_to_roman():
    try:
        decimal_input = int(decimal_entry.get())
        roman_output = converter.to_roman(decimal_input)
        result_label.config(text=f"O número romano equivalente a {decimal_input} é: {roman_output}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido")


def convert_roman_to_decimal():
    roman_input = roman_entry.get().upper()
    decimal_output = converter.to_decimal(roman_input)
    if decimal_output == 'Número fora do intervalo (1-3999)' or decimal_output == 0:
        messagebox.showerror("Erro", "Digite um número romano válido")
    else:
        result_label.config(text=f"O número decimal equivalente a {roman_input} é: {decimal_output}")


# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor de Números Romanos")

converter = RomanConverter()

decimal_label = tk.Label(root, text="Digite o número decimal:")
decimal_entry = tk.Entry(root)
decimal_convert_button = tk.Button(root, text="Converter para Romano", command=convert_decimal_to_roman)

roman_label = tk.Label(root, text="Digite o número romano:")
roman_entry = tk.Entry(root)
roman_convert_button = tk.Button(root, text="Converter para Decimal", command=convert_roman_to_decimal)

result_label = tk.Label(root, text="Resultado aqui", font=("Arial", 12))

decimal_label.pack()
decimal_entry.pack()
decimal_convert_button.pack()
roman_label.pack()
roman_entry.pack()
roman_convert_button.pack()
result_label.pack()

root.mainloop()
