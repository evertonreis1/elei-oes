# 📊 Análise Aprofundada de Dados Eleitorais Brasileiros

## Desvendando Padrões de Comparecimento e Abstenção

Este repositório é um projeto abrangente dedicado à análise de dados eleitorais brasileiros, com foco principal em compreender os padrões de comparecimento e abstenção de eleitores. Utilizando dados do Tribunal Superior Eleitoral (TSE), buscamos identificar tendências, fatores influenciadores e insights valiosos sobre o comportamento eleitoral.

---

### ✨ Destaques do Projeto

*   **Análise Detalhada:** Explore notebooks Jupyter com análises aprofundadas sobre comparecimento e abstenção.
*   **Visualizações Interativas:** Geração de gráficos e visualizações para facilitar a compreensão dos dados.
*   **Estrutura Modular:** Código organizado em módulos Python para carregamento, processamento e visualização de dados.
*   **Foco em Alagoas:** Análise específica para o estado de Alagoas, permitindo insights regionais.
*   **Dados Abertos do TSE:** Utilização de dados públicos e oficiais para garantir a transparência e replicabilidade.

---

### 📁 Estrutura do Repositório

*   `data/`: Armazena os conjuntos de dados utilizados no projeto.
    *   `raw/`: Contém os dados brutos originais, diretamente do TSE.
    *   `processed/`: Dados limpos e transformados, prontos para análise.
*   `notebooks/`: Notebooks Jupyter que guiam a exploração e análise dos dados.
    *   `01_data_preparation.ipynb`: Etapas de pré-processamento, limpeza e engenharia de features dos dados.
    *   `02_alagoas_analysis.ipynb`: Análise exploratória e inferencial focada nos dados eleitorais de Alagoas.
    *   `03_tte_analysis.ipynb`: Análise geral dos dados do Tribunal Superior Eleitoral (TSE).
*   `src/`: Scripts Python contendo funções reutilizáveis para o projeto.
    *   `data_loader.py`: Módulo responsável por carregar os dados de diferentes fontes.
    *   `data_processor.py`: Módulo com funções para processar, limpar e transformar os dados.
    *   `visualizer.py`: Módulo dedicado à criação de visualizações e gráficos.
*   `reports/`: Contém os resultados das análises, como relatórios e figuras geradas.
    *   `figures/`: Armazena os gráficos e visualizações exportados dos notebooks.
*   `requirements.txt`: Lista de todas as bibliotecas Python necessárias para executar o projeto.
*   `README.md`: Este arquivo, fornecendo uma visão geral do projeto.

---

### 🚀 Como Começar

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/evertonreis1/elei-oes.git
    cd elei-oes
    ```

2.  **Crie e Ative um Ambiente Virtual (Altamente Recomendado):**
    Isso garante que as dependências do projeto não interfiram com outras instalações Python em seu sistema.

    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os Notebooks Jupyter:**
    Após a instalação das dependências, você pode abrir e executar os notebooks para replicar as análises.

    ```bash
    jupyter notebook
    ```
    Seu navegador padrão será aberto com a interface do Jupyter. Navegue até a pasta `notebooks/` e abra os arquivos `.ipynb`.

---

### 📊 Dados

Os dados utilizados neste projeto são públicos e foram obtidos diretamente do [Tribunal Superior Eleitoral (TSE)](https://www.tse.jus.br/eleicoes/estatisticas/repositorio-de-dados-eleitorais). Eles incluem informações detalhadas sobre o perfil do eleitorado, comparecimento e abstenção em diversas eleições.

---

### 🤝 Contribuição

Contribuições são muito bem-vindas! Se você tiver ideias para melhorias, novas análises ou encontrar algum bug, sinta-se à vontade para:

1.  Abrir uma [Issue](https://github.com/evertonreis1/elei-oes/issues) para discutir a mudança proposta.
2.  Criar um [Pull Request](https://github.com/evertonreis1/elei-oes/pulls) com suas alterações.

Por favor, certifique-se de seguir as convenções de código existentes e adicionar testes, se aplicável.

---

### 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### 📧 Contato

Para dúvidas ou sugestões, entre em contato com [itsevertonreis@gmail.com](Everton Reis).
