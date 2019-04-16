# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Caroline Chaim, carolineclc@al.insper.edu.br
# - aluno B: Giovanna Campedelli, giovannahc@al.insper.edu.br
import random
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "quarto andar": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
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
            "titulo": "Andar da varzea",
            "descricao": "Voce chegou ao quarto andar",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "wii": "Jogar wii e aceitar a DP"
            }
        },
        "wii": {
            "titulo": "wiiiiiiii",
            "descricao": "Voce ganhou no MarioKark, porém DP garantida",
            "opcoes": {}
        },
        "pegar livro": {
            "titulo": "livro",
            "descricao": "livro",
            "destino": "biblioteca"
        
        },
        "tiazinha da biblio": {
            "titulo": "Você deve lutar contra a Tiazinha",
            "descricao": "Tiazinha tem 3 de vida e pode tirar 10 das suas",
            "destino": "biblioteca"
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "pegar livro": "Tentar estudar,pegar livro sobre Python",
                "tiazinha da biblio": "Voce fez muito barulho, enfrente a tiazinha"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


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
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        vidaP1 = 10

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
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
    
                
                # Aluno B: substitua este comentário e a linha abaixo pelo código
                # para pedir a escolha do usuário.
                print()
                print("Suas escolhas são: ")
                for e, desc in opcoes.items():
                    print("{0}: {1}".format(e, desc))
                print()
                escolha = input("Para onde você deseja ir?: ")
                    
    
    
    
                if escolha in opcoes:
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True
        else:
            if nome_cenario_atual == "pegar livro":
                print("Voce esta aprendendo, ganhou +10 de vida!")
                vidaP1 = vidaP1 + 10
                print ("Suas vidas: {0}".format(vidaP1))
            
            elif nome_cenario_atual == "tiazinha da biblio":
                Pergunta = input("Voce quer atacar ou fugir?")
                
                if Pergunta == 'atacar':
                    print("-----combate---")
                    print("Vida tiazinha: 3")
                    print("Sua Vida:{0}".format(vidaP1))
                    vidaTia = 3
                    ataqueP1 = random.randint(1,3)
                    print()
                    print("seu ataque foi: {0}" .format(ataqueP1))
                    vidaTia = vidaTia - ataqueP1
                    while vidaTia > 0:
                        ataqueTia = 10
                        vidaP1 = vidaP1 - ataqueTia
                        if vidaP1 > 0:
                            ataqueP1 = random.randint(1,3)
                            print("seu ataque foi: {0}" .format(ataqueP1))
                            vidaTia = vidaTia - ataqueP1
                        elif vidaP1 == 0:
                            print("Voce morreu!!")
                            game_over = True
                    else:
                        break
                
            print()
            nome_cenario_atual = cenario_atual["destino"]
            

    print("Você morreu!!")


# Programa principal.
if __name__ == "__main__":
    main()
