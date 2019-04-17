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
                "predio novo": "Testar sua sorte com um veterano de computacao"
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
                         "e devorou sua alma.",
            "opcoes": {}
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
                       "conversar": "Conversar com o ninja"}
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
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

#lista inventário
    
inventario = []



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
    vidaP1 = 10
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
                    print("O ninja morreu")
                    print("Voce venceu esse combate!!")
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
                    print("A tiazinha morreu")
                    print("Voce venceu esse combate!!")
                    print()
                    nome_cenario_atual = cenario_atual["destino"]
                    
                    
                
            print()
            nome_cenario_atual = cenario_atual["destino"]
            


    print("Você morreu!!")


# Programa principal.
if __name__ == "__main__":
    main()
