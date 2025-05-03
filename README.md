# KnowYourFan

KnowYourFan é um projeto E-Sports criado em Python (Back-end) com FastAPI; e Angular (Front-end).
Este tem o objetivo de promover a estratégia  Know Your Fan, que seria coletar o máximo de informação sobre o usuário e fornecer conteúdo e serviços exclusivos.
O aplicativo permite fazer o vínculo da rede social (Facebook Graph API) do usuário e então acessar conteúdo de E-Sports customizado por IA (Gemini) de acordo com os interesses do usuário.
Para o armazenamento de dados é utilizado o Firebase Cloud Firestore e para os arquivos o Firebase Storage.

https://knowyourfan.onrender.com/

## Back-end - Python (FastAPI)
O Back-end é uma API em Python, que está no padrão de arquitetura CQRS (Command Query Responsibility Segregation) e também utiliza o Repository Pattern para o acesso de dados do Firebase.
A autenticação é feita com uso de JWT. Também é utilizado a API do Gemini, Firebase e Facebook Graph API.

### Instalação/Execução:
É necessário configurar as variáveis de ambientes no arquivo .env e providenciar a Secret File ServiceAccountKey.json que não está presente no repositório.
```bash

# Instale os pacotes necessários
pip install -r requirements.txt

# Inicie o servidor (localhost)
uvicorn main:app --reload

# Ou para Deploy use
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

```

### Estrutura:  

```text
app/
├── api/
│   ├── {endpoint-folder}/
│   │   ├── commands
│   │   └── queries
│   └── {endpoint-routes}.py
├── services/
├── models/
├── repositories/
├── .env
├── ServiceAccountKey.json
└── main.py
```

### Endpoints:
![image](https://github.com/user-attachments/assets/e947ae4f-d84e-44dc-a0fe-786a3feb4605)

### Models:
```python
class User(BaseModel):
    id: str
    facebook: str
    email: str
    password: str
    name: str
    address: str
    cpf: str
    interests: List[str]

class Document(BaseModel):
    id: str
    valid: bool
    type: str
    document_id: str
```


## Front-end - AngularJS
O Front-end é uma aplicação Angular que consome a API integrando as funcionalidades.

### Instalação/Execução:
```bash

# Instale os pacotes necessários
npm install

# Inicie o servidor (localhost)
ng serve --ssl

# Ou para Deploy use
npm run build --prod

```

### Estrutura:  

```text
src/
├── app/
│   ├── components/
│   ├── pages/
│   └── services/
├── environments/
└── main.ts
```

### Telas e Funcionalidades:

#### Página Home:
![image](https://github.com/user-attachments/assets/e869de6e-f992-425b-957b-fdda35f44092)
> Funcionalidades:
> - Navegação
<br>

#### Página de Login:
![image](https://github.com/user-attachments/assets/1dbd3a93-3c81-4c53-bd26-f58c1aba0036)
> Funcionalidades:
> - Login por usuário
> - Login por Facebook
<br>

#### Página de Cadastro:
![image](https://github.com/user-attachments/assets/fb9ba135-2b72-41ec-916d-a170f04c7e78)
> Funcionalidades
> - Cadastro
> - Atualização de dados
<br>

#### Página de Documentos:
![image](https://github.com/user-attachments/assets/8b9ffdca-f188-4276-a36b-be3a0c2e79a0)
##### Modais:
<p align="center">
  <img src="https://github.com/user-attachments/assets/30667621-a2d1-4e80-a16d-de72858181b8" width="400"/>
  <img src="https://github.com/user-attachments/assets/a2dd3639-1b0e-4b78-b6fd-d24be8a16762" width="400"/>
</p>

> Funcionalidades
> - Upload de documentos
> - Visualização de documentos
> - Validação de documentos por IA (Gemini)
<br>

#### Página E-Sports:
![image](https://github.com/user-attachments/assets/3f055b21-0dac-4945-b95a-526fd2351305)
> Funcionalidades
> - Acesso de conteúdo E-Sports personalizado por IA (Gemini)
<br>
