const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

// Importa as rotas
const ProfileRoutes = require ("./src/Routes/ProfileRoutes")

// Usa as rotas com prefixo
app.use("/api/profiles", ProfileRoutes);

// Rota raiz em JSON
app.get("/", (req, res) => {
  res.json({ message: "Servidor DevShowcase API rodando!" });
});

app.listen(3000, () => {
  console.log("Servidor rodando na porta 3000");
});
