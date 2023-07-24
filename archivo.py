import sys

# Define una variable de cada tipo de primitivo
integer_var = 42
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True

# Concatena las otras variables aplicando la conversión correcta para funcionar
concatenated_string = string_var + " " + str(integer_var) + " " + str(float_var) + " " + str(boolean_var)

# Imprime el resultado de la concatenación
print("Concatenated String:", concatenated_string)

# Límite de los enteros y los flotantes en Python

# Límite de los enteros:
# En Python, los enteros no tienen límite teórico, ya que Python 3 utiliza un sistema de números enteros de longitud variable (integers of arbitrary precision).
# Esto significa que los enteros pueden ser tan grandes como la memoria del sistema lo permita.

# Límite de los flotantes:
# En Python, los flotantes son de doble precisión de 64 bits según el estándar IEEE 754. El valor máximo y mínimo representable por un flotante en Python es:
# Mayor valor positivo:
max_float = float(sys.float_info.max)
# Menor valor positivo (valor cercano a cero):
min_float = float(sys.float_info.min)

# Aplica la fórmula de la suma de los primeros n números pares
# La fórmula para la suma de los primeros n números pares es: sum = n * (n + 1)
n = 10
sum_of_first_n_even_numbers = n * (n + 1)

# Imprime los resultados de las tareas anteriores
print("Maximum representable float:", max_float)
print("Minimum representable positive float:", min_float)
print("Sum of the first", n, "even numbers:", sum_of_first_n_even_numbers)