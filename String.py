# colentando String
palavra = str(input("Digite uma palavra: "))
tamanho = len(palavra)

# imprimindo ela ao contrario
print(f'A palavra "{palavra}" escrita ao contrario fica: ', end='')
for i in range(0, tamanho, 1):
    print(palavra[tamanho - 1 - i], end='')
