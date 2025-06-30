# 🚭 Dashboard de Tabagismo e Fatores de Risco

Um dashboard interativo em Streamlit para explorar padrões de tabagismo e fatores de risco associados através de visualização abrangente de dados.

## 📋 Visão Geral do Projeto

Este dashboard analisa um dataset abrangente sobre hábitos de tabagismo e fatores de risco relacionados, fornecendo insights sobre:
- Prevalência de tabagismo em diferentes demografias
- Métricas de saúde e sua correlação com status de tabagismo
- Fatores de risco e padrões de estilo de vida
- Capacidades de exploração interativa de dados

## 🚀 Funcionalidades

- **📊 6+ Visualizações Interativas**: Incluindo gráficos de pizza, histogramas, box plots, matrizes de correlação e gráficos de dispersão customizados
- **🔍 Navegação Multi-página**: Organizada em seções lógicas para fácil exploração
- **⚙️ Filtros Dinâmicos**: Filtragem em tempo real por idade, gênero, status de tabagismo e outras variáveis
- **📱 Design Responsivo**: Funciona em dispositivos desktop e móveis
- **🎨 Interface Moderna**: Interface limpa e profissional com estilo personalizado

## 📁 Estrutura do Projeto

```
trabalho/
├── app.py                          # Arquivo principal da aplicação
├── requirements.txt                # Dependências Python
├── README.md                      # Documentação do projeto
├── data/                          # Diretório de armazenamento de dados
├── pages/                         # Páginas adicionais do Streamlit
│   ├── 1_Advanced_Analytics.py    # Página de análises avançadas
│   └── 2_Data_Export.py          # Funcionalidade de exportação de dados
└── utils/                         # Funções utilitárias
    ├── data_processing.py         # Limpeza e processamento de dados
    └── visualizations.py          # Funções de criação de gráficos
```

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- Git (para clonar o repositório)

### Passos de Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-seu-repositorio>
   cd trabalho
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

5. **Acesse o dashboard**
   Abra seu navegador web e navegue para `http://localhost:8501`

## 📊 Páginas do Dashboard

### 🏠 Início
- Visão geral do projeto e documentação
- Informações do dataset e dados de amostra
- Instruções de navegação

### 📈 Análise Geral
- Estatísticas gerais de tabagismo
- Distribuições de idade e demográficas
- Indicadores chave de performance

### 🔍 Análise Demográfica
- Padrões de tabagismo por gênero e faixas etárias
- Correlações de nível educacional
- Análise de segmentos populacionais

### 🏥 Métricas de Saúde
- Distribuições de IMC por status de tabagismo
- Correlações de condições de saúde
- Avaliações de risco médico

### 🎯 Fatores de Risco
- Análise de fatores de estilo de vida
- Matrizes de correlação de risco
- Insights preditivos

### 📊 Explorador Interativo
- Gráficos de dispersão customizáveis
- Seleção dinâmica de variáveis
- Filtragem em tempo real

## 🔧 Como os Filtros Funcionam

O dashboard inclui vários filtros interativos que afetam todas as visualizações:

- **Slider de Faixa Etária**: Filtra participantes por faixa etária
- **Seleção de Gênero**: Foca em grupos de gênero específicos
- **Status de Tabagismo**: Inclui/exclui diferentes categorias de tabagismo
- **Atualizações em Tempo Real**: Todos os gráficos atualizam automaticamente quando os filtros mudam

## 📈 Principais Visualizações

1. **Gráfico de Pizza do Status de Tabagismo** (Interativo)
2. **Histograma de Distribuição de Idade**
3. **Gráfico de Barras Gênero vs Tabagismo**
4. **Box Plots de IMC por Status de Tabagismo** (Interativo)
5. **Mapa de Calor de Correlação**
6. **Explorador de Gráfico de Dispersão Personalizado** (Totalmente Interativo)

## 🌐 Deploy

### Deploy no Streamlit Cloud

1. **Envie para o GitHub**
   ```bash
   git add .
   git commit -m "Setup inicial do dashboard"
   git push origin main
   ```

2. **Deploy no Streamlit Cloud**
   - Visite [share.streamlit.io](https://share.streamlit.io)
   - Conecte seu repositório GitHub
   - Selecione o arquivo `app.py`
   - Deploy!

### Opções Alternativas de Deploy
- **Heroku**: Use o `requirements.txt` incluído
- **AWS/GCP**: Deploy como aplicação containerizada
- **Rede Local**: Use `streamlit run app.py --server.address 0.0.0.0`

## 📦 Dependências

- **streamlit** >= 1.28.0: Framework web para o dashboard
- **pandas** >= 2.0.0: Manipulação e análise de dados
- **plotly** >= 5.15.0: Visualizações interativas
- **numpy** >= 1.24.0: Computações numéricas
- **kagglehub** >= 0.2.0: Funcionalidade de download de dataset

## 📊 Informações do Dataset

**Fonte**: [Dataset de Tabagismo e Outros Fatores de Risco](https://www.kaggle.com/datasets/khushikyad001/smoking-and-other-risk-factors-dataset)

**Tamanho**: 2000+ registros atendendo aos requisitos do projeto

**Características**: Informações demográficas, métricas de saúde, fatores de estilo de vida e status de tabagismo

## 🤝 Contribuindo

1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

Criado como parte de um projeto de visualização interativa de dados.

## 🆘 Suporte

Se você encontrar algum problema:

1. Verifique se todas as dependências estão instaladas corretamente
2. Certifique-se de ter uma conexão estável com a internet para download do dataset
3. Verifique compatibilidade da versão do Python
4. Verifique a saída do terminal para mensagens de erro específicas

Para ajuda adicional, por favor crie uma issue no repositório GitHub.

---

**Feliz Exploração de Dados! 📊🚭**
