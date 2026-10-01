## ** Rodar antes de inciar o projeto:**

``` powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # libera o script de ativação só nesta janela
.venv\Scripts\Activate.ps1
pip install -r aula01/requirements.txt
streamlit run aula01/app.py #rodar o arquivo web
 
```

*Utilizar docstring nas funções*

**[ Aula Dois ]**
1. Filtragem de dados, string para numeros
2. Aplicação de listas
3. *Dicionário (chave:valor) 
