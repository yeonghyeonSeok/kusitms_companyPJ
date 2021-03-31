const express = require("express");
const router = express.Router();
const upload = require("../config/multer");
const defaultRes = require("../module/utils/utils");
const statusCode = require("../module/utils/statusCode");

/*
대화내용 분석
METHOD       : POST
URL          : /analyze
BODY         : text = 대화내용
*/
router.post("/", upload.single("text"), async (req, res) => {
  if (req.file == undefined) {
    return res
      .status(200)
      .send(defaultRes.successFalse(statusCode.OK, "파일전송실패"));
  }
  return res
    .status(200)
    .send(
      defaultRes.successTrue(statusCode.OK, "파일전송성공", req.file.location)
    );
});

module.exports = router;
