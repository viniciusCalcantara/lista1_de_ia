# S1: A ^ B → C
# S2: A → D
# S3: C ^ D → E
# S4: B ^ E ^ F → G
# S5: A ^ E → H
# S6: D ^ E ^ H → I
# S7: A
# S8: B
# S9: F

base_de_fatos = set()
base_de_fatos.add('A')
base_de_fatos.add('B')
base_de_fatos.add('F')

pilha = []
    
def Antecedentes(hipotese):
    if (hipotese == 'C'):
        return ['A', 'B']
    elif (hipotese == 'D'):
        return ['A']
    elif (hipotese == 'E'):
        return ['C', 'D']
    elif (hipotese == 'G'):
        return ['B', 'E', 'F']
    elif (hipotese == 'H'):
        return ['A', 'E']
    elif (hipotese == 'I'):
        return ['D', 'E', 'H']
    else:
        return []


def busca_em_profundidade(hipotese):
    if hipotese in base_de_fatos:
        return True
    else:
        pilha.append(hipotese)
        antecedentes = Antecedentes(hipotese)
        if len(antecedentes) == 0:
            pilha.pop()
            return False
        
        for antecedente in antecedentes:
            if busca_em_profundidade(antecedente) == False:
                return False
        pilha.pop()
        base_de_fatos.add(hipotese)
        return True


sentenca_inicial = input("Digite a sentença inicial a ser provada: ")
if busca_em_profundidade(sentenca_inicial):
    print(f"{sentenca_inicial} é verdade")
else:
    print(f"{sentenca_inicial} não pode ser provada")
