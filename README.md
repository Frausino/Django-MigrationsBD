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

# 1. Rastreamento de migrações aplicadas

O Django mantém uma tabela django_migrations no banco de dados.
Cada linha corresponde a uma migração aplicada.
Isso garante que migrações não sejam aplicadas mais de uma vez.
Se você remover manualmente a linha, o Django pode reaplicar a migração, mas isso não é recomendado em produção.

# 2. Arquivos de migração

Cada migração é um arquivo Python dentro de migrations/.
Contém uma classe Migration com:
dependencies: lista de migrações que precisam ser aplicadas antes.
operations: lista de operações que alteram o banco de dados.
As operações comuns incluem:
CreateModel, DeleteModel, RenameModel
AddField, RemoveField, AlterField, RenameField
AddIndex, RemoveIndex
Operações avançadas:
RunSQL — SQL personalizado
RunPython — código Python personalizado
SeparateDatabaseAndState — separa estado do projeto e do banco, útil para migrações complexas ou de grandes volumes de dados.

# 3. Dependências entre migrações

Dependências controlam a ordem de execução.
Podem ser:
Dentro do mesmo app (('historical_data', '0001_initial'))
Entre apps diferentes (('auth', '0009_alter_user_last_name_max_length'))
É possível usar run_before para forçar uma migração a rodar antes de outra.

# 4. Como o Django detecta alterações

Django não compara com o banco de dados diretamente.
Ele reconstrói o “estado do projeto” a partir das migrações aplicadas.
Compara esse estado com os modelos atuais e gera operações necessárias.
Isso garante compatibilidade entre SQL gerado e banco de dados específico.

# 5. Visualização do SQL

Comando: python manage.py sqlmigrate <app> <migration_number>
Permite ver o SQL que será executado antes de aplicar a migração.
Pode usar --backwards para ver o SQL de desaplicação.

# 6. Limitações e precauções

Django tenta criar migrações eficientes.
Alterações complexas podem gerar DeleteModel + CreateModel inesperados, apagando dados.
Sempre revise migrações e teste em uma cópia do banco de dados antes de produção.
Não mexa diretamente na tabela django_migrations em produção.

# 7. Operações avançadas

SeparateDatabaseAndState é útil para:
Criar índices em grandes tabelas sem downtime
Mover modelos entre apps
Evita inconsistências entre o estado do projeto e o banco de dados real.
Requer cuidado, parecido com “cirurgia cardíaca” em termos de risco.

# ✅ Resumo Final

Django mantém o histórico de migrações para não reaplicar mudanças.
Cada migração é um arquivo Python contendo Migration com dependencies e operations.
Django compara o estado reconstruído dos modelos com os atuais e gera automaticamente as operações necessárias.
Para casos avançados, existem operações personalizadas e a poderosa SeparateDatabaseAndState.
