# Ejercicio 1
# Calcular la suma de la diagonal principal de una matriz cuadrada (nxn).

matrix_1 = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
    ]

matrix_2 = [
    [2,3,4],
    [2,3,4],
    [2,3,4]
    ]

# ------ EJERCICIO 1 ---------
def suma_diagonal_princ(mat1):
    result = 0
    for i in range(len(mat1)):
        result += mat1[i][i]
    return(result)

# print(suma_diagonal_princ(matrix_1))

# ------ EJERCICIO 2 ---------
# Ejercicio 2
# Calcular la suma de la diagonal secundaria de una matriz cuadrada (nxn).

matrix_2 = [
    [2,3,8],
    [2,3,4],
    [2,3,4]
    ]

def suma_diagonal_sec(mat1):
    result = 0
    for i in range(len(mat1)):
        result += mat1[len(mat1)-1-i][i]
    return(result)

# print(suma_diagonal_sec(matrix_2))

# ------ EJERCICIO 3 ---------
# Ejercicio 3
# Construir una lista donde cada elemento del mismo es la suma de cada fila de una matriz rectangular (nxm)

rect_matrix = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,0,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,0,4,5],
    [1,2,3,4,5]
]

def list_construct(rectangular_matrix):
    result = []
    for i in range(len(rectangular_matrix)):
        result.append(sum(rectangular_matrix[i]))
    return(result)

# print(list_construct(rect_matrix))

# ------ EJERCICIO 4 ---------
# Ejercicio 4
# Calcular la suma de todos los elementos de la matriz.

def sum_elements_in_matrix(mat):
    result = []
    for i in range(len(mat)):
        result.append(sum(mat[i]))
    return(sum(result))

# print(sum_elements_in_matrix(rect_matrix))

# ------ EJERCICIO 5 ---------
# Ejercicio 5
# Calcular la cantidad de elementos iguales a cero de la matriz

def elements_equal_zero(mat):
    result = 0
    for i in range(len(mat)):
        for element in mat[i]:       
            if element == 0:
                result += 1 
    return(result)

# print(elements_equal_zero(rect_matrix))

# ------ EJERCICIO 6 ---------
# Ejercicio 6
# Dada una matriz cuadrada A y un escalar c, construir B = c.A

# A = [n*n] 
# c = ? 
# RESULTADO = B = c * A

matrix_2 = [
    [2,3,8],
    [2,3,4],
    [2,3,4]
    ]

def multiply_matrix(mat, scale):
    result_mat = []
    for i in range(len(mat)):
        row = []
        for element in mat[i]:       
           row.append(element * scale) 
           
        result_mat.append(row)
        
    return(result_mat)

# print(multiply_matrix(matrix_2, 3))

# ------ EJERCICIO 7 ---------
# Ejercicio 7
# Dada una matriz A de nxm y un vector b de m elementos, calcular A.b

# A = matriz rectangular NxM
# vector = M elementos
# Resultado => A * vector

matrix_2 = [
    [2,3,8],
    [2,3,4],
    [2,3,4]
    ]

vector_b = [
    1,
    2,
    3
    ]

def matrix_times_vector(mat, vector):
    result_mat = []
    for i in range(len(mat)): # para cada fila
        result_mat.append(sum(list(x*y for x,y in list(zip(mat[i], vector)))))
    
    return(result_mat)

# print(matrix_times_vector(matrix_2, vector_b))

# ------ EJERCICIO 8 ---------
# Ejercicio 8
# Dadas dos matrices de nxm, construir la matriz suma

matrix_1 = [
    [2,2,2],
    [2,2,2],
    [2,2,2],
    [2,2,2]
    ]

matrix_2 = [
    [2,3,8],
    [2,3,4],
    [2,3,4],
    [2,3,4]
    ]

def sum_matrix(mat1,mat2):
    result = []
    given = list(zip(mat1,mat2))
    
    for i in range(len(given)):
        row = []
        for index in range(len(given[i][0])):    
            row.append(given[i][0][index] + given[i][1][index])      
        result.append(row)
         
    return(result)

# print(sum_matrix(matrix_1, matrix_2))

# ------ EJERCICIO 9 ---------

# Ejercicio 9
# Dadas dos matrices, construir si es posible la matriz producto.
# conciden la n-columnas de la primea con n-filas de la segunda

matrix_1 = [
    [1,2,3],
    [4,5,6]
    ]

matrix_2 = [
    [10,11],
    [20,21],
    [30,31]
    ]

def multiply_matrix(mat1, mat2):

    # GET COLUMNS
    columns = []
    for i in range(len(mat2[0])):
        items = []
        for element in mat2:
            items.append(element[i])
        columns.append(items)

    # MULTIPLY ELEMENTS BY COLUMN ITEMS
    zipped = list(zip(mat1, columns))
    print(f"{zipped=}")

    result = []
    for x,y in zipped:
        row = []
        for i in range(len(x)):
            # print(f"{x[i]=} MULTIPLICADO X {y[i]=}")
            row.append(x[i] * y[i])
            # print(x,y)
        result.append(sum(row))
    print(result)

multiply_matrix(matrix_1,matrix_2)