#coding:=utf-8
#__author__=Vast
# 检查收件箱，统计回复号码
import androidhelper
import time
import os
import configparser
droid = androidhelper.Android()
filelocation='/storage/sdcard1/duanxin/'
ISOTIMEFORMAT=' %Y-%m-%d %X'

if os.path.exists(filelocation+'conf.ini'):
	f1=configparser.ConfigParser
	f1.read('config.conf')
	time2=f1.get('a1','time')
	print('检测到之前的任务记录，时间为:',time.strftime(ISOTIMEFORMAT,time.localtime(time2)))
	if(input('是否采用（Y）/ 新建（N）：')=='N'):
		time2=time.time()
		f1.set('a1','time',time2)
		f1.write(open('config.conf','w'))


time2=time.time()

#f = open(filelocation+'phone.txt','r')
#phone=f.read().split()

#f.close()
phone='''123123123123
123123123
123123123
123123312
'''
phone=phone.split()
print('读入完成！共',len(phone),'个电话')


SMSmsgs = droid.smsGetMessages(False, 'sent').result
SMS=[]
for i in range(len(SMSmsgs)):
	if  int(SMSmsgs[i]['date'])>time2:
		SMS.append(SMSmsgs[i]['date'])
begin=len(SMS)


text='test'
print('发送内容如下：')
print(text)
if (input('输入Y以确认下一步：')!='Y'):
	exit()
print('开始发送短信……')
count=1
for currNum in phone:
	print('正在发送第',count,'个短信')
	count+=1
	droid.smsSend(currNum,text)
	time.sleep(2)
print('所有短信发送完成!')
	

print('检查成功发送短信……')
time.sleep(10)
SMSmsgs = droid.smsGetMessages(False, 'sent').result
SMS=[]
for i in range(len(SMSmsgs)):
	if  int(SMSmsgs[i]['date'])>time2:
		SMS.append(SMSmsgs[i]['date'])
print('成功发送',len(SMS)-begin,'条短信')
