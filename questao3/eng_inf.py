base_de_fatos = set()
base_de_fatos.add('A')
base_de_fatos.add('B')
base_de_fatos.add('F')

pilha = []
    
antecedentes_dict = {
        'C': ['A', 'B'],
        'D': ['A'],
        'E': ['C', 'D'],
        'G': ['B', 'E', 'F'],
        'H': ['A', 'E'],
        'I': ['D', 'E', 'H']
    }


def Antecedentes(hipotese):
    """ Retorna os antecedentes necessários para provar uma hipótese """
    return antecedentes_dict.get(hipotese, [])


def busca_em_profundidade(hipotese):
    print(f"Procurando por {hipotese}")
    if hipotese in base_de_fatos:
        print(f"{hipotese} é um fato")
        return True
    if hipotese in pilha:
        print(f"{hipotese} está na pilha, ou seja, não pode ser provado")	
        return False 

    pilha.append(hipotese)
    antecedentes = Antecedentes(hipotese)
    if not antecedentes:
        print(f"{hipotese} não tem antecedentes")
        pilha.pop()
        return False  
    
    print(f"Os antecedentes de {hipotese} são {antecedentes}")
    for antecedente in antecedentes:
        if not busca_em_profundidade(antecedente):
            print(f"{antecedente} não pode ser provado")
            pilha.pop()
            return False
    
    print(f"Todos os antecedentes de {hipotese} foram provados")
    base_de_fatos.add(hipotese) 
    pilha.pop()
    return True


sentenca_inicial = input("Digite a sentença inicial a ser provada: ")
if busca_em_profundidade(sentenca_inicial):
    print(f"{sentenca_inicial} é verdade")
else:
    print(f"{sentenca_inicial} não pode ser provada")
