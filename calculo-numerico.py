from tabla import *
import math

#Las funciones se deben de escribir en formato de codigo de Python, en terminos de x e y
def evaluar_funcion(funcion:str, x:float, y:float=0) -> float:
    return eval(funcion)

def calcular_error_relativo(valor_real:float, valor_aproximado:float) -> float:
    return abs((valor_real-valor_aproximado)/valor_real) if valor_real != 0 else 0

def biseccion(funcion:str, limite_inferior:float, limite_superior:float, error_esperado:float) -> float:
    def se_cumple_valor_intermedio(funcion:str, a:float, b:float) -> bool:
        return evaluar_funcion(funcion,a)*evaluar_funcion(funcion,b) < 0

    def calcular_punto_medio(a:float, b:float) -> float:
        return (a+b)/2

    m_actual = calcular_punto_medio(limite_inferior,limite_superior)
    m_previo = 0
    i = 1
    error_aproximado = 100
    a = limite_inferior
    b= limite_superior

    if se_cumple_valor_intermedio(funcion,limite_inferior,limite_superior):
        while(i < 100 and error_aproximado > error_esperado):
            m_previo = m_actual
            m_actual = calcular_punto_medio(a,b)

            if evaluar_funcion(funcion,m_actual) * evaluar_funcion(funcion,b) < 0:
                a = m_actual
            else:
                b = m_actual
            
            if i > 1:
                error_aproximado = calcular_error_relativo(m_previo,m_actual)*100

            i = i + 1
            
    return m_actual

def newton_rapshon(funcion:str, funcion_derivada:str, valor_inicial:float, error_esperado:float) -> float:
    error_actual = 100
    x_anterior = valor_inicial

    tabla_resultado = Tabla(["Aprox. a la raiz","Error aprox."])
    tabla_resultado.agregar_fila([x_anterior,""])

    while(error_esperado < error_actual):
        i = x_anterior
        x = i - (evaluar_funcion(funcion,i)/evaluar_funcion(funcion_derivada,i))
        error_actual = calcular_error_relativo(x,x_anterior) * 100
        tabla_resultado.agregar_fila([x,f"{error_actual}%"])
        x_anterior = x  
    return tabla_resultado.obtener_string()

def calcular_paso(limite_inferior:float, limite_superior:float, intervalos: int) -> float:
    return (limite_superior-limite_inferior)/intervalos

def riemann(funcion:str, limite_inferior:float, limite_superior:float, intervalos:int) -> float:
    h = calcular_paso(limite_inferior,limite_superior,intervalos)
    acumulador = 0
    x = limite_inferior

    for i in range(intervalos):
        acumulador += evaluar_funcion(funcion,x) * h
        x = limite_inferior + (i + 1) * h
    
    return acumulador

def trapecio(funcion: str, limite_inferior: float, limite_superior:float, intervalos: int) -> float:
    def calcular_area_trapecio(base_menor:float, base_mayor:float, altura:float) -> float:
        return((base_menor+base_mayor)*altura)/2

    h = calcular_paso(limite_inferior,limite_superior,intervalos)
    acumulador = 0
    x = limite_inferior

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

    y_anterior = valor_inicial
    indices= ["i","t","y"] if funcion_real is None else ["i","t","y","Zi","Er"]
    tabla_resultado = Tabla(indices)
        

    for i in range(intervalos+1):
        t = h * i + limite_inferior
        y = y_anterior + h * evaluar_funcion(funcion,t,y_anterior) if i !=0 else valor_inicial
        
        if funcion_real is not None:
            z = evaluar_funcion(funcion_real,t,y_anterior)
            error = calcular_error_relativo(z,y)
        
        fila = [i,t,y] if funcion_real is None else [i,t,y,z,error]
        tabla_resultado.agregar_fila(fila)
        y_anterior = y
    
    return tabla_resultado