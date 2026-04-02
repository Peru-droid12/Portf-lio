# Gerador de Senhas Seguras
# Feito por Pedro
# Gera senhas aleatórias com tamanho definido pelo usuário

import random
import string

def criar_senha(tamanho):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    todos = letras + numeros + simbolos

    senha_final = ''.join(random.choice(todos) for _ in range(tamanho))
    return senha_final

def iniciar():
    print("🔐 GERADOR DE SENHAS DO PEDRO 🔐")

    while True:
        try:
            tamanho = int(input("\nQuantos caracteres você quer na senha? (mín 6): "))

            if tamanho < 6:
                print("❌ Muito curto! Coloca pelo menos 6.")
                continue

            break

        except:
            print("⚠️ Digita um número válido aí.")

    print("\nGerando senha... ⏳")

    senha = criar_senha(tamanho)

    print(f"\n✅ Sua senha: {senha}")
    print(f"📏 Total de caracteres: {len(senha)}")

if __name__ == "__main__":
    iniciar()