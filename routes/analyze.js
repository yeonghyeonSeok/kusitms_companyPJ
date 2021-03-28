const express = require("express");
const router = express.Router();
const upload = require("../config/multer");

/*
대화내용 분석
METHOD       : POST
URL          : /analyze
BODY         : text = 대화내용
*/
router.post("/", upload.single("text"), async (req, res) => {
  console.log(req.file.location);
});

module.exports = router;
