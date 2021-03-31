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

router.get("/", async (req, res) => {
  const analyze_result = {
    date_data: {
      start: "2021-02-13",
      end: "2021-03-10",
    },
    participant_num: 6,
    participant_list: [
      "김유빈",
      "오케이",
      "링커리어 이정민님",
      "김성원",
      "경수",
      "김현정",
    ],
    participant_chat: [
      ["김유빈", 473],
      ["오케이", 259],
      ["링커리어 이정민님", 194],
      ["김성원", 95],
      ["경수", 48],
      ["김현정", 32],
    ],
    participant_file: [
      ["김유빈", 28],
      ["오케이", 23],
      ["김성원", 9],
      ["김현정", 3],
      ["경수", 1],
      ["링커리어 이정민님", 1],
    ],
    participant_question: [
      ["김유빈", 79],
      ["링커리어 이정민님", 32],
      ["오케이", 27],
      ["김성원", 13],
      ["경수", 7],
      ["김현정", 4],
    ],
    participant_picture: [
      ["김유빈", 22],
      ["오케이", 12],
      ["링커리어 이정민님", 6],
      ["김성원", 3],
      ["김현정", 3],
      ["경수", 2],
    ],
  };
  return res
    .status(200)
    .send(defaultRes.successTrue(statusCode.OK, "통신성공", analyze_result));
});

module.exports = router;
