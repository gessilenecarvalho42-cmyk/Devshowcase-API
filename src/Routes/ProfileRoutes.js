const express = require("express");
const router = express.Router();
const { createProfile, getProfileById, getAllProfiles } = require("../Controllers/ProfileController");

router.post("/", createProfile);
router.get("/", getAllProfiles);
router.get("/:id", getProfileById);

module.exports = router;

