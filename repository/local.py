words = [
    ('isquiotibial', 'Es un músculo', 'Se encuentra en el tren inferior','Facilita la extensión de la pierna',1),
    ('meditar', 'produce un estado de relajamiento', 'Contribuye al bienestar físico','Interviene la mente y el cuerpo',1),
    ('arena', 'conjunto de fracmentos sueltos de roca', 'la particula individual se llama grano','se encuentran en las costas',1),
    ('dormir', 'Se puede hacer parado', 'Se puede hacer en la cama','es uno de los placeres de la vida',1),
]

#print(words[0])

a = [1,2,3,4,5]
b =  list()

b = a.copy()

print(a)
print(b)

a[0] = 0

print(a)
print(b)

print(a is b)