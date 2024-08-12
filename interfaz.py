import tkinter as tk
from grammar import Grammar
from predict_table import PredictTable
from main import PDA

class PDAGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Verificador de Cadenas")
        self.geometry("600x600")
        self.configure(bg="#333")
        self.pda = PDA(Grammar(), PredictTable())  # Crear la instancia de PDA aquí
        self.crear_interfaz()

    def crear_interfaz(self):
        self.label = tk.Label(self, text="Verificador de Cadenas", font=('Arial', 16), bg="#333", fg="yellow")
        self.label.pack(pady=10)

        self.input_label = tk.Label(self, text="Ingrese una cadena:", font=('Arial', 16), bg="#333", fg="white")
        self.input_label.pack(pady=10)
        
        self.input_entry = tk.Entry(self, font=('Arial', 16), width=30, relief="solid", borderwidth=2)
        self.input_entry.pack(pady=10)
        
        estilo_boton = {
            'font': ('Arial', 20, 'bold'), 
            'fg': '#333',
            'bg': 'white',
            'width': 11,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }
        
        self.verify_button = tk.Button(self, text="Verificar", command=self.verify_input, **estilo_boton)
        self.verify_button.pack(pady=10)
        

        self.result_stack_label = tk.Label(self, text="Pila:", font=('Arial', 12), bg="#333", fg="white")
        self.result_stack_label.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.stack_text = tk.Text(self, height=20, width=60, font=('Arial', 12), relief="solid", borderwidth=2,
                                  yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.stack_text.yview)
        self.stack_text.pack(pady=10)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.result_label = tk.Label(self, text="", font=('Arial', 14), bg="#333", fg="white")
        self.result_label.pack(pady=10)
    def verify_input(self):
        input_string = self.input_entry.get()
        stack_trace = self.pda.process_input(input_string)
        
        self.stack_text.delete('1.0', tk.END)
        
        if isinstance(stack_trace, list):  # Verificar si stack_trace es una lista
            for step in stack_trace:
                self.stack_text.insert(tk.END, "Pila: " + str(step[1]) + "\n")
                self.stack_text.insert(tk.END, "\n")

            if stack_trace[-1] is not False:  # Si la traza de la pila es una lista válida
                self.result_label.config(text="La cadena es válida.")
            else:
                self.result_label.config(text="La cadena no es válida.")
        else:
            self.stack_text.insert(tk.END, "Pila: " + str(stack_trace) + "\n")
            self.result_label.config(text="La cadena no es válida.")

if __name__ == "__main__":
    app = PDAGUI()
    app.mainloop()
