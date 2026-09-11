const { DataTypes } = require("sequelize");

module.exports = (sequelize) => {
  return sequelize.define("Technology", {
    name: {
      type: DataTypes.STRING,
      allowNull: false
    }
  });
};