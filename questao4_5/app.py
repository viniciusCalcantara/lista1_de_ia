from knowledge_base import KnowledgeBase
from inference_engine import InferenceEngine
import os
import copy


def criar_agente(nome_do_agente):

    kb = KnowledgeBase()
    config = {}
    with open(nome_do_agente + '/conf.txt', 'r') as file:
        for line in file:
            if '=' in line:
                chave, valor = line.strip().split('=')
                config[chave] = valor

    if not os.path.exists(config['fatos']):
        print(f"Arquivo não encontrado: {config['fatos']}")
        return
    with open(config['fatos'], "r") as file:
        fatos = file.read().split("\n")
        fatos = [f.strip() for f in fatos]

    for fato in fatos:
        kb.add_fact(fato.lower().strip())


    if not os.path.exists(config['regras']):
        print(f"Arquivo não encontrado: {config['regras']}")
        return
    with open(config['regras'], "r") as file:
        regras = file.read().split("\n")
        regras = [r.strip() for r in regras]



    for regra in regras:
        if "=>" not in regra:
            continue

        antecedentes, consequentes_lista = regra.split("=>")
        antecedentes_lista = antecedentes.split(", ")
        consequentes_lista = consequentes_lista.split(", ")

        for consequente in consequentes_lista:
            kb.add_rule(antecedentes_lista, consequente)
    
    
    return kb


def main():
    print("----------Vamos criar seu agente inteligente!! ----------")
    print("Insira o nome do seu agente")
    nome_do_agente = input().strip()
    
    kb = criar_agente(nome_do_agente)    
    ie = InferenceEngine(kb)

    # print("Fatos: ", kb.facts)
    print("Regras: ", kb.rules)

    print("A sua base de conhecimento (Regras) foi carregada com sucesso!!")
    print("Os fatos iniciais também foram carregados com sucesso!!")

    print("O que sabemos no momento: ", kb.facts)

    print("-----------------")

    print("Digite 1 para acionar o engenho de inferência e ver que regras podem ser acionadas")
    print("Digite 2 para fornecer uma hipótese que você deseja provar a respeito dos fatos que você tem")
    print("Digite 3 para sair")
    input_usuario = input("opcao: ").strip()


    fatos_atuais = copy.deepcopy(kb.facts)
    while input_usuario != "3":
        if fatos_atuais != kb.facts:
            print("Os fatos mudaram!!")
            print("Os fatos atuais são: ", kb.facts)
            fatos_atuais = copy.deepcopy(kb.facts)
            print("-----------------")

        if input_usuario == '1':
            conclusoes_obtidas, regras_acionadas = ie.forward_chaining()

            if len(conclusoes_obtidas) == 0:
                print("Nenhuma regra pode ser acionada")
            else:
                print("Regras acionadas: ", regras_acionadas)
                print("Conclusões obtidas: ", conclusoes_obtidas)

            print("-----------------")
            
        elif input_usuario == '2':
            hipotese = input("Digite a hipótese que você deseja provar: ").strip()
            if ie.backward_chaining(hipotese):
                print(f"A hipótese {hipotese} pode ser provada de acordo com o conhecimento do engenho de inferência")
            else:
                print(f"A hipótese {hipotese} não pode ser provada de acordo com o conhecimento do engenho de inferência")
            
            print("-----------------")


        input_usuario = input("opcao: ").strip()
            
        
    
    print("Obrigado por usar o engenho de inferência!!")


main()





        
        

    
    