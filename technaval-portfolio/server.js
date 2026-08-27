const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Simulação de "base de dados" de usuários
const users = [
  { email: 'admin@technaval.com', password: 'admin123' },
  { email: 'user@technaval.com', password: 'user123' }
];

// Configuração de middlewares
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname)));

// Rota de login
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: 'Email e senha são obrigatórios.' });
  }

  const user = users.find(
    u => u.email === email && u.password === password
  );

  if (user) {
    // Em um sistema real, você usaria JWT ou OAuth aqui
    res.json({ message: 'Login bem-sucedido!', success: true });
  } else {
    res.status(401).json({ message: 'Credenciais inválidas.' });
  }
});

// Inicia o servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});