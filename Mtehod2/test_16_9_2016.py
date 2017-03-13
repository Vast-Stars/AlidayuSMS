# -*- coding: utf-8 -*-
#__auth__: Vast
#__Date__: 16/9 2016
from alidayu import AlibabaAliqinFcSmsNumSendRequest

# 其中appkey和secret是必须的参数
# url可选，默认为沙箱的URL，正式应用请传入 https://eco.taobao.com/router/rest
# partner_id为可选，其值为下载的TOP SDK中的top/api/base.py里的SYSTEM_GENERATE_VERSION
#2.85
appkey =
secret=
url='https://eco.taobao.com/router/rest'
partner_id=''
req=AlibabaAliqinFcSmsNumSendRequest(appkey, secret, url, partner_id)

req.extend="123456"
req.sms_type="normal"
req.sms_free_sign_name="计算机部"
#req.sms_param=json.dumps(params)
#req.sms_param=json.dumps()

f=open("测试.txt")
#读入号码
A=f.read().split()
f.close()
A= [str(item) for item in A]
print('共',len(A),'个号码，共',len(A)*0.045*3,'元')
A=','.join(A)

req.rec_num=A
req.sms_template_code='SMS_15415001' #短信模板编号

resp= req.getResponse()
print(resp)

#try:
#    resp= req.getResponse()
#    print(resp)
#except Exception,e:
#    print(e)
print('OK')