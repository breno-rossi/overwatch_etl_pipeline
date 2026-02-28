# Overwatch Heroes ETL Pipeline

Pipeline de dados que extrai estatísticas de heróis do Overwatch de uma API externa, transforma os dados e carrega em um banco PostgreSQL para análise e visualização em dashboards Grafana.

## Arquitetura

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│   Overfast API  │ ──── │   ETL Pipeline  │ ──── │   PostgreSQL    │
│   (Data Source) │      │    (Airflow)    │      │   (Data Store)  │
└─────────────────┘      └─────────────────┘      └────────┬────────┘
                                                           │
                                                  ┌────────▼────────┐
                                                  │     Grafana     │
                                                  │   (Dashboard)   │
                                                  └─────────────────┘
```

## Stack Tecnológica

| Tecnologia | Versão | Função |
|------------|--------|--------|
| Python | 3.x | Linguagem principal |
| Apache Airflow | 2.9.0 | Orquestração do pipeline |
| PostgreSQL | 15 | Banco de dados |
| Grafana | latest | Visualização e dashboards |
| Docker | - | Containerização |
| Pandas | - | Manipulação de dados |

## Estrutura do Projeto

```
overwatch_etl_pipeline/
├── dags/
│   └── heroes_dag.py          # DAG do Airflow para orquestração
├── etl/
│   ├── extract.py             # Extração de dados da API
│   ├── transform.py           # Transformação e limpeza
│   └── load.py                # Carregamento no PostgreSQL
├── sql/
│   ├── schema.sql             # Schema da tabela heroes_stats
│   └── create_airflow_db.sql  # Criação do banco do Airflow
├── docker-compose.yaml        # Configuração dos containers
├── requirements.txt           # Dependências Python
└── etl_test.py                # Script de teste standalone
```

## Pipeline ETL

### Extract
- **Fonte**: [Overfast API](https://overfast-api.tekrop.fr/)
- **Dados**: Estatísticas de heróis (pick rate, win rate)
- **Dimensões**:
  - Plataformas: PC, Console
  - Modos: Competitive, Quickplay
  - Regiões: Americas, Asia, Europe

### Transform
- Adiciona metadados (plataforma, modo, região)
- Registra timestamp de inserção
- Remove registros com dados faltantes

### Load
- Insere dados na tabela `heroes_stats` do PostgreSQL
- Inclui tratamento de erros e rollback de transações

## Schema do Banco de Dados

```sql
CREATE TABLE heroes_stats (
    hero VARCHAR(20),
    pickrate FLOAT,
    winrate FLOAT,
    platform VARCHAR(10),
    gamemode VARCHAR(10),
    region VARCHAR(10),
    INSERTED_AT TIMESTAMP DEFAULT NOW()
);
```

## Como Executar

### Pré-requisitos
- Docker
- Docker Compose

### Subindo os containers

```bash
docker-compose up -d
```

### Acessando os serviços

| Serviço | URL | Porta |
|---------|-----|-------|
| Airflow | http://localhost:1919 | 1919 |
| Grafana | http://localhost:2020 | 2020 |
| PostgreSQL | http://localhost:1818 | 1818 |

### Testando o pipeline manualmente

```bash
python etl_test.py
```

## Agendamento

O pipeline é executado **a cada hora** via Apache Airflow, coletando estatísticas atualizadas dos heróis do Overwatch.

## Dependências

```
requests
pandas
psycopg2-binary
apache-airflow
```

## Licença

Consulte o arquivo [LICENSE](LICENSE) para mais informações.
