from math import ceil, floor

class Tabla:
    def __init__(self,indices: list):
        self.indices: list = indices
        self.contenido: list = [indices]
        self.longitudes_maximas: list = []
        self.ancho_tabla: int

    def obtener_contenido(self) -> list:
        return self.contenido
    
    def establecer_longitudes_maxima(self) -> None:
        for i in range(len(self.indices)):
            self.longitudes_maximas.append(max(map(len,map(str,[x[i] for x in self.contenido]))))

    def establecer_ancho_tabla(self) -> None:
        self.ancho_tabla = sum(self.longitudes_maximas)+len(self.indices)*2+len(self.indices)+1

    def agregar_fila(self,elementos: list) -> None:
        if (len(elementos) == len(self.indices)):
            self.contenido.append(elementos)
        else:
            raise ValueError('El numero de elementos no coincide con la cantidad de indices')

    def repetir_caracter(self, char:str, n:int) -> str:
        return (char*n)[0:n]

    def formatear_string(self) -> str:
        tabla_string = ''
        self.establecer_longitudes_maxima()
        self.establecer_ancho_tabla()
        for fila in self.contenido:
            tabla_string += f"{self.repetir_caracter('-',self.ancho_tabla)}\n"
            for elemento in enumerate(fila):
                espacio_total = self.longitudes_maximas[elemento[0]] - len(str(fila[elemento[0]]))
                espacio_previo = self.repetir_caracter(' ',ceil(espacio_total/2))
                espacio_posterior = self.repetir_caracter(' ',floor(espacio_total/2))
                tabla_string += f"| {espacio_previo}{fila[elemento[0]]}{espacio_posterior} "
                if elemento[0] == len(self.indices)-1:
                    tabla_string += '|\n'

        tabla_string += f"{ self.repetir_caracter('-',self.ancho_tabla)}"
        return tabla_string