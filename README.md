# SICC
Projeto Acadêmico SICC

Trata-se de um sistema integrado de controle de cabines

## Como rodar o projeto

## Pré-requisitos

- Python 3.8+
* Recomendado: Python 3.10.9
## Configuração do Ambiente

1. Clone o repositório:
    ```
    git clone https://github.com/Emanuel-Bruno/SICC.git
    cd SICC
    ```

2. Crie um ambiente virtual e ative-o:
    ```
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```
    pip install -r requirements-dev.txt
    ```


## Executando o Projeto

1. Aplique as migrações:
    ```
    python manage.py migrate
    ```

2. Execute o servidor de desenvolvimento:
    ```
    python manage.py runserver
    ```

Agora você pode acessar o site em `http://localhost:8000`.

## Executando os Testes

Para executar os testes, use o seguinte comando:

```
python manage.py test principal
```

### Utilizando o coverage:
Executando
```
coverage run manage.py test principal
```

Criando o report
```
coverage report
```

Criando a documentação em html
```
coverage html
```

