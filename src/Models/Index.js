const sequelize = require("../Database/Connection");

const ProfileModel = require("./Profile");
const ProjectModel = require("./Project");
const TechnologyModel = require("./Technology");
const FeedbackModel = require("./Feedback");

const Profile = ProfileModel(sequelize);
const Project = ProjectModel(sequelize);
const Technology = TechnologyModel(sequelize);
const Feedback = FeedbackModel(sequelize);

// Relacionamentos

Profile.hasMany(Project);
Project.belongsTo(Profile);

Project.belongsToMany(Technology, {
  through: "ProjectTechnology"
});

Technology.belongsToMany(Project, {
  through: "ProjectTechnology"
});

Project.hasMany(Feedback);
Feedback.belongsTo(Project);

module.exports = {
  sequelize,
  Profile,
  Project,
  Technology,
  Feedback
};