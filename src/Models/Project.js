const { DataTypes } = require("sequelize");

module.exports = (sequelize) => {
  return sequelize.define("Project", {
    title: {
      type: DataTypes.STRING,
      allowNull: false
    },

    description: {
      type: DataTypes.TEXT,
      allowNull: false
    },

    repositoryUrl: {
      type: DataTypes.STRING,
      allowNull: false
    }
  });
};