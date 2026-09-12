const express = require("express");
const router = express.Router();
const { createProfile, getProfileById } = require("../Controllers/ProfileController");

// POST /api/profiles → cria perfil
router.post("/", createProfile);

// GET /api/profiles/:id → busca perfil por ID
router.get("/:id", getProfileById);

module.exports = router;

module.exports = router;