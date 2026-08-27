// Simple Node.js/Express server for Portfolio backend
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const path = require('path');
const nodemailer = require('nodemailer');
const bcrypt = require('bcryptjs');

const app = express();
const PORT = process.env.PORT || 3000;

// Configuração do email (Gmail SMTP)
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS
  }
});

// Simulated database of users (with hashed passwords)
const users = [
  { 
    email: process.env.LOGIN_EMAIL, 
    password: bcrypt.hashSync(process.env.LOGIN_PASSWORD, 10), 
    name: process.env.LOGIN_NAME 
  }
];

// Função para enviar email de notificação
async function sendNotificationEmail(userData) {
  const mailOptions = {
    from: process.env.EMAIL_USER,
    to: process.env.EMAIL_USER,
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
    console.log('Email de notificação enviado para', process.env.EMAIL_USER);
  } catch (error) {
    console.error('Erro ao enviar email:', error);
  }
}

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Servir apenas arquivos estáticos da pasta public
app.use(express.static(path.join(__dirname, 'public')));

// Login API endpoint
app.post('/api/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: 'Email e senha são obrigatórios.' });
  }

  const user = users.find(u => u.email === email);

  if (user && await bcrypt.compare(password, user.password)) {
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

  // Add new user with hashed password
  const hashedPassword = await bcrypt.hash(password, 10);
  const newUser = { email, password: hashedPassword, name };
  users.push(newUser);

  // Envia email de notificação
  await sendNotificationEmail(newUser);

  res.json({ message: 'Cadastro realizado com sucesso!', success: true });
});

// Contact form endpoint
app.post('/api/contact', async (req, res) => {
  const { name, email, subject, message } = req.body;

  if (!name || !email || !subject || !message) {
    return res.status(400).json({ message: 'Todos os campos são obrigatórios.' });
  }

  const mailOptions = {
    from: process.env.EMAIL_USER,
    to: process.env.EMAIL_USER,
    subject: `Contato do Portfolio: ${subject}`,
    html: `
      <h2>Nova mensagem de contato!</h2>
      <p><strong>Nome:</strong> ${name}</p>
      <p><strong>Email:</strong> ${email}</p>
      <p><strong>Assunto:</strong> ${subject}</p>
      <p><strong>Mensagem:</strong></p>
      <p>${message}</p>
      <p><strong>Data:</strong> ${new Date().toLocaleString('pt-BR')}</p>
    `
  };

  try {
    await transporter.sendMail(mailOptions);
    res.json({ message: 'Mensagem enviada com sucesso!', success: true });
  } catch (error) {
    console.error('Erro ao enviar email:', error);
    res.status(500).json({ message: 'Erro ao enviar mensagem. Tente novamente.' });
  }
});

// Fallback route to serve index.html for all other routes (Express 5 syntax)
app.get('/{*path}', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Erro não tratado:', err);
  res.status(500).json({ message: 'Erro interno do servidor.' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
  console.log('Notificações enviadas para:', process.env.EMAIL_USER);
});
