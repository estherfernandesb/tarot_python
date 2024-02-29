import random
# import sys 
# sys.stdout.reconfigure(encoding='utf-8')

print("****************************************")
print("Seja bem vinde a tiragem de Tarot em CMD")
print("****************************************")

# Função para ler as cartas
def ler_cartas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            cartas = file.readlines()
            return [carta.strip().split(': ') for carta in cartas]
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []

# Função para sortear uma carta aleatoriamente
def sortear_carta(cartas):
    if cartas:
        return random.choice(cartas)
    else:
        return ("", "Não há cartas disponíveis.")

# Função principal
def main():
    nome_arquivo = 'cartas_tarot.txt'
    cartas = ler_cartas(nome_arquivo)

    if cartas:
        input("Pressione Enter para tirar uma carta de tarô...")
        carta_tirada, descricao = sortear_carta(cartas)
        print(f"A carta de tarô tirada é: {carta_tirada}")
        print(f"Descrição: {descricao}")
    else:
        print("Não foi possível tirar uma carta de tarô.")

if __name__ == "__main__":
    main()