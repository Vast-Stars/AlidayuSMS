import androidhelper
import time
droid = androidhelper.Android()

f = open('/storage/sdcard1/phone1.txt','r')
phone=f.read().split()
f.close()


SMSmsgs = droid.smsGetMessages(False, 'sent').result
for i in range(len(SMSmsgs)):
	if  int(SMSmsgs[i]['date'])>1473635033:
            if SMSmsgs[i]['address'][0:3]=='+86':
                SMSmsgs[i]['address']==SMSmsgs[i]['address'][3:]
            #print(SMSmsgs[i]['address'][3:])
            if SMSmsgs[i]['address'] in phone:
                phone.remove(SMSmsgs[i]['address'])
                print('remove one')
print(len(phone))


rq='12日16:30-17:50'
#1
count=1
text='test'+rq+'test'
count=1
print('开始发送短信……')
for currNum in phone:
	print('正在发送第',count,'个短信')
	count+=1
	droid.smsSend(currNum,text)
print('所有短信发送完成!')
