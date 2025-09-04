'''Faça um programa em Python e salve o arquivo na extensão .py que simule 
uma pequena calculadora: - O programa deve pedir dois números ao usuário. - Depois, deve pedir a operação desejada (+, -, *, /). - As operações devem ser implementadas em funções (ex: funcao soma, subtracao, 
multiplicacao e divisao). - Trate os seguintes casos usando try/except/else/finally: 
1. Se o usuário digitar algo que não seja número → mostrar "Erro: valor inválido". 
2. Se o usuário escolher "/" e o denominador for zero → mostrar "Erro: divisão por zero". 
3. Se o usuário escolher uma operação inválida → mostrar "Erro: operação inválida". 
4. Caso contrário → mostrar o resultado chamando a função correspondente. - No final, use o bloco finally para exibir a mensagem "Fim do programa".'''


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


def main():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        
        operacao = input("Qual operação deseja realizar? (+, -, *, /): ")
        
        if operacao == '+':
            resultado = soma(n1, n2)
        elif operacao == '-':
            resultado = subtracao(n1, n2)
        elif operacao == '*':
            resultado = multiplicacao(n1, n2)
        elif operacao == '/':
            if n2 == 0:
                raise ZeroDivisionError 
            resultado = divisao(n1, n2)
        else:
            raise ValueError("Operação inválida")
    
    except ValueError as e:
        if "could not convert" in str(e):
            print("Erro: valor inválido")
        else:
            print("Erro: operação inválida")
    
    except ZeroDivisionError:
        print("Erro: divisão por zero")
    
    else:
        print(f"Resultado: {resultado}")
    
    finally:
        print("Fim do programa")


if __name__ == "__main__":
    main()

