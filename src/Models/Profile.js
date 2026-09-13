module.exports = (sequelize, DataTypes) => {
  const Profile = sequelize.define("Profile", {
    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
    bio: {
      type: DataTypes.STRING,
    },
  });

  return Profile;
};

