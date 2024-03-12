import math 

def evaluar_funcion(funcion:str, x:float, y:float=0) -> float:
    return eval(funcion)

def se_cumple_valor_intermedio(funcion:str, a:float, b:float) -> bool:
    return evaluar_funcion(funcion,a)*evaluar_funcion(funcion,b) < 0

def calcular_punto_medio(a:float, b:float) -> float:
    return (a+b)/2

def calcular_error_relativo(valor_real:float, valor_aproximado:float) -> float:
    return abs((valor_real-valor_aproximado)/valor_real) if valor_real != 0 else 0

def biseccion(funcion:str, limite_inferior:float, limite_superior:float, error_esperado:float) -> float:
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

def calcular_area_trapecio(base_menor:float, base_mayor:float, altura:float) -> float:
    return((base_menor+base_mayor)*altura)/2

def trapecio(funcion: str, limite_inferior: float, limite_superior:float, intervalos: int) -> float:
    h = calcular_paso(limite_inferior,limite_superior,intervalos)
    acumulador = 0
    x = limite_inferior

    for i in range(intervalos):
        acumulador += calcular_area_trapecio(evaluar_funcion(funcion,x),evaluar_funcion(funcion,x+h),h)
        x = limite_inferior + (i + 1) * h
    
    return acumulador

def euler(funcion:str, limite_inferior:float, limite_superior:float, intervalos:int, valor_inicial:float) -> float:
    h = calcular_paso(limite_inferior,limite_superior,intervalos)
    y_anterior = valor_inicial
    
    for i in range(intervalos+1):
        t = h * i + limite_inferior
        y = y_anterior + h * evaluar_funcion(funcion,t,y_anterior) if i !=0 else valor_inicial
        print(f"{i} | {t} | {y}")
        y_anterior = y

def main():
    #print(biseccion("math.pow(math.e,-x)-math.log(x)",1,1.5,1))
    #print(riemann("3 * x * math.pow(math.e,x**2)",0,1,4))
    #print(riemann("x * math.sqrt(x**2 +1)",0,1,4))
    #print(trapecio("math.pow(math.e,x**2)",0,1,5))
    euler("2*x*y",1,2,4,1)

if __name__ == "__main__":
    main()