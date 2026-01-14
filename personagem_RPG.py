#Tipagem da barra de progresso
full_dot = '●'
empty_dot = '○'
def criacao_personagem():
    while True:
        primeiro_nome = input("Qual o nome do seu personagem? ").strip()
        segundo_nome = input("Qual o sobrenome do seu personagem? ").strip()
        if primeiro_nome == "" or segundo_nome == "":
            questao = input("Você não acha que ele merece um nome? (s/n): ").lower()
            if questao in ['não', 'n', 'nao']:
                print("Ok, quando decidir um nome estarei pronto. :)")
                return None
            continue
        if not primeiro_nome.isalpha() or not segundo_nome.isalpha():
            print("Digite apenas letras para o nome do seu personagem.")
            continue
        if len(primeiro_nome) > 10 or len(segundo_nome) > 10:
            print("Nome muito longo (máximo 10 caracteres).")
            continue
        try:
            print("\n--- Atributos (0 a 10) ---")
            forca = int(input('Qual a força? '))
            magia = int(input('Qual a magia? ')) 
            inteligencia = int(input('Qual a inteligência? '))  
            carisma = int(input('Qual o carisma? '))
            #Validacao atributos
            if not (0 <= forca <= 10 and 0 <= magia <= 10 and 0 <= inteligencia <= 10 and 0 <= carisma <= 10):
                print('Escolha apenas números entre 0 e 10.')
                continue
        except ValueError:
            print('Digite apenas números inteiros para os atributos.')
            continue
        #Montagem da ficha
        forca_line = "FORÇA         " + full_dot * forca + empty_dot * (10 - forca)
        magia_line = "MAGIA         " + full_dot * magia + empty_dot * (10 - magia)
        inteligencia_line = "INTELIGENCIA  " + full_dot * inteligencia + empty_dot * (10 - inteligencia)
        carisma_line = "CARISMA       " + full_dot * carisma + empty_dot * (10 - carisma)
        return f"\nSEU PERSONAGEM:\n{primeiro_nome} {segundo_nome}\n{forca_line}\n{magia_line}\n{inteligencia_line}\n{carisma_line}"
#Loop Principal
while True:
    resultado = criacao_personagem()
    if resultado:
        print(resultado)
    finalizacao = input("Você deseja criar outro personagem?: ")
    if finalizacao in ['não', 'n', 'nao']:

        break
