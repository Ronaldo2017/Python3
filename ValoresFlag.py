n = s = total = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    s += n
    total += 1
print(f'Foram digitados {total} e a soma foi de: {s}')
