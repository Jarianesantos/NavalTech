// Simple Node.js/Express server for Portfolio backend
const express = require('express');
const cors = require('cors');
const path = require('path');
const nodemailer = require('nodemailer');

const app = express();
const PORT = process.env.PORT || 3000;

// Configuração do email (Gmail SMTP)
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'jarianenaval@gmail.com',
    pass: 'QVOUQHYP' // Senha de app do Gmail
  }
});

// Simulated database of users
const users = [
  { email: 'jarianenaval@gmail.com', password: 'QVOUQHYP', name: 'Jariane Santos' }
];

// Função para enviar email de notificação
async function sendNotificationEmail(userData) {
  const mailOptions = {
    from: 'jarianenaval@gmail.com',
    to: 'jarianenaval@gmail.com',
    subject: 'Novo cadastro no Portfolio',
    html: `
      <h2>Novo cliente cadastrado!</h2>
      <p><strong>Nome:</strong> ${userData.name}</p>
      <p><strong>Email:</strong> ${userData.email}</p>
      <p><strong>Data:</strong> ${new Date().toLocaleString('pt-BR')}</p>
    `
  };

  try {
    await transporter.sendMail(mailOptions);
    console.log('Email de notificação enviado para jarianenaval@gmail.com');
  } catch (error) {
    console.error('Erro ao enviar email:', error);
  }
}

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname)));

// Login API endpoint
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: 'Email e senha são obrigatórios.' });
  }

  const user = users.find(
    u => u.email === email && u.password === password
  );

  if (user) {
    res.json({ message: 'Login realizado com sucesso!', success: true });
  } else {
    res.status(401).json({ message: 'Credenciais inválidas.' });
  }
});

// Register API endpoint
app.post('/api/register', async (req, res) => {
  const { name, email, password, confirmPassword } = req.body;

  if (!name || !email || !password || !confirmPassword) {
    return res.status(400).json({ message: 'Todos os campos são obrigatórios.' });
  }

  if (password !== confirmPassword) {
    return res.status(400).json({ message: 'As senhas não coincidem.' });
  }

  if (password.length < 6) {
    return res.status(400).json({ message: 'A senha deve ter pelo menos 6 caracteres.' });
  }

  const existingUser = users.find(u => u.email === email);
  if (existingUser) {
    return res.status(409).json({ message: 'Este email já está cadastrado.' });
  }

  // Add new user
  const newUser = { email, password, name };
  users.push(newUser);

  // Envia email de notificação
  await sendNotificationEmail(newUser);

  res.json({ message: 'Cadastro realizado com sucesso!', success: true });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
  console.log('Notificações enviadas para: jarianenaval@gmail.com');
});
