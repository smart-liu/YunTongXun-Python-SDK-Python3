#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import random

#随机六位数的验证码
six_code = "%06d" % random.randint(0, 999999)

#主帐号
accountSid= '您的主帐号';

#主帐号Token
accountToken= '您的主帐号Token';

#应用Id
appId='您的应用ID';

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com';

#请求端口 
serverPort='8883';

#REST版本号
softVersion='2013-12-26';

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id

class YunTongXun(object):
    """发送短信验证码，单例模式"""

    def __new__(cls):
        # 判断有没有类属性instance
        if not hasattr(cls, "instance"):
            # 如果没有，则创建这个类的对象，并保存到类属性instance中
            obj = super(YunTongXun, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        # 如果有，则直接返回对象
        return cls.instance

    def send_template_sms(self, to, datas=[six_code, 2], temp_id=1):
        try:
            # 调用云通讯的工具rest发送短信
            result = self.rest.sendTemplateSMS(to, datas, temp_id)  # 手机号码,内容数据[验证码,时间],模板Id
            
        except Exception as error:
            raise error

        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送成功
            return 0, six_code
        else:
            # 发送失败
            return -1, six_code

#sendTemplateSMS(手机号码,内容数据,模板Id)  
def sendTemplateSMS(to,datas,tempId):
   
    #初始化REST SDK
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)
    
    result = rest.sendTemplateSMS(to,datas,tempId)
    for k,v in result.iteritems(): 
        
        if k=='templateSMS' :
                for k,s in v.iteritems(): 
                    print '%s:%s' % (k, s)
        else:
            print '%s:%s' % (k, v)
    
   
