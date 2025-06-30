# Guia de Deploy no Streamlit Cloud

## Deploy Rápido no Streamlit Cloud

1. **Envie seu código para o GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Commit inicial: Dashboard de tabagismo Streamlit"
   git branch -M main
   git remote add origin https://github.com/seuusuario/dashboard-tabagismo.git
   git push -u origin main
   ```

2. **Deploy no Streamlit Cloud:**
   - Vá para [share.streamlit.io](https://share.streamlit.io)
   - Faça login com GitHub
   - Clique em "New app"
   - Selecione seu repositório
   - Escolha `app.py` como arquivo principal
   - Clique em "Deploy!"

## Variáveis de Ambiente (se necessário)
Nenhuma variável de ambiente é necessária para esta aplicação.

## Requisitos
Todas as dependências estão listadas em `requirements.txt` e serão automaticamente instaladas durante o deploy.

## Performance Esperada
- Primeiro carregamento pode levar 30-60 segundos para download do dataset
- Carregamentos subsequentes serão mais rápidos devido ao cache
- Recursos interativos respondem em tempo real
