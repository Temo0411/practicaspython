# #Podemos usar comillas triples para que el print de una cadena sea seguido.

# print("""
#       Funcionamiento\
# de programas: (opciones)
# -1 Para salir
#     -2 Para entrar
#       """)

texto="Hola mundo qué pedo"
print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.swapcase())
print(texto.title())

# texto=texto.upper()
# print(texto)

print("{}+{}={}".format(2,3,2+3))
print("{}+{}={}".format("Hola","Mundo","Hola Mundo"))
print("{:.3f}+{:.4f}={}".format(2,3,2+3))
print("{2}+{0}={1}".format(2,2,2+3))
print("{2}+{0}={1}".format("Hola","mundo", "Hola Mundo"))
print("{:d}={:b}={:o}={:x}.".format(15,15,15,15))
