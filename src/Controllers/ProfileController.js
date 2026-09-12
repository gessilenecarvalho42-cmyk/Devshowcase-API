const { Profile } = require("../Models/Index");

const createProfile = async (req, res)=>{
  try {
    const profile = await Profile.create(req.body);

    res.status(201).json(profile);

  } catch (error) {
    res.status(500).json({
      error: error.message
    });
  }
};

const getProfileById = async (req, res)=>{
  try {
    const profile = await Profile.findByPk(req.params.id);

    if (!profile) {
      return res.status(404).json({
        message: "Perfil não encontrado"
      });
    }

    res.json(profile);

  } catch (error) {
    res.status(500).json({
      error: error.message
    });
  }
};

module.exports = {
  createProfile,
  getProfileById
};