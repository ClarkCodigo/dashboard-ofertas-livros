## ** Rodar antes de inciar o projeto:**

``` powershell
    python -m venv .venv
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # libera o script de ativação só nesta janela
    .venv\Scripts\Activate.ps1

    # chamar dados da aula atual
    pip install -r aula04/requirements.txt
    streamlit run aula04/app.py #rodar o arquivo web
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