from calculo_numerico import *

#BISECCION
biseccion_1:float = biseccion(
    funcion="(x-2)**2-math.log(x)",
    limite_inferior=1,
    limite_superior=2,
    error_esperado=0.03
)

biseccion_2:float = biseccion(
    funcion="math.e**x -3 * x**2",
    limite_inferior=0,
    limite_superior=1,
    error_esperado=0.03
)

#NEWTON-RAPHSON
newton_rapshon_1:Tabla = newton_rapshon(
    funcion="(x-2)**2-math.log(x)",
    funcion_derivada="2*(x-2)-(1/x)",
    valor_inicial=1.5,
    error_esperado=0.02
)

newton_rapshon_2:Tabla = newton_rapshon(
    funcion="math.e**x - 3*x**2",
    funcion_derivada="math.e**x - 6*x",
    valor_inicial=0.5,
    error_esperado=0.02
)

#METODO DE RIEMANN
riemann_1:float = riemann(
    funcion="x * math.sqrt((x**2) + 1)",
    limite_inferior=0,
    limite_superior=1,
    intervalos=4
)

riemann_2:float = riemann(
    funcion="3 * x * math.e**(x**2)",
    limite_inferior=0,
    limite_superior=1,
    intervalos=4
)

#METODO DE TRAPECIO
trapecio_1:float = trapecio(
    funcion="x * math.sqrt((x**2) + 1)",
    limite_inferior=0,
    limite_superior=1,
    intervalos=4
)

trapecio_2:float = trapecio(
    funcion="3 * x * math.e**(x**2)",
    limite_inferior=0,
    limite_superior=1,
    intervalos=4
)

#EULER EDO
euler_1:Tabla = euler(
    funcion="y",
    limite_inferior=0,
    limite_superior=1,
    valor_inicial=1,
    intervalos=4,
    funcion_real="math.e**x"
)

euler_2:Tabla = euler(
    funcion="2*x*y",
    limite_inferior=1,
    limite_superior=2,
    valor_inicial=1,
    intervalos=4,
    funcion_real="math.e**((x**2)-1)"
)

#JACOBI
jacobi_1:list[float] = jacobi(
    "(-3*y+z+8)/6",
    "(-2*x-z+7)/4",
    "(x-3*y+7)/5",
    0.2
)

#GAUSS_SEIDEL
gauss_seidel_1:list[float] = gauss_seidel(
    "(-3*y+z+8)/6",
    "(-2*x-z+7)/4",
    "(x-3*y+7)/5",
    0.3
)
