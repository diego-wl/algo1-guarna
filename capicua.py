""" 
Escribir un programa que solicite el ingreso de una serie de números.
Por cada número ingresado se deberá informar si el mismo es ó no, un número
capicúa.
Se debe evaluar que lo ingresado, sea un número entero positivo; de lo contrario,
se debe enviar el mensaje “Número Inválido”, y solicitar el siguiente.
El ingreso de números, termina cuando en lugar de un número positivo, el usuario ingresa 0.
"""
BASE_NUMERICA = 10

def es_igual(x, y):
  return x == y

def es_dintinto(x, y):
  return not es_igual(x, y)

def solicitar_numero():
  mensaje = "Ingrese un valor entero positivo o cero para finalizar:"
  valor = int(input(mensaje))

  while (valor < 0):
    print("Numero Invalido\n")
    valor = int(input(mensaje))

  return valor

def es_capicua(num):
  return False

def procesar_serie():
  numero = solicitar_numero()

  while es_dintinto(numero, 0):
    if es_capicua(numero):
      print(f'El numero {numero} es capicua\n')
    else:
      print(f'El numero {numero} no es capicua\n')

    numero = solicitar_numero()


print('Debe ingresar una serie de numeros enteros positivos y se le indicará si son capicua o no\n\n')
procesar_serie()
print('Programa finalizado.')