const express = require("express");
const app = express();
const profileRoutes = require("./src/Routes/ProfileRoutes");

app.use(express.json());

// Rotas
app.use("/api/profiles", profileRoutes);

app.get("/", (req, res) => {
  res.json({ message: "Servidor DevShowcase API rodando!" });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor DevShowcase API rodando na porta ${PORT}`);
});
