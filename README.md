# Análise de Redes de Tráfego Marítimo (AIS 2025)
### 📂 Estrutura do Projeto
```text
maritime-traffic-graph/
├── notebooks/          # Processamento no Kaggle
├── src/                # Scripts de construção do grafo
├── output/             # Arquivo .graphml para o Gephi
├── docs/               # Prints e relatórios
└── README.md           # Documentação


# Maritime Traffic Graph Analysis (AIS 2025)

Este projeto realiza a modelagem e análise de redes complexas a partir de dados de telemetria AIS (Automatic Identification System) obtidos através do **MarineCadastre.gov**. O foco é a reconstrução de rotas marítimas georreferenciadas para o ano de 2025.

##  Estrutura do Repositório

- **notebooks/**: Experimentos e processamento pesado realizados no Kaggle.
- **src/**: Scripts Python reutilizáveis para carregamento de dados e construção de grafos.
- **output/**: Arquivos `.graphml` gerados para visualização no Gephi.
- **docs/**: Documentação, imagens de satélite e resultados das análises.

##  Tecnologias e Ferramentas
- **Linguagem**: Python 3.10+
- **Processamento**: GeoPandas, Pyogrio (leitura de alta performance).
- **Grafos**: NetworkX (algoritmos de centralidade e métricas).
- **Visualização**: Gephi (layout geográfico e análise visual).
- **Ambiente**: Kaggle Kernels (processamento de datasets > 7GB).

## Metodologia
O projeto utiliza a técnica de **Coordinate Rounding** (Arredondamento de Coordenadas) para agrupar sinais de GPS em hubs logísticos (nós), permitindo a análise de fluxo entre portos e zonas de tráfego intenso.

##  Como Executar
1. Clone o repositório: `git clone https://github.com/arleswasb/maritime-traffic-graph.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Utilize os notebooks na pasta `/notebooks` para processar os dados do MarineCadastre.

##  Identificação Acadêmica

Autor: Werbert Arles de Souza Barradas

Instituição: Universidade Federal do Rio Grande do Norte (UFRN)

Curso: Engenharia de Computação

Disciplina: Estrutura de Dados II

Orientador: Prof. Dr. Ivanovich Silva