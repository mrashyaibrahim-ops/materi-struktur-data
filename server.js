const express = require("express");
const app = express();

app.get("/api/data", (req, res) => {
  res.json({ pesan: "Halo dari server" });
});

app.listen(3000);