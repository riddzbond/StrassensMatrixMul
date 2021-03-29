def print_matrix(m, n):  # Printing Input Matrix
    for i in range(n):
        for j in range(n):
            print(m[i][j], end=' ')
        print()
    print()

def print_matrix2(m, n): # Printing Output Matrix
    for j in range(n):
        for i in range(n):
            print(m[i][j], end=' ')
        print()
    print()

def input_matrix(m, n): # Taking Matrix Input
    print('Enter matrix:')
    for i in range(n):
        for j in range(n):
            m[i][j] = int(input(f'Enter element [{i+1},{j+1}]: '))
    print()

def mat_add(a,b):   # Add 2 Matrices
    n = len(a)
    c = []
    if(n == 1):
        x1 = a[0][0]
        y1 = b[0][0]
        res = x1+y1
        e = []
        e.append(0)
        c.append(e)
        c[0][0] = res
        return c
    

    for k in range(n): 
        e =[]
        for m in range(n):
            e.append(0)
        c.append(e)

    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    # print(c)
    return c

def mat_sub(a,b): # Sub 2 Matrices
    n = len(a)
    c = []
    if(n == 1):
        x1 = a[0][0]
        y1 = b[0][0]
        res = x1-y1
        e = []
        e.append(0)
        c.append(e)
        c[0][0] = res
        return c

    

    for k in range(n): 
        e =[]
        for m in range(n):
            e.append(0)
        c.append(e)

    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]

    return c
  
def split(matrix): # Splitting the Matrix
    y = 0
    z = 0
    a = [];
    b = [];
    c = [];
    d = [];
    n = len(matrix)
    n2 = n//2
  
    for k in range(n2): 
        e = []
        for m in range(n2):
            e.append(0)
        a.append(e)

    for k in range(n2): 
        e = []
        for m in range(n2):
            e.append(0)
        b.append(e)

    for k in range(n2): 
        e = []
        for m in range(n2):
            e.append(0)
        c.append(e)

    for k in range(n2): 
        e = []
        for m in range(n2):
            e.append(0)
        d.append(e)

    y = z = 0
    for i in range(0,n2):
        for j in range(0,n2):
            a[y][z] = matrix[i][j]
            z =+ 1
        z = 0
        y =+ 1

    y = z = 0
    for i in range(0,n2):
        for j in range(n2,n):
            b[y][z] = matrix[i][j]
            z =+ 1
        z = 0
        y =+ 1

    y = z = 0
    for i in range(n2,n):
        for j in range(0,n2):
            c[y][z] = matrix[i][j]
            z =+ 1
        z = 0
        y =+ 1

    y = z = 0
    for i in range(n2,n):
        for j in range(n2,n):
            d[y][z] = matrix[i][j]
            z =+ 1
        z = 0
        y =+ 1

    return a,b,c,d

def combine1(c11, c12, c21, c22): # Combining Ouput
    n = len(c11)
    n2 = n * 2
    c = [] 
    

    for k in range(n2): 
        e = []
        for m in range(n2):
            e.append(0)
        c.append(e)

    y = z = 0
    for i in range(0, n):
        for j in range(0, n):
            c[i][j] = c11[y][z]
            z =+ 1
        z = 0
        y =+ 1

    y = z = 0
    for i in range(n,n2):
        for j in range(0, n):
            c[i][j] = c12[y][z]
            z =+ 1
        z = 0
        y =+ 1

    y = z = 0
    for i in range(0, n):
        for j in range(n, n2):
            c[i][j] = c21[y][z]
            z =+ 1
        z = 0
        y =+ 1

    y = z = 0
    for i in range(n, n2):
        for j in range(n, n2):
            c[i][j] = c22[y][z]
            z =+ 1
        z = 0
        y =+ 1
    
    return c




def strassen(x, y): # Applying Strassen's Algorithm
    num = len(x)
    
    
    if num == 1:
        c = []
        x1 = int(x[0][0])
        y1 = int(y[0][0])
        e = []
        e.append(0)
        c.append(e)
        c[0][0] = x1 * y1
        return c
  
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    p1 = strassen(a, mat_sub(f,h))              # p1 = strassen(a, f - h)  
    p2 = strassen(mat_add(a,b), h)              # p2 = strassen(a + b, h)        
    p3 = strassen(mat_add(c,d), e)              # p3 = strassen(c + d, e)        
    p4 = strassen(d, mat_sub(g,e))              # p4 = strassen(d, g - e)        
    p5 = strassen(mat_add(a,d), mat_add(e,h))   # p5 = strassen(a + d, e + h)        
    p6 = strassen(mat_sub(b,d), mat_add(g,h))   # p6 = strassen(b - d, g + h) 
    p7 = strassen(mat_sub(a,c), mat_add(e, f))  # p7 = strassen(a - c, e + f)
  
    
    r = mat_add(mat_sub(mat_add(p5,p4),p2),p6)        # r = p5 + p4 - p2 + p6  
    s = mat_add(p1,p2)                                # s = p1 + p2           
    t = mat_add(p3,p4)                                # t = p3 + p4            
    u = mat_sub(mat_sub(mat_add(p1,p5),p3),p7)        # u = p1 + p5 - p3 - p7  
    
    # print(combine1(c11,c12,c21,c22))
    return combine1(r,s,t,u)



# Driving Code
num = int(input('Enter size of matrix: '))
m1 = []
m2 = []

for k in range(num): 
        e =[]
        for m in range(num):
            e.append(0)
        m1.append(e)

for k in range(num): 
        e =[]
        for m in range(num):
            e.append(0)
        m2.append(e)

input_matrix(m1,num)
input_matrix(m2,num)

print_matrix(m1, num)
print_matrix(m2, num)

output = strassen(m1,m2)

print_matrix2(output, num)


# m1 = [[2, 6, 3, 7], 
#       [3, 1, 2, 9], 
#       [4, 3, 2, 1], 
#       [6, 7, 8, 9]]

# m2 = [[4, 5, 2, 1], 
#       [6, 2, 8, 1], 
#       [5, 2, 8, 9], 
#       [9, 2, 1, 4]]
