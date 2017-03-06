# -*- coding=UTF-8 -*-

__author__="jesty(jestyf@hotmail.com)"

import hashlib
import requests
import json
import time

global url,sing_name,smstemplate,appkey,secret
######################
#注意，目前的程序生成param参数部分未完全完成
#所以，在模板中只能包含一个变量，
#且变量名称为name,即含有一个${name}
#需要发送短信的列表保存格式为：
#姓名 手机号
#将此文件保存为txt格式并在下面指定出
#程序运行环境为Python 2.7
#####################

namelist='list.txt'
print(namelist)
input()
sign_name='日常通知' #定义短信签名
smstemplate='SMS_14985167'#指定短信模板编号
appkey='23454557' #你自己的appkey
secret="d80f1357c1a4f2d684bf5c3806e6b2b7"#你自己的app秘钥


url='http://gw.api.taobao.com/router/rest'  #接口地址

#获取MD5
def getmd5(head_str):
	str=hashlib.md5(head_str).hexdigest().upper()
	return str
#获取时间字串
def gettime():
	tmp=time.localtime(time.time())
	tstr=time.strftime('%Y-%m-%d %H:%M:%S',tmp)
	return tstr
#拼接参数字串
def arg_connect(post_list):
	global secret
	connect_arg=secret
	connect_arg+='app_key'+post_list['app_key']
	connect_arg+='force_sensitive_param_fuzzytrue'
	connect_arg+='formatjson'+'method'+post_list['method']
	connect_arg+='partner_idtop-apitools'
	connect_arg+='rec_num'+post_list['rec_num']
	connect_arg+='sms_free_sign_name'+post_list['sms_free_sign_name']
	connect_arg+='sms_param'+post_list['sms_param']
	connect_arg+='sms_template_code'+post_list['sms_template_code']+'sms_typenormal'
	connect_arg+='timestamp'+post_list['timestamp']
	connect_arg+='v2.0'
	return connect_arg	
#获取需要传的参数
def getheader(name,phonenum):
	global appkey,smstemplate
	param="{name:\'%s\'}"%(name)
	payload={
		'app_key':appkey,
		'force_sensitive_param_fuzzy':'true',
		'format':'json',
		'method':'alibaba.aliqin.fc.sms.num.send',
		'partner_id':'top-apitools',
		'rec_num':phonenum,
		'sms_free_sign_name':sign_name,
		'sms_param':param,
		'sms_template_code':smstemplate,
		'sms_type':'normal',
		'timestamp':gettime(),
		'v':'2.0'
	}
	estr=arg_connect(payload)
	md5str=getmd5(estr)
	payload['sign']=md5str
	return payload
#返回状态分析
def statusanalysis(data):
	s=json.loads(data)
	if ('alibaba_aliqin_fc_sms_num_send_response' in s):
		return 1
	elif ('error_response' in s):
		print '发送未成功'
		print '返回代码为%s'%(s['error_response']['code'])
		print '返回信息为%s'%(s['error_response']['code'])
		return -1
#向接口发送数据
def post_req(name,phonenum):
	global url
	tmp_payload=getheader(name,phonenum)
	r=requests.get(url,params=tmp_payload)
	status=statusanalysis(r.text)
	if (status==1):
		print '成功向%s(手机号%s)发送短信'%(name,phonenum)

#打开文件，获取列表并发送短信
with open(namelist) as file:
	for line in file:
		try:
			name,phonenum=[x for x in line.split()]
		except Exception,e:
			print '无法解析输入内容'
			print '返回错误信息为:%s'%(e)
			continue
		post_req(name,phonenum)