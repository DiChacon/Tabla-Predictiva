from grammar import Grammar
from predict_table import PredictTable

class PDA:
    def __init__(self, grammar, predict_table):
        self.grammar = grammar
        self.predict_table = predict_table

    def process_input(self, input_string):
        # Verificar si la cadena comienza con "let"
        if not input_string.startswith("let"):
            print("Error: La cadena no comienza con 'let'.")
            return False

        stack = ['$']
        input_string = input_string.replace(" ", "")  # Eliminar espacios en blanco
        input_string += '$'  # Agregar $ al final de la cadena
        input_pointer = 0
        stack_trace = [] 

        # Agregar el símbolo inicial 'A' a la pila
        stack.append('A')

        # Loop principal del autómata
        while True:
            X = stack[-1]  # Símbolo en la cima de la pila
            a = input_string[input_pointer]  # Símbolo apuntado en la cadena
            print("Cadena de entrada:", input_string[input_pointer:])  # Imprimir la cadena de entrada restante
            print("Pila:", stack)
            print("Símbolo en la pila (X):", X)
            print("Símbolo apuntado en la cadena (a):", a)
            # Almacenar el estado de la pila en la traza
            stack_trace.append((input_string[input_pointer:], stack.copy()))

            # Si el símbolo apuntado en la cadena es $
            if a == '$':
                print("Fin de la cadena.")
                if X == '$':
                    stack.pop()  # Eliminar el $
                    return stack_trace
                else:
                    print("Error: La cadena ha sido consumida pero la pila no está vacía.")
                    return False

            # Caso base: X es terminal
            if X in self.grammar.terminals:
                if X == a:
                    stack.pop()
                    input_pointer += 1
                elif X == 'let':  # Si el símbolo en la pila es "let"
                    stack.pop()
                else:
                    return False  # Error
            else:  # X es no terminal
                if X == 'A':
                    stack.pop()  # Extraer X de la pila
                    productions = self.grammar.productions['A']
                    for symbol in reversed(productions):
                        stack.append(symbol)
                elif X == 'T':
                    if input_string[input_pointer:input_pointer+3] == 'let':
                        stack.pop()  # Extraer X de la pila
                        stack.append('let')  # Consumir 'let' como un todo
                        input_pointer += 3  # Avanzar el puntero 3 posiciones
                elif X == ';' and a == ';':
                    input_pointer += 1
                    stack.pop()
                elif a.isdigit():
                    if X == 'D':
                        if input_string[input_pointer] in self.predict_table.table['D']['0..9']:
                            stack.pop()  # Extraer X de la pila
                            stack.append(input_string[input_pointer])
                            input_pointer += 1
                            stack.pop()
                        else:
                            return False
                    else:
                        production = self.predict_table.table[X]['0..9']
                        if production is not None:
                            stack.pop()
                            for symbol in reversed(production):
                                stack.append(symbol)
                        else:
                            return False
                elif a.isalpha():
                    if X == 'L':
                        if input_string[input_pointer] in self.predict_table.table['L']['a...z']:
                            stack.pop()  # Extraer X de la pila
                            stack.append(input_string[input_pointer])
                            input_pointer += 1
                            stack.pop()
                        else:
                            return False
                    else:
                        production = self.predict_table.table[X]['a...z']
                        if production is not None:
                            stack.pop()  # Extraer X de la pila
                            for symbol in reversed(production):
                                stack.append(symbol)
                        else:
                            return False
                elif X in self.predict_table.table:
                    production = self.predict_table.table[X][a]

                    if production == ['empty']:
                        stack.pop()  # Extraer X de la pila
                    else:
                        stack.pop()  # Extraer X de la pila
                        if production is not None:
                            for symbol in reversed(production):
                                stack.append(symbol)
                        else:
                            return False
                else:
                    return False

    def is_valid(self, input_string):
        return self.process_input(input_string)

# Crear un objeto PDA con la gramática y la tabla de análisis predictivo
grammar = Grammar()
predict_table = PredictTable()

pda = PDA(grammar, predict_table)