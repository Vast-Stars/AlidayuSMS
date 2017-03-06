#coding:=utf-8
#__author__=Vast
# 检查收件箱，统计回复号码


import androidhelper

droid = androidhelper.Android()


f = open('/storage/sdcard1/reply.txt','r')
#f = open('D:\phone.txt','r')
phone=f.read().split()
f.close()

count=1
SMSmsgs = droid.smsGetMessages(True, 'inbox').result
SMS=[]
for i in Range(len(SMSmsgs))：
	if  SMSmsgs[i]['date']>1473583925914：
		SMS.append(SMSmsgs[i])
print(len(SMS))
for i in Range(len(SMS))
	if  SMSmsgs[i]['address'] in f
		count+1
print(count)