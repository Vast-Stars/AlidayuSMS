#coding:=utf-8
#__author__: Vast
import androidhelper

droid = androidhelper.Android()


f = open('/storage/sdcard1/reply.txt','r')
phone=f.read().split()
f.close()


SMSmsgs = droid.smsGetMessages(False, 'inbox').result
SMS=[]

for i in range(len(SMSmsgs)):
	if  int(SMSmsgs[i]['date'])>1473635833:
		SMS.append(SMSmsgs[i]['address'][3:])

#print(SMS)

count=0
for i in range(len(SMS)):
    if  SMS[i] in phone:
        count+=1
        phone.remove(SMS[i])

print('共收到',count,'个回复')
print('以下',len(phone),'个号码未回复：')
print(phone)

text=[str(item) for item in phone]
text='\r\n'.join(text)
f = open('/storage/sdcard1/reply.txt','w')
f.write(text)
f.close()
print('已保存结果')
