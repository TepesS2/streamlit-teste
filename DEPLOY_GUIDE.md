# 🚀 Guia de Deploy no Streamlit Cloud

## Passo 1: Preparar o Repositório GitHub

### 1.1 Inicializar Git (se ainda não foi feito)
```bash
git init
git add .
git commit -m "Initial commit: Dashboard de Tabagismo e Fatores de Risco"
```

### 1.2 Criar Repositório no GitHub
1. Vá para [github.com](https://github.com)
2. Clique em "New repository"
3. Nome sugerido: `dashboard-tabagismo-streamlit`
4. Marque como **Público** (necessário para Streamlit Cloud gratuito)
5. **NÃO** adicione README, .gitignore ou license (já temos)
6. Clique "Create repository"

### 1.3 Conectar Repositório Local ao GitHub
```bash
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/dashboard-tabagismo-streamlit.git
git push -u origin main
```

## Passo 2: Deploy no Streamlit Cloud

### 2.1 Acessar Streamlit Cloud
1. Vá para [share.streamlit.io](https://share.streamlit.io)
2. Clique em "Sign in" 
3. Use sua conta GitHub para fazer login

### 2.2 Criar Nova App
1. Clique em "New app"
2. Escolha "From existing repo"
3. Selecione seu repositório: `SEU_USUARIO/dashboard-tabagismo-streamlit`
4. Branch: `main`
5. Main file path: `app.py`
6. App URL (opcional): escolha um nome personalizado

### 2.3 Configurações Avançadas (Opcional)
- **Python version**: 3.11 (será detectado automaticamente pelo runtime.txt)
- **Requirements**: será detectado automaticamente pelo requirements.txt

### 2.4 Deploy
1. Clique em "Deploy!"
2. Aguarde o processo de deploy (pode levar alguns minutos)
3. Sua app estará disponível em: `https://SEU_APP_NAME.streamlit.app`

## Passo 3: Verificação e Troubleshooting

### ✅ Checklist Pré-Deploy
- [x] `requirements.txt` atualizado
- [x] `runtime.txt` criado
- [x] `.streamlit/config.toml` configurado
- [x] Código traduzido e funcionando localmente
- [x] Repositório público no GitHub

### 🔧 Solução de Problemas Comuns

**Erro de Dependências:**
- Verifique se todas as dependências estão no `requirements.txt`
- Use versões específicas se necessário

**Erro de Memória:**
- O dataset será baixado automaticamente na primeira execução
- Pode levar alguns minutos para carregar

**Erro de Timeout:**
- O Streamlit Cloud tem limite de tempo para deploy
- Se necessário, otimize o código para carregamento mais rápido

## Passo 4: Atualizações Futuras

Para atualizar sua app:
```bash
git add .
git commit -m "Atualização: descrição das mudanças"
git push origin main
```

O Streamlit Cloud detectará automaticamente as mudanças e fará redeploy.

## 📱 Compartilhamento

Após o deploy, você pode compartilhar sua app através da URL:
- **URL Pública**: `https://seu-app-name.streamlit.app`
- **Incorporar**: Use iframe em sites
- **Redes Sociais**: Compartilhe diretamente

## 🎯 Próximos Passos Recomendados

1. **Teste a App**: Verifique todas as funcionalidades
2. **Documentação**: Atualize README.md com a URL da app
3. **Monitoramento**: Use analytics do Streamlit Cloud
4. **Feedback**: Colete feedback de usuários para melhorias

---

**🔗 Links Úteis:**
- [Documentação Streamlit Cloud](https://docs.streamlit.io/streamlit-cloud)
- [Troubleshooting](https://docs.streamlit.io/streamlit-cloud/troubleshooting)
- [Limites e Quotas](https://docs.streamlit.io/streamlit-cloud/get-started#resource-limits)
