const { Profile } = require("../Models");

// Criar perfil
const createProfile = async (req, res) => {
  try {
    const profile = await Profile.create(req.body);
    res.json(profile);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Buscar perfil por ID
const getProfileById = async (req, res) => {
  try {
    const profile = await Profile.findByPk(req.params.id);
    if (profile) {
      res.json(profile);
    } else {
      res.status(404).json({ error: "Perfil não encontrado" });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Listar todos os perfis
const getAllProfiles = async (req, res) => {
  try {
    const profiles = await Profile.findAll();
    res.json(profiles);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

module.exports = { createProfile, getProfileById, getAllProfiles };

