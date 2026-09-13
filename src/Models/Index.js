const { Sequelize, DataTypes } = require("sequelize");

// conexão com banco SQLite (arquivo local devshowcase.db)
const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: "devshowcase.db"
});

// modelo Profile
const Profile = sequelize.define("Profile", {
  name: {
    type: DataTypes.STRING,
    allowNull: false
  },
  bio: {
    type: DataTypes.STRING,
    allowNull: false
  }
});

// sincroniza automaticamente as tabelas
sequelize.sync()
  .then(() => {
    console.log("Banco sincronizado com sucesso!");
  })
  .catch((error) => {
    console.error("Erro ao sincronizar banco:", error);
  });

module.exports = { sequelize, Profile };
