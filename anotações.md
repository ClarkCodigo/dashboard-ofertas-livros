## ** Rodar antes de inciar o projeto:**

``` powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # libera o script de ativação só nesta janela
.venv\Scripts\Activate.ps1
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
    - E imutavel, sem atribuição append 
2. Set
    - Conjunto sem repetição
3. sorted x sort()
    -somente lista vs lista, set, tuplas, etc