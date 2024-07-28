n = int(input('введите п строк '))
m = int(input('введите m столбцов '))
v= int(input ('введите v значение   '))
if n <=0:
    print('Неверное кол-во строк ', n, 'Матрица пуста')
elif m <= 0:
    print('Неверное ко-во стсолбцов ', m, 'Матрица пуста')
def get_matrix(n,m,v):
    matrix = []
    for i in range (n):
        matrix.append([])
        for j in range(m):
               matrix[i].append(v)
    print(matrix)
    return matrix
matrix = get_matrix(n,m,v)

