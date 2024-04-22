nombre=input("Introduce tu nombre: ")
apellido=input("Introduce tu apellido: ")
edad=int(input("Introduce tu edad: "))
correo=input("Introduce tu correo electrónico: ")
telefono= input("Introduce tu teléfono: ") #Aquí no estamos colocando que sea un dato de tipo int ya que si el número iniciara con 0s ej. 01800;
                                            #el 0 desaparecería
print("Nombre: "+ nombre)
print("Apellido: "+ apellido)
print("Tengo "+ str(edad)+ " años de edad")
print("Correo: " +correo)
print("Teléfono: "+ telefono)