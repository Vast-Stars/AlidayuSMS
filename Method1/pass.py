# -*- coding=UTF-8 -*-

__author__="jesty(jestyf@hotmail.com)"

import hashlib
import requests
import re
import time
from urllib import quote as urlencode

global url
url='http://gw.api.taobao.com/router/rest'

def getmd5(head_str):
	str=hashlib.md5(head_str).hexdigest().upper()
	return str
def gettime():
	tmp=time.localtime(time.time())
	datastr=time.strftime('%Y-%m-%d',tmp)
	timestr=time.strftime('%H:%M:%S',tmp)
	return datastr,timestr
	
def arg_connect(post_list):
	srcret="______________________"#你自己的app秘钥
	md5str=srcret
	md5str+='app_key________' #你自己的appkey
	md5str+='force_sensitive_param_fuzzytrue'
	md5str+='formatxmlmethodalibaba.aliqin.fc.sms.num.send'
	md5str+='partner_idtop-apitools'
	#md5str+='rec_num'+post_list['rec_num']
	#md5str+='sign_methodmd5'
	md5str+='sms_free_sign_name'+post_list['sms_free_sign_name']
	md5str+='sms_param'+post_list['sms_param']
	md5str+='sms_template_codeSMS_14691590sms_typenormal'
	md5str+='timestamp'+post_list['timestamp']
	md5str+='v2.0'
	#md5str=md5str+srcret
	print md5str
	md5str=getmd5(md5str)
	return md5str	
		
def getheader(name,phonenum):
	datastr,timestr=gettime()
	param="{name:\'%s\'}"%urlencode(name)
#	param="{name:\'%s\'}"%(name)
	payload={
		'app_key':'————————————'#你自己的appkey
		'force_sensitive_param_fuzzy':'true',
		'format':'xml',
		'method':'alibaba.aliqin.fc.sms.num.send',
		'partner_id':'top-apitools',
		'rec_num':phonenum,
	#	'sign_method':'md5',
		'sms_free_sign_name':urlencode('计算机部'),
		'sms_param':urlencode(param),
		'sms_template_code':'SMS_14691590',
		'sms_type':'normal',
		#'timestamp':urlencode(datastr+' '+timestr),
		'timestamp':datastr+' '+timestr,
		'v':'2.0'
	}
	estr=arg_connect(payload)
	md5str=getmd5(estr)
#	payload['rec_num']=phonenum
	payload['sign']=md5str
	payload['timestamp']=datastr+'+'+urlencode(timestr)
	
	return payload

def post_req(name,phonenum):
	global url
	tmp_payload=getheader(name,phonenum)
	r=requests.get(url,params=tmp_payload)
	print r.text

namelist='passlist.txt'
with open(namelist) as file:
	for line in file:
		name,phonenum=[x for x in line.split()]
		post_req(name,phonenum)