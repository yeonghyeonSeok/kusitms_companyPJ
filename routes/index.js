var express = require("express");
var router = express.Router();

/* GET home page. */
router.get("/", function (req, res) {
  console.log("1");
  res.render("main.html");
});

module.exports = router;
