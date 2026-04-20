print("\n-------- saludas --------")
def saludar():
  print("Hola")

saludar()

print("\n-------- saludas nombre --------")
def saludarNombre(nombre):
  print(f"Hola {nombre}")

saludarNombre("Maria")

print("\n-------- suma --------")
def suma(n1, n2):
  resultado = n1 + n2
  return resultado

resSuma = suma(1, 2)
print(f"El resultado de 1 + 2 = {resSuma}")

print("\n-------- resta --------")
def resta(n1, n2):
  """Resta dos numero y obtiene el resultado"""
  resultado = n1 - n2
  return resultado

print(resta(10, 5))
#help(resta)

print("\n-------- tabla mult --------")
def tabla_multiplicar(numero, hasta):
  cont = 1
  while cont <= hasta:
    print(f"{cont} * {numero} = {cont * numero}")
    cont += 1 
  
tabla_multiplicar(2, 5)

print("\n-------- multiplicar --------")

def multiplicar(numero, multiplicando = 2):
  return numero * multiplicando
print(multiplicar(2))