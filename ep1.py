# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Caroline Chaim, carolineclc@al.insper.edu.br
# - aluno B: Giovanna Campedelli, giovannahc@al.insper.edu.br


#dicionário de salas
import random
import json

with open ("cenario.json", 'r',encoding='utf8') as arquivo:
    cenarios = json.load(arquivo)
        
    
#lista inventário
    



def main():
    nome_cenario_atual = "inicio"
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

#    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    ganhou = False
    vidaP1 = 10
    ataqueagilidade = 0
    ataquelivrao = 0 
    inventario = []
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print()
        print()
        print (cenario_atual["titulo"])
        print ("-" * len(cenario_atual["titulo"]))
        print (cenario_atual["descricao"])



        if "opcoes" in cenario_atual:
            opcoes = cenario_atual['opcoes']
            
            if len(opcoes) == 0:
                print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                game_over = True
            elif nome_cenario_atual == "teletransporte":
                print()
                print("Suas escolhas são: ")
                print ()
                for e, desc in opcoes.items():
                    print(" -> {0}: {1} \n".format(e, desc))
                print()
                escolha = input("Para onde você deseja ir?: ")
                if escolha not in cenarios:
                    print ()
                    print("Sua indecisão foi sua ruína!")
                    game_over = True
                nome_cenario_atual = escolha
            
            else:
                print()
                print("Suas escolhas são: ")
                print ()
                for e, desc in opcoes.items():
                    print(" -> {0}: {1} \n".format(e, desc))
                print()
                escolha = input("Para onde você deseja ir?: ")
                    
    
                if escolha in opcoes or escolha == "vida" or escolha == "teletransporte":
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True
                    
         #sala para o teletransporte
           
        elif nome_cenario_atual == "sala 213":
            if "chave segundo andar"in inventario:
                    print ()
                    print ("Parabens! Voce tem acesso à sala de teletransporte")
                    print ("Sempre que digitar: teletransporte, consiguira escolher seu destino")
                    nome_cenario_atual = cenario_atual["destino"]
            else:
                    print ()
                    print ("Voce nao tem acesso a essa sala. Tente pegar uma chave")
                    nome_cenario_atual = cenario_atual ["destino1"]
                     
                    
        else:
            #vida com livro
            if nome_cenario_atual == "pegar livro":
                print("Voce esta aprendendo, ganhou +10 de vida!")
                vidaP1 = vidaP1 + 10
                print ("Suas vidas: {0}".format(vidaP1))
            #vida mostrador
            elif nome_cenario_atual == "vida":
                print ("Você possui {0} vidas".format(vidaP1))
            #vida com conversa
            elif nome_cenario_atual == "conversar":
                print ("Depois de uma longa discussão sobre arquivos JSON, você ganhou +15 de vida")
                vidaP1 = vidaP1 + 15
                print ("Suas vidas: {0}".format(vidaP1))
            #vida com  milagre
            elif nome_cenario_atual == "beber mais": 
                print ()
                print ("Voce bebeu até receber um milagre. Ganhou mais 20 de vida")
                vidaP1 += 20
            #dica jovem
            elif nome_cenario_atual == "jovem":
                Pergunta = input("Voce quer pagar uma cerveja para seu veterano?")
                if Pergunta == "sim":
                    print ()
                    print ("Depois de ter pagado cerveja para o seu veterano com 5 das duas vidas, ele te deu um papel misterioso contendo dicas para o EP:" )
                    print ()
                    print ("Converse com alguem no quarto andar e ganhe a luta contra o ninja; e tera mais chances quando for falar com o professor ")
                    vidaP1 -= 5
                else:
                     print()
                     nome_cenario_atual = cenario_atual["destino"]
                    
            #sala terceiro andar
            elif nome_cenario_atual == "sala virtual":
                if "chave misteriosa" in inventario:
                    print ()
                    print ("Seu veterano, ao inves de te atacar, sentiu pena do seu desespero e resolveu te dar a chave da sala 213. Use-a com cuidado")
                    inventario.append ("chave segundo andar")
                else: 
                    print ()
                    print ("Oh não! Essa sala esta bloqueada! Tente achar a chave que abra essa porta")
                    #luta golem
            elif nome_cenario_atual == "garagem":
                 Pergunta = input("Voce quer atacar ou fugir?")
                 
                 if Pergunta == 'atacar':
                    print ()
                    print("-------combate-------")
                    print("Vida golem: 3")
                    print("Sua Vida:{0}".format(vidaP1))
                    vidagolem = 3
                    ataqueP1 = random.randint(1,3)
                    print()
                    print("seu ataque foi: {0}" .format(ataqueP1))
                    vidagolem = vidagolem - ataqueP1
                    while vidagolem>0 and game_over == False:
                        print("Vida Golem:{0}".format(vidagolem))
                        ataquegolem = 5
                        print()
                        print("O golem atacou")
                        vidaP1 = vidaP1 - ataquegolem
                        print("Sua Vida:{0}".format(vidaP1))
                        if vidaP1 > 0:
                            print()
                            ataqueP1 = random.randint(1,2)
                            print("seu ataque foi: {0}" .format(ataqueP1))
                            vidagolem = vidagolem - ataqueP1   
                        elif vidaP1 <= 0 or vidaP1 == 0:
                                print("Voce morreu!")
                                game_over = True
                    if vidagolem <= 0:             
                        print()
                        print("O golem morreu")
                        print("Voce venceu esse combate!!")
                        print ("voce ganhou uma chave misteriosa")
                        inventario.append ("chave misteriosa")
                        nome_cenario_atual = cenario_atual["destino"]
                
                
            #luta ninja
            elif nome_cenario_atual == "lutar ninja":
                 Pergunta = input("Voce quer atacar ou fugir?")
                 
                 if Pergunta == 'atacar':
                    print("-------combate-------")
                    print("Vida ninja: 3")
                    print("Sua Vida:{0}".format(vidaP1))
                    vidaninja = 3
                    ataqueP1 = random.randint(1,2)
                    print()
                    print("seu ataque foi: {0}" .format(ataqueP1))
                    vidaninja = vidaninja - ataqueP1
                    while vidaninja > 0 and game_over == False:
                        print("Vida Ninja:{0}".format(vidaninja))
                        ataqueninja = 5
                        print()
                        print("O ninja atacou")
                        vidaP1 = vidaP1 - ataqueninja
                        print("Sua Vida:{0}".format(vidaP1))
                        if vidaP1 > 0:
                            print()
                            ataqueP1 = random.randint(1,2)
                            print("seu ataque foi: {0}" .format(ataqueP1))
                            vidaninja = vidaninja - ataqueP1   
                        elif vidaP1 == 0 or vidaP1<=0:
                                print("Voce morreu!")
                                game_over = True
                    if vidaninja <= 0:            
                        print()
                        print("O ninja morreu")
                        print("Voce venceu esse combate!!")
                        print("Voce ganhou um ataque especial para quando for entregar o EP: ")
                        print("ataque agilidadeeee")
                        print("Esse ataque consegue tirar 10 de vida do inimigo final")
                        ataqueagilidade = 10
                        print()
                        nome_cenario_atual = cenario_atual["destino"]
            # Luta tiazinha   
            elif nome_cenario_atual == "tiazinha da biblio":
                Pergunta = input("Voce quer atacar ou fugir?")
                
                if Pergunta == 'atacar':
                    print("-------combate-------")
                    print("Vida tiazinha: 3")
                    print("Sua Vida:{0}".format(vidaP1))
                    vidaTia = 3
                    ataqueP1 = random.randint(1,2)
                    print()
                    print("seu ataque foi: {0}" .format(ataqueP1))
                    vidaTia = vidaTia - ataqueP1
                    while vidaTia > 0:
                        print("Vida Tiazinha:{0}".format(vidaTia)) 
                        ataqueTia = 3
                        vidaP1 = vidaP1 - ataqueTia
                        print()
                        print("A tiazinha atacou")
                        print("Sua Vida:{0}".format(vidaP1))
                        if vidaP1 > 0:
                            ataqueP1 = random.randint(1,2)
                            print("seu ataque foi: {0}" .format(ataqueP1))
                            vidaTia = vidaTia - ataqueP1 
                        elif vidaP1 == 0:
                                print("Voce morreu!")
                                game_over = True
                    print()
                    print("A tiazinha morreu")
                    print("Voce venceu esse combate!!")
                    print("Voce ganhou um ataque especial para quando for entregar o EP: ")
                    print("ataque do livraoooo")
                    print("Esse ataque consegue tirar 15 de vida do inimigo final")
                    ataquelivrao = 15
                    print()
                    nome_cenario_atual = cenario_atual["destino"]
                    
            #Luta professor
            elif nome_cenario_atual == "luta professor":
                print("-------batalha final-------")
                print("Vida professor: 60")
                print("Sua Vida:{0}".format(vidaP1))
                vidaprofessor = 60
                while vidaprofessor > 0:
                    if vidaP1 > 0:
                        if ataqueagilidade == 10:
                            if ataquelivrao == 15:
                                print()
                                qual_ataque = input("deseja atacar com livrao ou agilidade?  ")
                                if qual_ataque == 'agilidade':
                                    ataqueP1 = 10
                                    print("seu ataque foi: {0}" .format(ataqueP1))
                                    vidaprofessor = vidaprofessor- ataqueP1
                                elif qual_ataque == 'livrao':
                                    ataqueP1 = 15
                                    print("seu ataque foi: {0}" .format(ataqueP1))
                                    vidaprofessor = vidaprofessor - ataqueP1
                            else:
                                print("Voce pode atacar com agilidade")
                                ataqueP1 = 10
                                print("seu ataque foi: {0}" .format(ataqueP1))
                                vidaprofessor = vidaprofessor - ataqueP1
                        elif ataquelivrao == 15:
                            if ataqueagilidade == 10:
                                print()
                                qual_ataque = input("deseja atacar com livrao ou agilidade?  ")
                                if qual_ataque == 'agilidade':
                                    ataqueP1 = 10
                                    print("seu ataque foi: {0}" .format(ataqueP1))
                                    vidaprofessor = vidaprofessor - ataqueP1
                                elif qual_ataque == 'livrao':
                                    ataqueP1 = 15
                                    print("seu ataque foi: {0}" .format(ataqueP1))
                                    vidaprofessor = vidaprofessor - ataqueP1
                            else:
                                print("Voce pode atacar com o livrao")
                                ataqueP1 = 15
                                print("seu ataque foi: {0}" .format(ataqueP1))
                                vidaprofessor = vidaprofessor - ataqueP1 
                        else:
                            ataqueP1 = 5
                            print()
                            print("seu ataque foi: {0}" .format(ataqueP1))
                            vidaprofessor = vidaprofessor - ataqueP1
                    
                    elif vidaP1 <= 0:
                        game_over = True
                        break
                    
                    if vidaprofessor > 0:
                        print("Vida Professor:{0}".format(vidaprofessor)) 
                        ataqueprofessor = 10
                        vidaP1 = vidaP1 - ataqueprofessor
                        print()
                        print("Professor atacou")
                        print("Sua Vida:{0}".format(vidaP1))   
                    
                if vidaprofessor <= 0:
                    print()    
                    print("O professor morreu")
                    print("VOCÊ VENCEU A BATALHA FINAL")
                    game_over = True
                    ganhou = True
                    
                
            print()
            nome_cenario_atual = cenario_atual["destino"]
            

    if ganhou == True:
        print("Voce livrou o Insper de um monstro e ainda conseguiu adiar a entrega do EP para todos")
        print ()
        print("Voce é o novo heroi")
    else:
        print ()
        print("GAME OVER")


# Programa principal.
if __name__ == "__main__":
    main()
