with open('D:/Gaby/Informatica/fisiere in python/nume_in.txt', 'r') as f:
    nume=f.readline()
with open('D:/Gaby/Informatica/fisiere in python/nume_out.txt', 'w') as f:
    f.write(f'Hello, {nume}!\n')
    f.write(f'Hallo, {nume}!\n')
    f.write(f'Hola, {nume}!\n')