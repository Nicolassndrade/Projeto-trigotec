import math

def calcular_trigonometria(angulo):

    radianos = math.radians(angulo)

    seno = math.sin(radianos)
    cosseno = math.cos(radianos)
    tangente = math.tan(radianos)

    return seno, cosseno, tangente

def teorema_de_pitagoras(cateto1, cateto2):

    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    
    return hipotenusa

def menu():
    
    print("\nEscolha uma opção:")
    print("[1]- Calcular seno, cosseno e tangente")
    print("[2]- Calcular o Teorema de Pitágoras")
    print("[0]- Sair")

while True:
    menu()
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        angulo = float(input("Digite o ângulo em graus: "))
        seno, cosseno, tangente = calcular_trigonometria(angulo)

        print(f"Seno: {seno:.4f}")
        print(f"Cosseno: {cosseno:.4f}")
        print(f"Tangente: {tangente:.4f}")
    
    elif opcao == "2":
       
        cateto1 = float(input("Digite o valor do primeiro cateto: "))
        cateto2 = float(input("Digite o valor do segundo cateto: "))

       
        hipotenusa = teorema_de_pitagoras(cateto1, cateto2)

        print(f"A hipotenusa é: {hipotenusa:.4f}")
    
    elif opcao == "0":
        print("Saindo...")
        break
    
    else:
        print("\nOpção inválida! Por favor, selecione uma das opções disponíveis (1, 2 ou 0).")
