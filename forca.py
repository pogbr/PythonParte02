def jogar(palavrasecreta):
    print("*************************************")
    print("*******Que comece os jogos **********")
    print("*************************************")

    letras_acertadas = ["_","_","_","_","_","_"]
    i=0
    while i <= 5:
        print(letras_acertadas)
        chute = input("Qual a letra?\n").strip().lower()
        
        index = 0
        for j in palavrasecreta:
            if(j == chute):
                letras_acertadas[index] = j
            index +=1    
        
        print(letras_acertadas)

        sabe_a_palavra = input("Você já sabe a palavra? Entre com SIM e NÃO\n")
        if(sabe_a_palavra.lower() == "sim"):
            palavradousuario = input("Entre com a palavra:\n").lower()
            if(palavradousuario == str(palavrasecreta)):
                print("Parabéns você acertou")
                break
            else:
                print("Você errou! Você possui mais {}".format(4-i) + " chances")
        i+=1
        
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar("banana") 