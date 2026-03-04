# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44
straniza = 100
stroka = 50
sumbol = 25
v = 4
V_knigi = straniza * stroka * sumbol * v / 1024**2
N = V / V_knigi



print("Количество книг, помещающихся на дискету:",round(N))


