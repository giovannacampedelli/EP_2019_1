# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Caroline Chaim, carolineclc@al.insper.edu.br
# - aluno B: Giovanna Campedelli, giovannahc@al.insper.edu.br


#dicionário de salas
import random
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguão do perigo",
            "descricao": "Você está no saguão de entrada do Insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "quarto andar": "Subir para o andar sagrado da engenharia",
                "biblioteca": "Ir para a biblioteca",
                "rua": "Dar meia volta e sair do prédio velho"
            }
        },
        "rua": {
            "titulo": "Rua da Raposa. aka Quatá",
            "descricao":"Você decidiu dar meia volta e sair do prédio novo. O que pretende fazer agora, jovem?",
            "opcoes": {
                "sujos": "Ir para o bar da raposa como forma de escapar dos seus problemas",
                "predio novo": "Testar sua sorte com um veterano de computacao",
                "inicio": "voltar"
            } 
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguão de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e quer dedvorar sua alma."
                         "O professor tem 40 de vida e pode tirar 10 das suas",
            "opcoes":{
                        "luta professor": "Tente enfrentar o Professor e evitar pegar DP e ser devorado",
            }
        },
        "quarto andar": {
            "titulo": "Andar sagrado da Engenharia",
            "descricao": "Voce chegou ao quarto andar",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguão de entrada",
                "wii": "Jogar Wii",
                "405": "Sala 405",
            }
        },
        "405": {
            "titulo": "sala 405",
            "descricao": "Voce chegou à sala secreta de treinamentos. Um misterioso ninja appeared",
            "opcoes": {"quarto andar": "meia volta volver", 
                       "lutar ninja": "Lutar com o ninja",
                       "conversar": "Conversar com o ninja"
            }
        },
        "wii": {
            "titulo": "Mario Kart, baby",
            "descricao": "Você escolheu jogar MarioKart Wii com os seus veteranos, mas sua DP foi garantida",
            "opcoes": {}
        },
        "pegar livro": {
            "titulo": "livro",
            "descricao": "Pegou o livro de Python",
            "destino": "biblioteca"       
        },
        "conversar": {
                "titulo": "Conversa",
                "descricao": "Conversa afiada", 
                "destino":"quarto andar"
        },      
        "lutar ninja": {
                "titulo" : "Você escolheu lutar com o ninja da computação",
                "descricao": "Ninja tem 3 de vida e pode tirar 5 das suas",
                "destino": "405"
        },        
        "tiazinha da biblio": {
            "titulo": "Você deve lutar contra a Tiazinha",
            "descricao": "Tiazinha tem 3 de vida e pode tirar 5 das suas",
            "destino": "biblioteca"
        },
        "vida" : {"titulo" : "vidas",
                  "descricao" : "estoque de vidas",
                  "destino": "inicio"
          
        },       
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "pegar livro": "Tentar estudar",
                "tiazinha da biblio": "Voce fez muito barulho, enfrente a tiazinha"
            }
        },
        "luta professor": {
                "titulo": "Batalha Final",
                "descricao": "é preciso ganhar esta batalha para conseguir enviar o EP e evitar que sua alma seja devorada",
                "destino": "andar professor"
            },
        "sujos":{
            "titulo" : "Bar dos condenados", 
            "descricao" : "Você nao demora muito para chegar ao bar dos condenados. Lá voce avista um jovem bebendo no canto.",
            "opcoes": {
                "jovem": "Falar com o jovem solitário",
                "beber": "beber até um milagre acontecer",
                "rua": "voltar"
            }
        },
        "jovem": {
            "titulo": "Jovem presidente",
            "descricao": "Parabens! voce avistou o presidente do Diretório academico. O que será que ele tem a oferencer?",
            "destino": "sujos"
        },                            
        "beber": {
            "titulo": "Beber?",
            "descricao": "Voce quer mesmo beber até um milagre acontecer?",
            "opcoes": {
                "beber mais": "Tem certeza?",
                "sujos": "voltar para ir para um melhor caminho (recomendado)"
            }
        },
        "beber mais": {
                "titulo": "Milagre",
                "descricao": " Parabens",
                "destino": "sujos"
        },
        "predio novo": { 
                "titulo": "Melhor predio dos melhores predios",
                "descricao": "Não demorou muito para voce chegar ao predio ideial. Aonde voce quer ir?",
                "opcoes": {
                    "garagem": "O que será que voce vai enconrar na garagem do predio novo?",
                    "terceiro andar": "Encontrar com veteranos da computacao"
            }
        },
        "garagem": {
                "titulo": "golem",
                "descricao": "Voce deve lutar com o golem. O golem tem 10 de vida e tem um ataque de 10",
                "destino": "predio novo"
                
        }               
    }
        
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

#lista inventário
    



def main():
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

    cenarios, nome_cenario_atual = carregar_cenarios()

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
            
            else:
                print()
                print("Suas escolhas são: ")
                print ()
                for e, desc in opcoes.items():
                    print(" -> {0}: {1} \n".format(e, desc))
                print()
                escolha = input("Para onde você deseja ir?: ")
                    
    
                if escolha in opcoes or escolha == "vida":
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True
                    
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
            #cores para a sala de teletransporte
            elif nome_cenario_atual == "jovem":
                print ()
                print ("Depois de ser forcado a pagar uma cerveja para o seu veterano com 5 das duas vidas, ele te deu um papel misterioso contendo as seguintes informacoes:" )
                print ()
                print ("∆ rua:rosa \n∆ biblioteca: azul \n∆ predio novo: verde \n∆ quarto andar: vermelho \n∆ andar professor: preto" )
                vidaP1 -= 5
            #luta golem
            elif nome_cenario_atual == "garagem":
                 Pergunta = input("Voce quer atacar ou fugir?")
                 
                 if Pergunta == 'atacar':
                    print ()
                    print("-------combate-------")
                    print("Vida golem: 3")
                    print("Sua Vida:{0}".format(vidaP1))
                    vidagolem = 10
                    ataqueP1 = random.randint(1,3)
                    print()
                    print("seu ataque foi: {0}" .format(ataqueP1))
                    vidagolem = vidagolem - ataqueP1
                    while vidagolem>0:
                        print("Vida Ninja:{0}".format(vidagolem))
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
                        elif vidaP1 <= 0:
                                print("Voce morreu!")
                                game_over = True
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
                    while vidaninja>0:
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
                        elif vidaP1 <= 0:
                                print("Voce morreu!")
                                game_over = True
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
                print("Vida professor: 40")
                print("Sua Vida:{0}".format(vidaP1))
                vidaprofessor = 40
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
        print("Voce é o novo heroi")
    else:
        print("GAME OVER")


# Programa principal.
if __name__ == "__main__":
    main()
