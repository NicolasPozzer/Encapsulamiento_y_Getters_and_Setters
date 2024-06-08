#Para encapsular en python usamos el Guion BAJO "_"
# si queremos declarar como un atributo o metodo Privado
# utilizamod un solo Guion, y si queremos declarar como
# un atributo o metodo muy privado asignamos dos Guiones.

#Ejemplo
# Privado = "_contrasenia"
# Muy privado = "__contrasenia"

#NOTA: Con getter y setter es la unica forma de manipular atributos que son "muy Privados".

class MiClase:
    def __init__(self):
        self._atributo_privado = "_atributo_privado"#Asignacion de valor desde el inicio
        self.__atributo_muy_privado = "__atributo_muy_privado"#Asignacion de valor desde el inicio

miclase = MiClase()
print(miclase._atributo_privado)

