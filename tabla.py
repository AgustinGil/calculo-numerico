from math import ceil, floor

class Tabla:
    def __init__(self,indices: list):
        self.indices: list[str] = indices
        self.contenido: list = [indices]
        self.__longitudes_maximas: list = []
        self.__ancho_tabla: int
    
    def __establecer_longitudes_maxima(self) -> None:
        for i in range(len(self.indices)):
            self.__longitudes_maximas.append(max(map(len,map(str,[x[i] for x in self.contenido]))))

    def __establecer_ancho_tabla(self) -> None:
        self.__ancho_tabla = sum(self.__longitudes_maximas)+len(self.indices)*2+len(self.indices)+1

    def __repetir_caracter(self, char:str, n:int) -> str:
        return (char*n)[0:n]

    def agregar_fila(self,elementos: list) -> None:
        if (len(elementos) == len(self.indices)):
            self.contenido.append(elementos)
        else:
            raise ValueError('El numero de elementos no coincide con la cantidad de indices')

    def obtener_contenido(self) -> list:
        return self.contenido

    def obtener_string(self) -> str:
        tabla_string = ''
        self.__establecer_longitudes_maxima()
        self.__establecer_ancho_tabla()
        for fila in self.contenido:
            tabla_string += f"{self.__repetir_caracter('-',self.__ancho_tabla)}\n"
            for elemento in enumerate(fila):
                espacio_total = self.__longitudes_maximas[elemento[0]] - len(str(elemento[1]))
                espacio_previo = self.__repetir_caracter(' ',ceil(espacio_total/2))
                espacio_posterior = self.__repetir_caracter(' ',floor(espacio_total/2))
                tabla_string += f"| {espacio_previo}{elemento[1]}{espacio_posterior} "
                
                if elemento[0] == len(self.indices)-1:
                    tabla_string += '|\n'

        tabla_string += f"{ self.__repetir_caracter('-',self.__ancho_tabla)}"
        return tabla_string