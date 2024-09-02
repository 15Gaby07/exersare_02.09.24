with open('D:/Gaby/Informatica/fisiere in python/tabla_înmilțirii_in.txt', 'r') as f:
    numar=int(f.readline())

with open('D:/Gaby/Informatica/fisiere in python/tabla_înmilțirii_out.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f'{numar} x {i} = {numar * i}\n')
