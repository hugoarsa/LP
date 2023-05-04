def f(x):
    print(x)
    x = x - 1
    print(x)

a = 3
print(a)
f(a)
#pasamos por valor o por referencia -> aparenta valor (no cambia) pero es por referencia ¯\_(ツ)_/¯
#pasa un puntero, pero pasa el puntero por valor (pasando referencias por valor)
print(a)

def g(y):
    print(y)
    y.pop() # si fuese y = [1,2] seria como el anterior, porque no modificas sino reasignas, entonces se pierde
    print(y)

b = [1,2,3]
print(b)
g(b)
print(b)

#todos los objetos son referencias a ellos mismos

#otro ejemplo de aliasing y referencias

fila = [0,0,0]

mat = [fila,fila,fila] # [fila]*3 or [fila for i in range(3)]
# para evitar aliasing declarar asi [ [0,0,0] for i in range(3)]

print(mat)
print(fila)

mat[0][0] = 99

print(mat)
print(fila)


fila[0] = 22

print(mat)
print(fila)

fila = [7,7,7] #ahora aqui estoy perdiendo la referencia original de fila, la fila original estara en mat[0] !!!

print(mat)
print(fila)

fila = mat[0][0]

print(mat)
print(fila)

list(map(lambda x: x + 2, [1,2,3]))
def h(z): return 2*z
list(map(h,[1,2,3]))

#tmb tenemos un filter, reduce (fold)