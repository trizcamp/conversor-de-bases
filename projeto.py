import os
os.system('cls')
print("[DECODIFICADOR BINARIO | HEXADECIMAL | DECIMAL | OCTAL]\n")

try: 
    opt = int(input("Escolha a conversão desejada:\n [1] BINARIO PARA AS DEMAIS BASES\n [2] SOBRE\n [0] SAIR\n Sua opção: "))
    if opt == 0:
            exit()
    if opt == 2:
        print("Curso: [Analise e Desenvolvimento De Sistemas]\n")
        print("Componentes do grupo: [Victor Hugo - Leonardo Zuzi - Beatriz Felix - Fabricio Nunes - Guilherme Guimarães - Leandro Lumes]\n")
        print("Disciplinas envolvidas: [Programação de Computadores - Organização e Arquitetura de Computadores]\n")
        print("[Versão do aplicativo: 1.0]")
        exit()
    num = (input("\nDigite o numero binario para conversão: "))
    opt2 = int(input("\nEscolha a conversão final desejada:\n [1] HEXADECIMAL\n [2] DECIMAL\n [3] OCTAL\n Sua opção: "))
#MENSAGEM DE ERRO CASO NÃO SEJA UM NUMERO BINARIO
except ValueError:
    print("[ERRO] Digite apenas números e não letras. Tente novamente.\n")
    exit()
os.system('cls')

#MENSAGEM DE ERRO CASO NÃO SEJA UM NUMERO BINARIO
if not str(num).isdigit() or not all(z in "01" for z in str(num)):
    print("[ERRO] O valor inserido não é um número binário válido. Tente novamente.\n")
    exit() 
#BINARIO PARA DECIMAL
if opt == 1 and opt2 == 2:
    decimal = 0
    n = len(num) - 1
    for d in num:
        decimal += int(d) * 2 ** n 
        n -= 1
    print("[ Sua conversão foi realizada com sucesso. ]\n")
    print(f"O numero ({num})2 para decimal é ({decimal})10")
#BINARIO PARA OCTAL
elif opt == 1 and opt2 == 3:
    decimal = 0
    x = 0
    binario = int(num)
    while binario != 0:
        decs = binario % 10
        decimal += decs * pow(2, x)
        binario //= 10
        x += 1
    octal = 0
    y = 1
    while decimal != 0:
        octal += (decimal % 8) * y
        decimal //= 8
        y *= 10
    print("[ Sua Conversão realizada com sucesso. ]\n")
    print(f"O número binário ({num})2 convertido para octal é ({octal})8")
#BINARIO PARA HEXA-DECIMAL
elif opt == 1 and opt2 == 1:
    decimall = 0
    finalhexx = num 
    for digito in num:
        decimall = decimall * 2 + int(digito)
    hex_tabela = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ""
    while decimall > 0:
        resto = decimall % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = hex_tabela[resto] + hexadecimal
        decimall = decimall // 16
    print("[ Sua conversão foi realizada com sucesso. ]\n")
    print(f"O numero ({finalhexx})2 para hexa-decimal é ({hexadecimal})16")
#MENSSAGEM DE ERRO
else:
    print("[ERRO] Opção de conversão inválida. Tente novamente.\n")