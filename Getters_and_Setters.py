#Creacion de atributos y metodos getter y setters privados y probar

class MiClase:
    def __init__(self, nombre, edad):#Aca todavia no se asiganan como privado
        #Aca si!!
        self._nombre = nombre
        self._edad = edad

    #Metodo get de Nombre
    def getNombre(self):
        return self._nombre

    #Metodo Set de nombre
    def setNombre(self, new_nombre):
        self._nombre = new_nombre

#Creacion del objeto para prueba
objeto = MiClase("Nicolas","24")

nombrePersona = objeto.getNombre()

print(nombrePersona) #Imprime Nicolas

#Seteo nuevo valor en el Nombre
objeto.setNombre("Nico")
nombrePersona = objeto.getNombre()#Asigno el nuevo valor al objeto

print(nombrePersona) #Y ahora devuelve Nico