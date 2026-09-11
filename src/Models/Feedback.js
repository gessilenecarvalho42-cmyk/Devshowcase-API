const { DataTypes } = require("sequelize");

module.exports = (sequelize) => {
  return sequelize.define("Feedback", {
    comment: {
      type: DataTypes.TEXT,
      allowNull: false
    },

    rating: {
      type: DataTypes.INTEGER,
      allowNull: false
    }
  });
};