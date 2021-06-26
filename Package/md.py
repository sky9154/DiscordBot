import datetime
import codecs
def week(m,d):
    while True:
        try:
            m=int(m)
            d=int(d)
            a=datetime.datetime(2021,m,d)
            week=a.weekday()+1
            if week==1:
                week="星期一"
            if week==2:
                week="星期二"
            if week==3:
                week="星期三"
            if week==4:
                week="星期四"
            if week==5:
                week="星期五"
            if week==6:
                week="星期六"
            if week==7:
                week="星期日"
            m=str(m)
            d=str(d)
            return("2021年",m,"月",d,"日是",week)
        except:
            m=str(m)
            d=str(d)
            return("2021年",m,"月",d,"日是不存在，請重新輸入!!!")