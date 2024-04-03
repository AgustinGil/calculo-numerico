from tabla import *
import math 

#Las funciones se deben de escribir en formato de codigo de Python, en terminos de x,y,z
def evaluar_funcion(funcion:str, x:float=0, y:float=0, z:float=0) -> float:
    return eval(funcion)

def calcular_error_relativo(valor_real:float, valor_aproximado:float) -> float:
    return abs((valor_real-valor_aproximado)/valor_real) if valor_real != 0 else 0

def biseccion(funcion:str, limite_inferior:float, limite_superior:float, error_esperado:float) -> float:
    def se_cumple_valor_intermedio(funcion:str, a:float, b:float) -> bool:
        return evaluar_funcion(funcion,a)*evaluar_funcion(funcion,b) < 0

    def calcular_punto_medio(a:float, b:float) -> float:
        return (a+b)/2
    
    m_actual:float = calcular_punto_medio(limite_inferior,limite_superior)
    m_previo:float = 0
    i:int = 1
    error_aproximado:float = 1
    a:float = limite_inferior
    b:float = limite_superior
    if se_cumple_valor_intermedio(funcion,limite_inferior,limite_superior):
        while(i < 100 and error_aproximado > error_esperado):
            m_previo = m_actual
            m_actual = calcular_punto_medio(a,b)

            if evaluar_funcion(funcion,m_actual) * evaluar_funcion(funcion,b) < 0:
                a = m_actual
            else:
                b = m_actual
            
            if i > 1:
                error_aproximado = calcular_error_relativo(m_previo,m_actual)

            i = i + 1
            
    return m_actual

def newton_rapshon(funcion:str, funcion_derivada:str, valor_inicial:float, error_esperado:float) -> float:
    error_actual:float = 1
    x_anterior:float = valor_inicial

    tabla_resultado:Tabla = Tabla(["Aprox. a la raiz","Error aprox."])
    tabla_resultado.agregar_fila([x_anterior,""])

    while(error_esperado < error_actual):
        i:float = x_anterior
        x:float = i - (evaluar_funcion(funcion,i)/evaluar_funcion(funcion_derivada,i))
        error_actual:float = calcular_error_relativo(x,x_anterior) 
        tabla_resultado.agregar_fila([x,f"{error_actual}"])
        x_anterior = x  
    return tabla_resultado

def calcular_paso(limite_inferior:float, limite_superior:float, intervalos: int) -> float:
    return (limite_superior-limite_inferior)/intervalos

def riemann(funcion:str, limite_inferior:float, limite_superior:float, intervalos:int) -> float:
    h:float = calcular_paso(limite_inferior,limite_superior,intervalos)
    acumulador:float = 0
    x:float = limite_inferior

    for i in range(intervalos):
        acumulador += evaluar_funcion(funcion,x) * h
        x = limite_inferior + (i + 1) * h
    
    return acumulador

def trapecio(funcion: str, limite_inferior: float, limite_superior:float, intervalos: int) -> float:
    def calcular_area_trapecio(base_menor:float, base_mayor:float, altura:float) -> float:
        return((base_menor+base_mayor)*altura)/2

    h:float = calcular_paso(limite_inferior,limite_superior,intervalos)
    acumulador:float = 0
    x:float = limite_inferior

    for i in range(intervalos):
        acumulador += calcular_area_trapecio(evaluar_funcion(funcion,x),evaluar_funcion(funcion,x+h),h)
        x = limite_inferior + (i + 1) * h
    
    return acumulador

def euler(funcion:str, limite_inferior:float, limite_superior:float, valor_inicial:float, intervalos:int=None, paso:float=None,funcion_real:str=None) -> list:
    if paso is None and intervalos is None:
        raise ValueError('Debes ingresar un valor de intervalo o de paso')
    elif paso is not None and intervalos is not None:
        raise ValueError('No puedes ingresar paso e intervalos, solo uno de ellos')
    else:
        h = calcular_paso(limite_inferior,limite_superior,intervalos) if paso is None else paso
        intervalos = intervalos if intervalos is not None else round((limite_superior-limite_inferior)/h)

    y_anterior:float = valor_inicial
    t_anterior:float = limite_inferior
    indices:list[str] = ["i","t","y"] if funcion_real is None else ["i","t","y","Zi","Er"]
    tabla_resultado:Tabla = Tabla(indices)

    for i in range(intervalos+1):
        t:float = h * i + limite_inferior
        y:float = y_anterior + h * evaluar_funcion(funcion,t_anterior,y_anterior) if i !=0 else valor_inicial
        
        if funcion_real is not None:
            z:float = evaluar_funcion(funcion_real,t,y_anterior)
            error:float = calcular_error_relativo(z,y)
        
        fila:list[float] = [i,t,y] if funcion_real is None else [i,t,y,z,error]
        tabla_resultado.agregar_fila(fila)
        y_anterior = y
        t_anterior = t
    
    return tabla_resultado

def calcular_error_vectores(vector_1 : list[float],vector_2: list[float]) -> float:
    if vector_1 == [0,0,0] or vector_2 == [0,0,0]:
        return 1
    
    vector_aux:list[float] = []
    for i in range(len(vector_1)):
        vector_aux.append(abs(vector_2[i]-vector_1[i]))
    return max(vector_aux) / max(vector_2) 

def jacobi(funcion_x : str,funcion_y:str, funcion_z: str, error : float) -> list[float]:
    error_relativo: float = 1
    vector_actual: list[float] = [0,0,0]
    while(error_relativo > error):
        x: float = evaluar_funcion(funcion_x,vector_actual[0],vector_actual[1],vector_actual[2])
        y: float = evaluar_funcion(funcion_y,vector_actual[0],vector_actual[1],vector_actual[2])
        z: float = evaluar_funcion(funcion_z,vector_actual[0],vector_actual[1],vector_actual[2])
        vector_anterior: list[float] = vector_actual
        vector_actual: list[float] = [x,y,z]
        error_relativo: float = calcular_error_vectores(vector_actual,vector_anterior)        
    return vector_actual

def gauss_seidel(funcion_x : str,funcion_y:str, funcion_z: str, error : float) -> list[float]:
    error_relativo: float = 1
    vector_actual: list[float] = [0,0,0]
    while(error_relativo > error):
        x: float = evaluar_funcion(funcion_x,vector_actual[0],vector_actual[1],vector_actual[2])
        y: float = evaluar_funcion(funcion_y,x,vector_actual[1],vector_actual[2])
        z: float = evaluar_funcion(funcion_z,x,y,vector_actual[2])
        vector_anterior: list[float] = vector_actual
        vector_actual: list[float] = [x,y,z]
        error_relativo: float = calcular_error_vectores(vector_actual,vector_anterior)
    return vector_actual