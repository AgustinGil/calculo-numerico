from math import ceil, floor

class Tabla:
    def __init__(self,indices: list):
        self.indices: list[str] = indices
        self.contenido: list = [indices]
        self.lineas_columnas: bool = True
        self.padding_columnas: int = 1
        self.__longitudes_maximas: list = []
        self.__ancho_tabla: int
    
    def __establecer_longitudes_maxima(self) -> None:
        for i in range(len(self.indices)):
            self.__longitudes_maximas.append(max(map(len,map(str,[x[i] for x in self.contenido]))))

    def __establecer_ancho_tabla(self) -> None:
        self.__ancho_tabla = sum(self.__longitudes_maximas)+len(self.indices)*(self.padding_columnas*2)+len(self.indices)+1

    def __repetir_caracter(self, char:str, n:int) -> str:
        return (char*n)[0:n]

    def agregar_fila(self,elementos: list) -> None:
        if (len(elementos) == len(self.indices)):
            self.contenido.append(elementos)
        else:
            raise ValueError(f'El numero de elementos ({len(elementos)}) no coincide con la cantidad de indices({len(self.indices)})')
        
    def actualizar_padding(self, padding:int) -> None:
        if(padding >= 0):
            self.padding_columnas = padding
        else:
            raise ValueError("Debe ingresar como padding un valor mayor a 0")
        
    def actualizar_lineas_columnas(self, x: bool) -> None:
        self.lineas_columnas = x

    def obtener_contenido(self) -> list:
        return self.contenido

    def obtener_string(self) -> str:
        tabla_string:str = ''
        self.__establecer_longitudes_maxima()
        self.__establecer_ancho_tabla()

        for fila in self.contenido:
            tabla_string += f"{self.__repetir_caracter('-',self.__ancho_tabla)}\n"
            for elemento in enumerate(fila):
                espacio_total:str = self.__longitudes_maximas[elemento[0]] - len(str(elemento[1]))
                espacio_previo:str = self.__repetir_caracter(' ',ceil(espacio_total/2) + self.padding_columnas) 
                espacio_posterior:str = self.__repetir_caracter(' ',floor(espacio_total/2) + self.padding_columnas)
                tabla_string += ("|" if self.lineas_columnas else "")+f"{espacio_previo}{elemento[1]}{espacio_posterior}"
                
                if elemento[0] == len(self.indices)-1:
                    tabla_string += ('|' if self.lineas_columnas else " ") + "\n"
        tabla_string += f"{ self.__repetir_caracter('-',self.__ancho_tabla)}"

        return tabla_string