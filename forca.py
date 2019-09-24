import random

def jogar():
    print("*************************************")
    print("*******Que comece os jogos **********")
    print("*************************************")

    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    palavrasecreta = random.choice(palavras)

    letras_acertadas = ["_" for x in palavrasecreta]

    i=0
    while i <= 5:
        print(letras_acertadas)
        chute = input("Qual a letra?\n").strip().lower()
        
        index = 0
        for j in palavrasecreta:
            if(j.lower() == chute.lower()):
                letras_acertadas[index] = j
            index +=1    
        
        
        print(letras_acertadas)
        if("_" not in letras_acertadas):
            print("Parabéns você acertou")
            break

        sabe_a_palavra = input("Você já sabe a palavra? Entre com SIM e NÃO\n")
        if(sabe_a_palavra.lower() == "sim"):
            palavradousuario = input("Entre com a palavra:\n").lower()
            if(palavradousuario.lower() == str(palavrasecreta.lower())):
                print("Parabéns você acertou")
                print("       ___________      ")
                print("      '._==_==_=_.'     ")
                print("      .-\\:      /-.    ")
                print("     | (|:.     |) |    ")
                print("      '-|:.     |-'     ")
                print("        \\::.    /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("        '-------'       ")
                break
            else:
                print("Você errou! Você possui mais {}".format(4-i) + " chances")
        i+=1
        
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar() 