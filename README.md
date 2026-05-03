# Análise de Redes de Tráfego Marítimo (AIS 2025)
### 📂 Estrutura do Projeto
```text
maritime-traffic-graph/
├── notebooks/          # Processamento no Kaggle
├── src/                # Scripts de construção do grafo
├── output/             # Arquivo .graphml para o Gephi
├── docs/               # Prints e relatórios
└── README.md           # Documentação


Este projeto realiza a modelagem e análise de grafos georreferenciados a partir de dados de telemetria AIS (Automatic Identification System) do banco de dados **MarineCadastre.gov** referentes ao ano de 2025.

## 🚀 Objetivo
Extrair trajetórias de navios (Track Lines), processar milhões de registros via Python/Kaggle e gerar um grafo no formato `.graphml` para análise avançada de redes no **Gephi**.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **GeoPandas & Pyogrio**: Processamento de dados espaciais de alta performance.
- **NetworkX**: Construção e algoritmos de teoria dos grafos.
- **Gephi**: Visualização e layout geográfico.
- **Kaggle**: Ambiente de nuvem para processamento do dataset de 7GB.

## 📊 Metodologia de Grafos
- **Nós (Nodes)**: Pontos de origem e destino (Hubs/Portos) identificados via arredondamento de coordenadas (precisão de ~1.1km).
- **Arestas (Edges)**: Movimentação de navios entre nós.
- **Pesos (Weights)**: Frequência de tráfego e duração média das viagens.

## 📈 Análises Realizadas
- [ ] Centralidade de Intermediação (Betweenness) para identificar gargalos.
- [ ] PageRank para definir autoridade dos portos.
- [ ] Detecção de Comunidades (Clusters logísticos).

## 📄 Como utilizar
1. Execute o notebook disponível na pasta `/notebooks` no ambiente Kaggle.
2. Baixe o arquivo `traffic.graphml`.
3. Importe no Gephi e utilize o plugin **GeoLayout** para visualização espacial.
