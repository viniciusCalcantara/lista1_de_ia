from knowledge_base import KnowledgeBase

class InferenceEngine():

    def __init__(self, knowledbase : KnowledgeBase):
        self.kb = knowledbase
        self.pilha = []


    def forward_chaining(self):
        """ Realiza encadeamento para frente """
        conclusoes = set()
        regras_acionadas = []


        for consequente, lista_antecedentes in self.kb.rules.items():
            for antecedente in lista_antecedentes:
                if all(sentenca in self.kb.facts for sentenca in antecedente):
                    if consequente not in self.kb.facts:
                        self.kb.facts.add(consequente)
                        conclusoes.add(consequente)
                        print(f"Acionando a regra {antecedente} => {consequente}")
                        regras_acionadas.append(f"{antecedente} => {consequente}")
                        print(f"Adicionando {consequente} como fato")

        return conclusoes, regras_acionadas
                    


    def Antecedentes(self, hipotese):
        """ Retorna os antecedentes necessários para provar uma hipótese """
        return self.kb.rules.get(hipotese)
    

    def vertificar_se_o_usuario_pode_comprovar_a_sentenca(self, sentenca):
        """ Verifica se o usuário pode comprovar a sentenca """
        print(f"Você pode provar a sentenca {sentenca}?(s/n)")
        resposta = input().strip()
        if resposta == 's':
            return True
        else:
            return False
        
        
    def backward_chaining(self, hipotese):
        print(f"Procurando por {hipotese}")
        if hipotese in self.kb.facts:
            print(f"{hipotese} é um fato")
            return True
        if hipotese in self.pilha:
            print(f"{hipotese} está na self.pilha, ou seja, não pode ser provado") 
            return False 
    
        self.pilha.append(hipotese)
        antecedentes = self.Antecedentes(hipotese)
        if antecedentes == None:
            print(f"{hipotese} não tem antecedentes")

            if self.vertificar_se_o_usuario_pode_comprovar_a_sentenca(hipotese):
                self.kb.facts.add(hipotese)
                self.pilha.pop()
                return True
            
            self.pilha.pop()
            return False
        
        print(f"Os antecedentes de {hipotese} são {antecedentes}")
        for antecedente in antecedentes:
            todas_as_sentencas_sao_fatos = True
            for senteca in antecedente:
                if not self.backward_chaining(senteca):
                    print(f"{senteca} não pode ser provado")
                    todas_as_sentencas_sao_fatos = False
                    break
            if todas_as_sentencas_sao_fatos:
                print(f"{hipotese} pode ser provado, pois todas os seus antecedentes: {antecedente} são fatos")
                self.pilha.pop()
                return True

        print(f"Não foi possível provar {hipotese}, pois não encontramos um antecedente que possa ser acionado")
        self.pilha.pop()
        return False                    
           