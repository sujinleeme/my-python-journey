import time
weekday_ko = {'Monday':'월','Tuesday':'화','Wednesday':'수','Thursday':'목','Friday':'금','Saturday':'토','Sunday':'일'}
weekday_today_ko = (weekday_ko[time.strftime('%A')])
message = (time.strftime('Today is %Y년 %-m월 %d일') + ' %s요일 입니다.' % (weekday_today_ko))
print (message)
