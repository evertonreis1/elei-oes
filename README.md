# Análise Estatística do Comparecimento e Abstenção nas Eleições de 2024 em Alagoas

## Descrição do Projeto
Este projeto utiliza conceitos de estatística e visualização computacional para analisar os dados referentes ao comparecimento e à abstenção dos eleitores nas eleições de 2024 no estado de Alagoas. A análise visa compreender padrões de participação eleitoral, identificar tendências e oferecer insights sobre a distribuição dos votos.

## Estrutura do Projeto
```
elei-oes/
├── data/
│   ├── raw/                  # Dados brutos originais
│   │   ├── comparecimento_abstencao_eleitor_tte_2024.csv
│   │   └── perfil_comparecimento_abstencao_2024_AL.csv
│   └── processed/            # Dados limpos e pré-processados (se aplicável)
├── notebooks/
│   ├── 01_data_preparation.ipynb  # Carregamento e pré-processamento inicial dos dados
│   ├── 02_alagoas_analysis.ipynb  # Análise e visualizações para os dados de Alagoas
│   └── 03_tte_analysis.ipynb      # Análise e visualizações para os dados de TTE
├── src/                      # Módulos Python com funções reutilizáveis
│   ├── data_loader.py        # Funções para carregar dados
│   ├── data_processor.py     # Funções para limpeza e processamento de dados
│   └── visualizer.py         # Funções para gerar visualizações
├── reports/
│   └── figures/              # Figuras e gráficos gerados
├── README.md
├── requirements.txt
```

## Tecnologias Utilizadas
- **Python**
- **Jupyter Notebook**
- **Pandas** para manipulação de dados
- **Matplotlib e Seaborn** para visualização dos dados
- **Numpy** para cálculos estatísticos

## Base de Dados
Os dados utilizados neste projeto foram extraídos das bases oficiais das eleições de 2024, com informações detalhadas sobre o comparecimento e a abstenção dos eleitores em Alagoas. As análises incluem:
- Taxa de comparecimento e abstenção por município
- Comparativo com eleições anteriores
- Distribuição de votantes por zona eleitoral
- Correlação entre fatores socioeconômicos e participação eleitoral

## Visualização de Dados
Para melhor interpretação dos resultados, foram gerados gráficos interativos e estatísticas descritivas que permitem identificar padrões relevantes na participação eleitoral.

## Como Executar o Projeto
1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/evertonreis1/eleicoes-alagoas-2024.git
    ```
2.  **Acesse a pasta do projeto:**
    ```bash
    cd eleicoes-alagoas-2024
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
5.  **Abra os notebooks na seguinte ordem para executar a análise:**
    *   `notebooks/01_data_preparation.ipynb`
    *   `notebooks/02_alagoas_analysis.ipynb`
    *   `notebooks/03_tte_analysis.ipynb`

## Contribuição
Caso queira contribuir com o projeto, fique à vontade para abrir issues e pull requests com sugestões ou melhorias.