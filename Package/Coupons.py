def check(id):
  coupons = [{
    "name" : "國旅券",
    "week1" : ["21", "32", "98", "67", "97", "410"],
    "week2" : ["04", "29", "40", "71", "87"]
    
  }, {
    "name" : "i原券",
    "week1" : ["64", "85"],
    "week2" : ["12", "59"]
  }, {
    "name" : "農遊券",
    "week1": ["89", "32", "54", "597", "453", "152"],
    "week2" : ["50", "13"]
  }, {
    "name" : "藝fun券(數位)",
    "week1" : ["96", "15", "07", "30", "73", "98", "19", "11"],
    "week2" : []
  }, {
    "name" : "藝fun券(紙本)",
    "week1" : ["39", "37", "23", "36", "79", "08", "14", "75"],
    "week2" : []
  }, {
    "name" : "動滋券",
    "week1" : ["97", "13", "19", "55", "71", "93", "381", "734", "644", "453", "985"],
    "week2" : []
  }, {
    "name" : "客庄劵2.0",
    "week1" : ["81", "900"],
    "week2" : []
  }, {
    "name" : "地方創生券",
    "week1" : ["081", "105", "594", "188", "089", "396", "521", "467", "912", "798", "358", "441", "367", "941", "335"],
    "week2" : []
  }]
  id_list = list(id) # 將身分證轉串列，方便判斷後三後二碼
  flag = 0 # 旗標 判斷是否中獎
  msg = "" # 輸出字串
  weekKey = "week" # 各個波次的名稱

  if len(id) != 3: # 判斷是否三碼
    return("請輸入身分證後三碼")

  msg = "身分證後三碼：" + str(id) + "\n"
  
  for week in range(1, 3):
    msg += "第 {} 波：\n".format(week)
    weekKey += str(week)
    for i in range(len(coupons)):
      if(id_list[1] + id_list[2]) in coupons[i][weekKey]:
        msg += coupons[i]["name"] + "\n"
        flag = 1
      else:
        if id in coupons[i][weekKey]:
          msg += coupons[i]["name"] + "\n"
          flag = 1
    if flag == 0:
      msg += "你什麼也沒中\n"
    
    # 重置變數
    flag = 0
    weekKey = "week"
  return msg

