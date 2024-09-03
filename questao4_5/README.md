# Agente Inteligente

Este projeto permite criar agentes inteligentes configuráveis por meio de regras e fatos. Siga as instruções abaixo para configurar o seu agente.

## Estrutura do Diretório

Crie um diretório com o nome do seu agente. Dentro deste diretório, você deve ter os seguintes arquivos:

- `regras.txt` - Contém as regras que o agente usará para inferência.
- `fatos.txt` - Contém os fatos conhecidos que o agente utilizará para aplicar as regras.
- `conf.txt` - Contém o caminho para os arquivos de regras e fatos.

Por exemplo, para um agente chamado `gerente`, a estrutura do diretório deve ser:

gerente/
    ├── regras.txt
    ├── fatos.txt
    └── conf.txt


## Configuração dos Arquivos

### Arquivo `regras.txt`

Este arquivo deve conter as regras que o agente usará. Cada linha deve seguir o formato:
condição1, condição2 => resultado

**Exemplo:**

```plaintext
renda=0k-15k, garantia=nenhuma=>risco=alto
renda=0k-15k, garantia=adequada=>risco=moderado
renda=15k-35k, divida=alta, historia_de_credito=desconhecida=>risco=alto
renda=15k-35k, divida=alta, historia_de_credito=ruim=>risco=alto
renda=15k-35k, divida=alta, historia_de_credito=boa=>risco=moderado
renda=15k-35k, divida=baixa=>risco=moderado
renda=acima_de_35k, historia_de_credito=desconhecida, garantia=nenhuma, divida=baixa=>risco=baixo
renda=acima_de_35k, historia_de_credito=desconhecida, garantia=nenhuma, divida=alta=>risco=moderado
renda=acima_de_35k, historia_de_credito=desconhecida, garantia=adequada=>risco=baixo
renda=acima_de_35k, historia_de_credito=ruim=>risco=moderado
renda=acima_de_35k, historia_de_credito=boa=>risco=baixo
```

### Arquivo `fatos.txt`

Este arquivo deve conter os fatos iniciais que o agente usará. Cada linha deve seguir o formato:
fato=valor

**Exemplo:**
```plaintext
historia_de_credito=boa
divida=alta          
garantia=nenhuma
renda=0k-15k
```

### Arquivo `conf.txt`

Este arquivo deve conter os caminhos para os arquivos de regras e fatos. O formato do arquivo é:
fatos=caminho/para/fatos.txt
regras=caminho/para/regras.txt

**Exemplo:**
```plaintext
fatos=gerente/fatos.txt
regras=gerente/regras.txt
```


### Uso do engenho de inferência

Depois de criado a estrutura de diretório necessária basta rodar: python app.py

## Motor de Inferência

O motor de inferência do agente inteligente possui duas funções principais:

### Encadeamento para Frente

O encadeamento para frente é uma técnica de inferência usada para deduzir novos fatos a partir dos fatos conhecidos e das regras fornecidas. Este método começa com os fatos iniciais e aplica as regras para gerar novos fatos até que não seja possível derivar mais informações. É útil quando você deseja deduzir todas as consequências possíveis a partir dos fatos conhecidos.

### Encadeamento para Trás

O encadeamento para trás, por outro lado, começa com uma hipótese ou conclusão desejada e trabalha retroativamente para verificar se essa conclusão pode ser alcançada a partir dos fatos conhecidos e das regras fornecidas. Esse método é usado para verificar se uma determinada conclusão pode ser provada ou para encontrar os fatos necessários que sustentam uma determinada conclusão.

Ambos os métodos são implementados para fornecer flexibilidade na maneira como o agente pode processar informações e inferir resultados com base nas regras e fatos configurados.

