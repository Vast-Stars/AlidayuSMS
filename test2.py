#coding:=utf-8
#__author__=Vast
# 发送短信
import androidhelper

droid = androidhelper.Android()

f = open('/storage/sdcard1/phone.txt','r')
#f = open('D:\phone.txt','r')
phone=f.read().split()
f.close()

print('读入完成！共',len(phone),'个电话')


text='test'
count=1
print('开始发送短信……')
for currNum in phone:
	print('正在发送第',count,'个短信')
	count+=1
	#droid.smsSend(currNum,text)
print('所有短信发送完成!')
	

print('开始检查未成功发送短信……')

SMSmsgs = droid.smsGetMessages(False, 'sent').result
print(len(SMSmsgs))
for msg in SMSmsgs:
    if msg['data']>1473583925914:
        del(SMSmsgs[SMSmsgs.index( msg)])
print(len(SMSmsgs))
print(SMSmsgs[0])
