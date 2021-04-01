var express = require("express");
var router = express.Router();

/* GET home page. */
router.get("/", function (req, res) {
  res.render("main.html");
});
router.use("/analyze", require("./analyze"));
router.use("/test", require("./test"));
module.exports = router;
