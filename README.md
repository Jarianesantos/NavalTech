# Portfolio

Site estático de portfólio pessoal.

## Características

* **Logo** – SVG com gradientes, anéis criptográficos giratórios e a Cifra de César (ROT 3).
* **Descrição** – breve texto sobre o conceito e a aplicação em engenharia de software.
* **Deploy** – pronto para GitHub Pages (`git push` → Settings → Pages).

## Como publicar

```bash
git add .
git commit -m "Add portfolio site"
git push origin main
```

Em seguida, no GitHub: **Settings → Pages → Source: main branch / /(root)**.  
O site ficará disponível no endereço configurado.

## Como Executar Localmente

```bash
npm install
npm start
```

Acesse: [http://localhost:3000](http://localhost:3000)

## Estrutura do Projeto

```
technaval-portfolio/
├── index.html          # Página principal
├── style.css           # Estilos
├── server.js           # Backend
├── package.json        # Dependências
├── package-lock.json   # Lock de dependências
└── technaval_logo.svg  # Logotipo
```