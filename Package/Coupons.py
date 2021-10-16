def check(id):
  coupons = [{
    "name": "國旅券",
    "number": ["21", "32", "98", "67", "97", "410"]
  }, {
    "name": "i原券",
    "number": ["64", "85"]
  }, {
    "name": "農遊券",
    "number": ["89", "32", "54", "597", "453", "152"]
  }, {
    "name": "藝fun券(數位)",
    "number": ["96", "15", "07", "30", "73", "98", "19", "11"]
  }, {
    "name": "藝fun券(紙本)",
    "number": ["39", "37", "23", "36", "79", "08", "14", "75"]
  }, {
    "name": "動滋券",
    "number": ["97", "13", "19", "55", "71", "93", "381", "734", "644", "453", "985"]
  }, {
    "name": "客庄劵2.0",
    "number": ["81", "900"]
  }, {
    "name": "地方創生券",
    "number": ["081", "105", "594", "188", "089", "396", "521", "467", "912", "798", "358", "441", "367", "941", "335"]
  }]
  id_list = list(id)
  flag = 0
  msg = ""
  if len(id) != 3:
    return("請輸入身分證後三碼")

  msg = "身分證後三碼：" + str(id) + "\n"

  for i in range(8):
    if(id_list[1] + id_list[2]) in coupons[i]["number"]:
      msg += coupons[i]["name"] + "\n"
      flag = 1
    else:
      if id in coupons[i]["number"]:
        msg += coupons[i]["name"] + "\n"
        flag = 1

  if flag == 0:
    msg += "你什麼也沒中"
  return msg