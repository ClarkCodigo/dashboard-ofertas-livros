## ** Rodar antes de inciar o projeto:**

``` powershell
    python -m venv .venv
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # libera o script de ativação só nesta janela
    .venv\Scripts\Activate.ps1

    # chamar dados da aula atual
    pip install -r aula04/requirements.txt
    streamlit run aula04/app.py #rodar o arquivo web
```
``` Bash
    python3 -m venv .venv
    source .venv/bin/activate

    # chamar dados da aula atual
    pip install -r aula04/requirements.txt
    streamlit run aula04/app.py # rodar o arquivo web
```

*Utilizar docstring nas funções*

**[ Aula Dois ]**
1. Filtragem de dados, string para numeros
2. Aplicação de listas
3. *Dicionário (chave:valor) 


**[ Aula Nove ]**
1. Tuplas
    - E imutavel, sem atribuição append, util para inclusão de chaves
2. Set
    - Conjunto sem repetição
3. sorted x sort()
    - somente lista vs lista, set, tuplas, etc
4. list comprehension
    - fazer loop, e condiçõa e resultado em uma linha
    - o que guarda | para cada item | caso condição seja verdadeira (opcional)
5. Ordenar com lambda
    - define qual o valor correto para comparação
    - Ex: sorted(livros, key=lambda livro: livro["preco"])

notas: Listas, tuplas, set, dicionario, desempacotamento, set, add, sorted, e outros

## Aula 4: Escrita em arquivos e manipulação de dicionários 
**Arquivos e CSV:** 
- Modos de abertura (open): "r" para leitura, "w" para escrita (apaga o conteúdo anterior e cria um novo arquivo) e "a" para acréscimo no final do arquivo.   

**Escrita de texto e CSV:**
- O método .write() exige strings e quebras de linha explícitas (\n). Para tabelas, usa-se csv.DictWriter (com newline="" para evitar linhas em branco no Windows), escrevendo o cabeçalho via .writeheader() apenas se o arquivo ainda não existir (.exists()) e adicionando registros via .writerow().

**Ambiente local vs. nuvem:** 
- No computador local, o arquivo .csv permanece salvo no disco; no Streamlit Cloud, o arquivo é temporário, compartilhado entre usuários e apagado quando o servidor reinicia.  

**Dicionários:**
- Busca e percurso: Usar o título como chave ({titulo: dados}) evita duplicidades e permite verificar existência com in sem laços. Para iterar, utilizam-se .keys() (chaves), .values() (valores) e .items() (pares chave-valor).   

**Edição, remoção e cópia:** 
- O método .update() altera ou cria múltiplas chaves simultaneamente e del remove uma chave específica. Como atribuir um dicionário (copia = d) cria apenas uma referência ao mesmo objeto, usa-se d.copy() para gerar uma cópia independente (aplicado na simulação de desconto sem alterar o preço original).   Componentes Streamlit: Separação da interface em abas com st.tabs, captura de cliques com st.button e atualização imediata da interface após gravar ou remover dados com st.rerun().   

## Aula 5: Tuplas, sets, list comprehension e lambda
**Tuplas:** 
- Sequências imutáveis definidas com parênteses (a, b) que, diferentemente das listas, podem ser chaves de dicionários. São usadas para retornar múltiplos valores de uma função e fazer desempacotamento (menor, maior = calcular_faixa_precos(livros)), alimentando o filtro de intervalo de dois pontos no st.slider.   

**Sets (Conjuntos):** 
- Coleções mutáveis sem elementos repetidos e sem acesso por índice, criadas com set() e alimentadas com .add(). Permitem operações de união (a | b), interseção (a & b) e diferença (a - b), usadas no projeto para subtrair as categorias favoritadas do total de categorias e exibir o resultado em um st.expander.   

**Ordenação (sorted vs. .sort()):** 
- Enquanto .sort() modifica apenas listas diretamente e retorna None, a função sorted(colecao) aceita qualquer coleção (listas, sets, tuplas) e devolve uma nova lista ordenada.   

**List Comprehension:** 
- Sintaxe [expressao for item in colecao if condicao] usada para condensar filtros e mapeamentos em uma única linha. Não deve ser usada quando o objetivo é acumular valores numéricos ou montar dicionários com estruturas if/else internas.   

**Funções Lambda:** 
- Funções anônimas de uma expressão (lambda parametro: retorno) passadas ao parâmetro key= da função sorted() para ordenar listas de dicionários por título, preço ou nota, combinadas com reverse=True para ordem decrescente.   