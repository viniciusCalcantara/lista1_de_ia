class KnowledgeBase():
    def __init__(self):
        self.facts = set()
        self.rules = {}

    def __str__(self):
        return "Facts: " + str(self.facts) + "\nRules: " + str(self.rules)

    def add_fact(self, fact : str):
        self.facts.add(fact)
    
    def add_rule(self,  premisses : list, consequent : str):
        if self.rules.get(consequent) is None:
            self.rules[consequent] = []
            self.rules[consequent].append(premisses)
        else:
            self.rules[consequent].append(premisses)

    
    