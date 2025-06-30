# 🚀 Guia Completo: Deploy do Dashboard no Streamlit Cloud

## ⚠️ Pré-requisitos

### 1. Instalar Git (se não estiver instalado)

**Windows:**
1. Baixe o Git em: [git-scm.com](https://git-scm.com/download/windows)
2. Execute o instalador
3. Nas opções, deixe as configurações padrão
4. Reinicie o VS Code após a instalação

**Verificar instalação:**
```bash
git --version
```

### 2. Configurar Git (primeira vez)
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@gmail.com"
```

## 📋 Passo a Passo Completo

### Passo 1: Criar Repositório no GitHub

1. **Acesse**: [github.com](https://github.com)
2. **Faça login** ou crie uma conta
3. **Clique** em "New repository" (botão verde)
4. **Configure**:
   - Repository name: `dashboard-tabagismo-streamlit`
   - Description: "Dashboard interativo para análise de tabagismo e fatores de risco"
   - ✅ Public (obrigatório para Streamlit Cloud gratuito)
   - ❌ NÃO marque "Add a README file"
   - ❌ NÃO marque "Add .gitignore"
   - ❌ NÃO marque "Choose a license"
5. **Clique** "Create repository"

### Passo 2: Comandos Git (Execute no Terminal do VS Code)

**Após instalar o Git, execute um comando por vez:**

```bash
# 1. Inicializar repositório Git
git init

# 2. Adicionar todos os arquivos
git add .

# 3. Fazer primeiro commit
git commit -m "Initial commit: Dashboard de Tabagismo e Fatores de Risco"

# 4. Configurar branch principal
git branch -M main

# 5. Conectar ao repositório GitHub (SUBSTITUA 'SEU_USUARIO')
git remote add origin https://github.com/SEU_USUARIO/dashboard-tabagismo-streamlit.git

# 6. Enviar código para GitHub
git push -u origin main
```

### Passo 3: Deploy no Streamlit Cloud

1. **Acesse**: [share.streamlit.io](https://share.streamlit.io)
2. **Clique** "Sign in with GitHub"
3. **Autorize** o Streamlit Cloud a acessar sua conta GitHub
4. **Clique** "New app"
5. **Configure**:
   - Repository: `SEU_USUARIO/dashboard-tabagismo-streamlit`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: (opcional) `dashboard-tabagismo-seu-nome`
6. **Clique** "Deploy!"

### Passo 4: Aguardar Deploy

- ⏱️ **Tempo estimado**: 2-5 minutos
- 📊 **Status**: Acompanhe o log de deploy
- 🚀 **URL final**: `https://seu-app-name.streamlit.app`

## 🔧 Alternativa: Deploy Manual

Se preferir fazer manualmente pelo GitHub web:

### 1. Criar arquivo no GitHub
1. Vá para seu repositório no GitHub
2. Clique "uploading an existing file"
3. Arraste todos os arquivos do projeto
4. Commit: "Add dashboard files"

### 2. Depois siga o Passo 3 acima

## 📱 Resultado Final

Após o deploy, você terá:
- ✅ **URL pública** para compartilhar
- ✅ **Dashboard totalmente funcional**
- ✅ **Atualizações automáticas** (quando fizer push no GitHub)
- ✅ **Hospedagem gratuita**

## 🆘 Precisa de Ajuda?

1. **Git não encontrado**: Instale o Git e reinicie o VS Code
2. **Erro de permissão GitHub**: Verifique se o repositório é público
3. **Erro no deploy**: Verifique o log no Streamlit Cloud
4. **App não carrega**: Pode levar alguns minutos na primeira vez

---

## 🎯 Links Importantes

- **Seu repositório**: `https://github.com/SEU_USUARIO/dashboard-tabagismo-streamlit`
- **Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io)
- **Documentação**: [docs.streamlit.io](https://docs.streamlit.io/streamlit-cloud)

**💡 Dica**: Marque este guia para futuras referências!
