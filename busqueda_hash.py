class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    def _funcion_hash(self, clave):
        """Genera un índice usando una función hash simple"""
        return hash(clave) % self.tamaño

    def insertar(self, clave, valor):
        """Inserta un valor en la tabla hash"""
        indice = self._funcion_hash(clave)
        if self.tabla[indice] is None:
            self.tabla[indice] = []
        self.tabla[indice].append((clave, valor))

    def buscar(self, clave):
        """Busca un valor dado su clave"""
        indice = self._funcion_hash(clave)
        if self.tabla[indice] is not None:
            for k, v in self.tabla[indice]:
                if k == clave:
                    return v
        return None

    def eliminar(self, clave):
        """Elimina un valor dado su clave"""
        indice = self._funcion_hash(clave)
        if self.tabla[indice] is not None:
            for i, (k, _) in enumerate(self.tabla[indice]):
                if k == clave:
                    del self.tabla[indice][i]
                    return True
        return False

#Ejemplo 1
print("Ejemplo 1")
usuarios= TablaHash(10)

usuarios.insertar("Adrian",19)
usuarios.insertar("Ana",19)
usuarios.insertar("Rafael",19)
usuarios.insertar("Gelmy",19)
usuarios.insertar("Carmen",19)
usuarios.insertar("Luis",19)
usuarios.insertar("Lucia",19)
usuarios.insertar("Julio",19)
usuarios.insertar("Guadalupe",19)
usuarios.insertar("Marisol",19)

print("Buscar la edad de Ana:", usuarios.buscar("Ana"))
print("Buscar la edad de Lucia:", usuarios.buscar("Lucia"))

usuarios.eliminar("Guadalupe")
print("Buscar la edad de Guadalupe:", usuarios.buscar("Guadalupe"))

print("\n")
#Ejemplo 2
print("Ejemplo 2")
calificaciones= TablaHash(10)

calificaciones.insertar("Alumno1","Luis - 83")
calificaciones.insertar("Alumno2","Maria - 70")
calificaciones.insertar("Alumno3","Carlos - 93")
calificaciones.insertar("Alumno4","Carmen - 76")
calificaciones.insertar("Alumno5","Odalys - 90")
calificaciones.insertar("Alumno6","Ana - 80")
calificaciones.insertar("Alumno7","Roberto - 77")
calificaciones.insertar("Alumno8","Juliana - 95")
calificaciones.insertar("Alumno9","Bryan - 72")
calificaciones.insertar("Alumno10","Jose - 89")

print("Buscar al alumno 4:", calificaciones.buscar("Alumno4"))
print("Buscar al alumno 7:", calificaciones.buscar("Alumno7"))

calificaciones.eliminar("Alumno9")
print("Buscar al alumno 9:", calificaciones.buscar("Alumno9"))