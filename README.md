# Matheus Caixeta Reis
**Engenheiro de Software · Automação & Identidade · Segurança da Informação**  
São Paulo, SP • [caixeta2602@gmail.com](mailto:caixeta2602@gmail.com) • [LinkedIn](https://www.linkedin.com/in/matheus-caixeta-5287ba201/) • [GitHub](https://github.com/caixeta7)

---

## 👨‍💻 Sobre Mim
Analista de TI com foco em **gestão de identidades (AD/Entra ID)**, **automação operacional** (PowerShell/Python) e **desenvolvimento de ferramentas internas**.  
Atualmente cursando **Pós-graduação em Segurança da Informação** (Senac), aplicando governança de acessos e hardening em ambientes corporativos.

> "Transformo processos manuais repetitivos em ferramentas confiáveis, auditáveis e escaláveis."

---

## 🛠️ Tecnologias & Domínios

| Categoria | Stack |
|-----------|-------|
| **Identidade & Acesso** | Active Directory, Microsoft 365 / Entra ID, RBAC, provisionamento |
| **Automação & Scripting** | PowerShell (RunspacePool, WinRM), Python (CLI, Tkinter, Flask), Bash |
| **Desenvolvimento Web** | Flask, React 18 + TypeScript + Vite, Tailwind CSS, SQLite/PostgreSQL |
| **Infra & Segurança** | Windows Server, Linux básico, Hardening (TLS, Registry, GPO), WMI/CIM |
| **Observabilidade** | Logging estruturado, relatórios Excel/CSV, dashboards em tempo real |

---

## 📌 Projetos Fixados (Pinned)

| Projeto | Descrição | Stack | Status |
|---------|-----------|-------|--------|
| [**painel-inventario-corporativo**](https://github.com/caixeta7/painel-inventario-corporativo) | Dashboard web (Flask + SQLite + WMI) para monitoramento de parque Windows em tempo real — 50+ atributos/máquina, filtros dinâmicos, exportação CSV | `Python` `Flask` `SQLite` `WMI` `Chart.js` | ![Public](https://img.shields.io/badge/Public-2ea44f?style=flat-square) |
| [**uptime-checker-massa**](https://github.com/caixeta7/uptime-checker-massa) | Verificador de uptime paralelo (PowerShell RunspacePool 80 threads) — Auditoria de frota 500+ máquinas em <3min, relatório Excel formatado | `PowerShell` `RunspacePool` `OpenXML` `Active Directory` | ![Public](https://img.shields.io/badge/Public-2ea44f?style=flat-square) |
| [**coletor-perfil-remoto**](https://github.com/caixeta7/coletor-perfil-remoto) | Migração de perfis Windows (Python/Tkinter + SMB/Robocopy) — Interface gráfica, execução assíncrona, tratamento de ACLs/arquivos em uso | `Python` `Tkinter` `SMB` `Robocopy` `Threading` | ![Public](https://img.shields.io/badge/Public-2ea44f?style=flat-square) |
| [**phishcheck**](https://github.com/caixeta7/phishcheck) | Detector de phishing/spam (FastAPI + React) — Heurísticas offline + Threat Intel (VirusTotal, Google Safe Browsing, AbuseIPDB) | `FastAPI` `React` `TypeScript` `Tailwind` `Security` | ![Public](https://img.shields.io/badge/Public-2ea44f?style=flat-square) |
| [**inventario-ti-dashboard**](https://github.com/caixeta7/inventario-ti-dashboard) | Sistema de inventário TI (React 18 + TypeScript + Tailwind + Vite) — 4 abas, filtros avançados, dark mode, PWA ready | `React` `TypeScript` `Tailwind` `Vite` `PWA` | ![Public](https://img.shields.io/badge/Public-2ea44f?style=flat-square) |
| [**backup-perfil-usuario**](https://github.com/caixeta7/backup-perfil-usuario) | Backup completo com suporte OneDrive corporativo/pessoal, logging estruturado, relatório HTML | `PowerShell` `OneDrive` `Robocopy` `Logging` | ![Public](https://img.shields.io/badge/Public-2ea44f?style=flat-square) |

> 💡 **Nota:** Os 6 repositórios acima estão fixados no perfil. Acesse a aba **Repositories → Pinned** para ver a seleção oficial.

---

## 🚀 Projetos em Destaque

### `painel-inventario-corporativo`
**Dashboard corporativo (Flask + SQLite + WMI)** — Monitoramento de parque Windows em tempo real com inventário de hardware/software.

`Python` `Flask` `SQLite` `WMI` `JavaScript` `Chart.js`

- Coleta automática via WMI/CIM de 50+ atributos por máquina
- Interface responsiva com filtros dinâmicos e exportação CSV
- Agendamento via Windows Task Scheduler / systemd
- [Código](https://github.com/caixeta7/painel-inventario-corporativo)

---

### `uptime-checker-massa`
**Verificador de uptime paralelo (PowerShell + RunspacePool)** — 80 threads para auditoria de frota Windows com relatório Excel.

`PowerShell` `RunspacePool` `Excel` `OpenXML` `Active Directory`

- Varredura de 500+ máquinas em < 3 min
- Detecção de usuário logado, último boot, status de rede
- Relatório formatado com formatação condicional
- [Código](https://github.com/caixeta7/uptime-checker-massa)

---

### `coletor-perfil-remoto`
**Migração de perfis Windows (Python/Tkinter + SMB/Robocopy)** — Desktop app para coleta/migração de perfis entre máquinas via rede.

`Python` `Tkinter` `SMB` `Robocopy` `Threading` `Logging`

- Interface gráfica para seleção de origem/destino
- Execução assíncrona com progresso em tempo real
- Tratamento de arquivos em uso, perfis corrompidos, ACLs
- [Código](https://github.com/caixeta7/coletor-perfil-remoto)

---

### `phishcheck`
**Detecção de phishing (FastAPI + React + Threat Intel)** — Análise de e-mails, URLs e domínios com heurísticas offline + APIs gratuitas (VirusTotal, Google Safe Browsing, AbuseIPDB).

`Python` `FastAPI` `React` `TypeScript` `Tailwind` `VirusTotal` `Google Safe Browsing`

- Heurísticas offline: punycode, encurtadores, TLDs suspeitos, engenharia social, SPF/DMARC
- Verificações online: DNS, WHOIS, 70+ motores AV, reputação de IP
- Fallback gracioso quando APIs não configuradas
- [Código](https://github.com/caixeta7/phishcheck)

---

### `inventario-ti-dashboard`
**Sistema de inventário TI (React 18 + Tailwind + Vite)** — 4 abas, filtros avançados, dark mode, PWA ready.

`React 18` `TypeScript` `Tailwind` `Vite` `PWA` `IndexedDB`

- CRUD completo de ativos com validação em tempo real
- Filtros combinados por múltiplas colunas
- Modo offline com sincronização posterior
- [Código](https://github.com/caixeta7/inventario-ti-dashboard)

---

### `echo`
**Template React + TypeScript + Vite + Oxlint** — Base configurada para projetos profissionais com linting rigoroso.

`React` `TypeScript` `Vite` `Oxlint` `ESLint` `Prettier`

- Configuração zero-config para times
- Regras estritas de hooks, imports, acessibilidade
- [Código](https://github.com/caixeta7/echo)

---

## 📦 Automação & Segurança (PowerShell / Python)

| Projeto | Stack | Descrição |
|---------|-------|-----------|
| `backup-perfil-usuario` | PowerShell | Backup completo com suporte OneDrive corporativo/pessoal, logging estruturado, relatório HTML |
| `hardening-phonelink` | PowerShell | Desativação de Phone Link via Registry Policy (prevenção vazamento dados) |
| `fix-tls12-dotnet` | Registry/.NET | Força TLS 1.2 em apps .NET Framework 4.x (compliance) |
| `upgrade-windows11-automatizado` | PowerShell | Validação TPM 2.0 + Secure Boot + upgrade silencioso |
| `ingressar-dominio` | PowerShell | Join AD interativo com validação DNS e renomeação |
| `assinatura-email-ad` | VBScript | Gera assinatura Outlook lendo atributos do AD via LDAP |
| `painel-impressoras` | Flask + JS | Monitoramento de impressoras em rede via ping paralelo |
| `biblioteca-pessoal-cli` | Python | Gerenciador de biblioteca pessoal via terminal (CRUD, busca normalizada, JSON) |
| `otimizador-rotas` | FastAPI + OR-Tools | Otimizador de rotas Shopee/Circuit — redução ~35% distância via TSP real (OSRM + OR-Tools) |

---

## 📊 GitHub Analytics

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=caixeta7&show_icons=true&theme=github_dark&hide_border=true&count_private=true&include_all_commits=true&locale=pt-br&custom_title=Visão%20Geral&title_color=58a6ff&text_color=c9d1d9&icon_color=58a6ff&bg_color=0d1117&border_color=30363d)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=caixeta7&layout=compact&theme=github_dark&hide_border=true&langs_count=10&title_color=58a6ff&text_color=c9d1d9&bg_color=0d1117&border_color=30363d&custom_title=Linguagens%20Mais%20Usadas)

</div>

<div align="center">

![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=caixeta7&theme=github-dark&hide_border=true&date_format=j%20M%5B%20Y%5D&background=0d1117&border=30363d&stroke=58a6ff&ring=58a6ff&fire=58a6ff&currStreakLabel=58a6ff&sideNums=c9d1d9&currStreakNum=58a6ff&sideLabels=c9d1d9)

</div>

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=caixeta7&label=Visualizações%20do%20Perfil&color=58a6ff&style=flat-square)

</div>

---

## 📈 Atividade Recente

<!--START_SECTION:activity-->
<!--STATS_UPDATED: 2026-08-23 03:39:22 UTC -->
<!--STATS_UPDATED: 2026-08-22 03:31:12 UTC -->
<!--STATS_UPDATED: 2026-08-21 03:39:23 UTC -->
<!--STATS_UPDATED: 2026-08-20 03:35:52 UTC -->
<!-- Esta seção é atualizada automaticamente via GitHub Actions -->
<!--END_SECTION:activity-->

---

## 📫 Contato

<div align="center">

[![E-mail](https://img.shields.io/badge/E--mail-caixeta2602@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:caixeta2602@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-matheus--caixeta--5287ba201-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-caixeta-5287ba201/)
[![GitHub](https://img.shields.io/badge/GitHub-caixeta7-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/caixeta7)

</div>

---

<details>
<summary>💡 <strong>Curiosidades & Foco Técnico</strong></summary>

- 🎯 **Foco principal**: Automação de infraestrutura Windows, segurança ofensiva/defensiva, dashboards operacionais
- ⚡ **Produtividade**: Scripts PowerShell paralelos (RunspacePool 80 threads), automação AD/Registry/WMI
- 🔒 **Segurança**: Hardening TLS, desativação de vetores de ataque (Phone Link), auditoria de phishing, Threat Intel
- 📚 **Aprendizado contínuo**: Rust, Kubernetes, arquitetura distribuída, engenharia de chaos
- 🏗️ **Arquitetura**: Clean Architecture, Domain-Driven Design, SOLID, testes automatizados, type-safety

</details>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,58a6ff,1f6feb&height=100&section=footer&animation=fadeIn" alt="Footer" />
</p>

<p align="center">
  <sub>⭐ Star nos repositórios que achar úteis • 🔄 Perfil atualizado automaticamente via GitHub Actions • 🛡️ Segurança e qualidade em primeiro lugar</sub>
</p>

















