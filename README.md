# Django Migrations Project

Este projeto acompanha o curso de **estrutura de aplicativos Python e Django**, abordando:

## Estrutura do projeto

- Pacotes únicos, módulos internos e múltiplos módulos
- Diretórios típicos: `bin/`, `data/`, `docs/`, `static/`, `templates/`
- Scripts úteis: `runserver`, `resetdb`

## Django

- **Apps**: módulos que contêm models, views, tests, admin
- **Models**: definem o esquema do banco de dados
- **Migrations**: sincronizam models com o banco sem SQL
  - Criar: `python manage.py makemigrations`
  - Aplicar: `python manage.py migrate`
  - Listar: `python manage.py showmigrations`
  - Nomear: `python manage.py makemigrations app --name descriptive_name`
- **Admin**: interface administrativa pronta
- **ORM**: mapeia classes Python para tabelas

## Boas práticas

- `.gitignore` configurado para Django e venv
- Variáveis sensíveis em `.env`
- Testes separados por módulo (`tests/`)
- Documentação com **Sphinx** (opcional)
- Uso de linters e formatadores: `flake8`, `black`

## Rodando o projeto

1. Clonar o repositório
2. Criar e ativar virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

## Migrations (Migrações)

As migrações sincronizam os models com o banco de dados sem precisar escrever SQL manualmente.

- **Criar migrações**:

```bash
python manage.py makemigrations
Aplicar migrações:

bash
python manage.py migrate

Listar migrações:

bash
python manage.py showmigrations

Nomear migrações (boa prática para futuras referências):

bash
python manage.py makemigrations <app_name> --name descriptive_name
```
