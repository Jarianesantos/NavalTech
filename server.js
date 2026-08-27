// Simple Node.js/Express server for Portfolio backend
const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

const users = [
  { email: 'admin@portfolio.com', password: 'admin123' },
  { email: 'user@portfolio.com', password: 'user123' }
];

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname)));

// Login API endpoint
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: 'Email and password are required.' });
  }

  const user = users.find(
    u => u.email === email && u.password === password
  );

  if (user) {
    res.json({ message: 'Login successful!', success: true });
  } else {
    res.status(401).json({ message: 'Invalid credentials.' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
