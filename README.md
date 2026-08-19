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

## 📦 Projetos de Automação & Segurança

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

---

## 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=caixeta7&show_icons=true&theme=default&hide_border=true&count_private=true&include_all_commits=true&locale=pt-br)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=caixeta7&layout=compact&theme=default&hide_border=true&langs_count=8)

---

## 📫 Contato

| Canal | Link |
|-------|------|
| **E-mail** | [caixeta2602@gmail.com](mailto:caixeta2602@gmail.com) |
| **LinkedIn** | [linkedin.com/in/matheus-caixeta-5287ba201](https://www.linkedin.com/in/matheus-caixeta-5287ba201/) |
| **GitHub** | [github.com/caixeta7](https://github.com/caixeta7) |

---

> *Perfil mantido com foco em qualidade sobre quantidade. Projetos arquivados/antigos removidos da vitrine principal.*