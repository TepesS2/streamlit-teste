<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Instruções do Projeto Dashboard Streamlit

Este é um projeto de dashboard interativo baseado em Streamlit para análise de dados de tabagismo e fatores de risco.

## Contexto do Projeto
- **Framework**: Streamlit para dashboard web
- **Visualização**: Plotly para gráficos interativos
- **Dados**: Dataset do Kaggle sobre tabagismo e fatores de risco (2000+ registros)
- **Linguagem**: Python 3.8+

## Diretrizes de Estilo de Código
- Use melhores práticas do Streamlit para cache com `@st.cache_data`
- Implemente design responsivo com `st.columns()` e `st.container()`
- Siga convenções de nomenclatura PEP 8
- Use type hints quando apropriado
- Adicione docstrings a todas as funções

## Padrões de Arquitetura
- **App principal**: `app.py` contém a lógica principal do dashboard
- **Páginas**: Páginas adicionais no diretório `/pages/` para apps multi-página
- **Utils**: Funções auxiliares em `/utils/` para processamento de dados e visualizações
- **Dados**: Armazenamento local de dados no diretório `/data/`

## Diretrizes Específicas do Streamlit
- Use `st.set_page_config()` para configuração de página
- Implemente tratamento adequado de erros para carregamento de dados
- Use session state para manter estados de filtros
- Organize layouts com sidebars e colunas
- Adicione indicadores de carregamento para operações demoradas

## Requisitos de Visualização
- Mínimo de 6 gráficos com pelo menos 2 interativos (Plotly)
- Inclua filtros que afetam todas as visualizações
- Use esquemas de cores consistentes e estilização
- Garanta responsividade móvel
- Adicione tooltips hover e anotações

## Tratamento de Dados
- Cache operações de carregamento de dados
- Implemente tratamento adequado de erros para dados ausentes
- Use pandas para manipulação de dados
- Limpe e pré-processe dados adequadamente
- Trate valores ausentes graciosamente

## Considerações de Performance
- Use `@st.cache_data` para operações custosas
- Minimize processamento de dados na thread principal
- Otimize renderização de gráficos com amostragem adequada de dados
- Implemente lazy loading quando possível
