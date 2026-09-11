const express = require("express");
const cors = require("cors");

const { sequelize } = require("./src/Models/Index");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    mensagem: "DevShowcase API funcionando!"
  });
});

sequelize.sync()
  .then(() => {
    app.listen(3000, () => {
      console.log("Servidor rodando na porta 3000");
    });
  })
  .catch((error) => {
    console.error("Erro ao conectar ao banco:", error);
  });