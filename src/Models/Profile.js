const { DataTypes } = require("sequelize");

module.exports = (sequelize) => {
  return sequelize.define("Profile", {
    name:{
      type: DataTypes.STRING,
      allowNull: false
    },

    email: {
      type: DataTypes.STRING,
      allowNull: false
    },

    bio: {
      type: DataTypes.TEXT
    }
  });
};