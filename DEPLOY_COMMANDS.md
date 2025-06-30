# 🚀 Scripts de Deploy

## Para Windows (PowerShell)

### 1. Inicializar Git e fazer primeiro commit
```powershell
git init
git add .
git commit -m "Initial commit: Dashboard de Tabagismo e Fatores de Risco"
```

### 2. Conectar ao GitHub (substitua SEU_USUARIO pelo seu username)
```powershell
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/dashboard-tabagismo-streamlit.git
git push -u origin main
```

### 3. Para atualizações futuras
```powershell
git add .
git commit -m "Atualização: descrição das mudanças"
git push origin main
```

## Para Linux/Mac

### 1. Inicializar Git e fazer primeiro commit
```bash
git init
git add .
git commit -m "Initial commit: Dashboard de Tabagismo e Fatores de Risco"
```

### 2. Conectar ao GitHub (substitua SEU_USUARIO pelo seu username)
```bash
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/dashboard-tabagismo-streamlit.git
git push -u origin main
```

### 3. Para atualizações futuras
```bash
git add .
git commit -m "Atualização: descrição das mudanças"
git push origin main
```

---

## 📋 Checklist antes do Deploy

- [ ] Testei a aplicação localmente
- [ ] Criei repositório público no GitHub
- [ ] Fiz push de todos os arquivos
- [ ] Verifiquei se requirements.txt está correto
- [ ] Tenho conta no Streamlit Cloud conectada ao GitHub

## 🔗 Links Diretos

- **GitHub**: [Criar novo repositório](https://github.com/new)
- **Streamlit Cloud**: [Deploy nova app](https://share.streamlit.io)
- **Documentação**: [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
