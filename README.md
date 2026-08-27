# NavalTech - Portfolio

Portfólio profissional de Jariane Santos - Desenvolvedora Full Stack especializada em soluções marítimas e inteligência artificial.

## Sobre o Projeto

Este é um portfólio web completo desenvolvido para apresentar projetos e serviços de desenvolvimento de software, com foco no setor marítimo e naval. O site inclui sistema de autenticação, notificações por email e design responsivo com tema marítimo.

## Funcionalidades

- **Design Responsivo** - Layout adaptável para desktop, tablet e mobile
- **Tema Marítimo** - Paleta de cores inspirada no oceano (azul-marinho, branco gelo)
- **Sistema de Autenticação** - Login e cadastro de usuários com senhas hasheadas (bcrypt)
- **Notificações por Email** - Alertas automáticos via nodemailer
- **Formulário de Contato** - Envio de mensagens diretamente por email
- **Projetos do GitHub** - Integração com repositórios reais
- **Animações Suaves** - Barras de habilidades animadas no scroll
- **Menu Mobile** - Navegação responsiva com hamburger menu

## Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Node.js, Express 5
- **Segurança:** bcrypt (hash de senhas), dotenv (variáveis de ambiente)
- **Email:** Nodemailer
- **Fonte:** Times New Roman
- **Ícones:** Font Awesome 6

## Estrutura do Projeto

```
NavalTech/
├── public/                 # Arquivos estáticos
│   ├── index.html          # Página principal
│   ├── style.css           # Estilos CSS
│   └── technaval_logo.svg  # Logotipo SVG
├── server.js               # Backend Node.js/Express
├── .env                    # Variáveis de ambiente (não commitado)
├── .gitignore              # Arquivos ignorados pelo Git
├── package.json            # Dependências
├── gerar_projetos.py       # Gerador de projetos (Python)
├── projetos_gerados.html   # HTML gerado pelo script
└── README.md               # Este arquivo
```

## Como Executar Localmente

### Pré-requisitos
- Node.js (v18 ou superior)
- npm

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/Jarianesantos/NavalTech.git

# Navegar até o diretório
cd NavalTech

# Instalar dependências
npm install

# Criar arquivo .env (copiar do exemplo)
cp .env.example .env

# Iniciar o servidor
npm start
```

Acesse: [http://localhost:3000](http://localhost:3000)

### Arquivo .env

O arquivo `.env` contém as configurações sensíveis e não deve ser commitado. Crie um com as seguintes variáveis:

```env
PORT=3000
EMAIL_USER=seu-email@gmail.com
EMAIL_PASS=sua-senha-de-app
LOGIN_EMAIL=seu-email@gmail.com
LOGIN_PASSWORD=sua-senha
LOGIN_NAME=Seu Nome
```

## Scripts Úteis

### Gerar Projetos (Python)

O script `gerar_projetos.py` gera automaticamente a seção de projetos do portfólio:

```bash
python gerar_projetos.py
```

Isso criará o arquivo `projetos_gerados.html` com a seção de projetos atualizada.

## Deploy

### GitHub Pages

1. Faça push para o repositório
2. Acesse **Settings → Pages**
3. Selecione a branch `main` e pasta `/ (root)`
4. O site estará disponível no endereço configurado

### Deploy com Node.js

```bash
# Instalar dependências
npm install

# Iniciar em produção
npm start
```

## Segurança

- ✅ Senhas hasheadas com bcrypt
- ✅ Variáveis de ambiente em arquivo `.env`
- ✅ `.env` não é commitado no Git
- ✅ Arquivos estáticos servidos apenas da pasta `public/`
- ✅ Validação de entrada em todos os endpoints

## Projetos em Destaque

| Projeto | Categoria | Tecnologias |
|---------|-----------|-------------|
| NavalTech Platform | Sistema Web | Node.js, Express, HTML5, CSS3 |
| IANaval | Inteligência Artificial | Python, scikit-learn, Pandas |
| SeaGuardian | Inteligência Artificial | Python, TensorFlow, OpenCV |
| PSV Hybrid Propulsion | Sistemas Embarcados | Python, Arduino, IoT |
| OptimarineAI | Inteligência Artificial | Python, TensorFlow |
| Maritime Data Platform | Ciência de Dados | Python, GeoPandas, PostgreSQL |

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

**Jariane Santos**
- Email: jarianenaval@gmail.com
- GitHub: [github.com/Jarianesantos](https://github.com/Jarianesantos)
- LinkedIn: [linkedin.com/in/jariane-santos-b2921a1b2](https://linkedin.com/in/jariane-santos-b2921a1b2)