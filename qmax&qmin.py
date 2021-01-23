def qmin(m, l, v, k, male):
    if male == True:
        return round((10*m + 6.25*l - 5*v + 5) * k, 3)
    else:
        return round((10*m + 6.25*l - 5*v - 161) * k, 3)


def qmax(m, l, v, k, male):
    if male == True:
        return round((13.397*m + 4.799*l - 5.677*v + 88.362) * k, 3)
    else:
        return round((9.247*m + 3.098*l - 4.330*v + 447.593) * k, 3)

m = 60
l = 170
v = 20
k = 1.375
male = True

print (qmin(m, l, v, k, male))
print (qmax(m, l, v, k, male))