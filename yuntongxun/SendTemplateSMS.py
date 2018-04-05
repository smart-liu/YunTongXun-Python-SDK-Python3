#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import random

#�����λ������֤��
six_code = "%06d" % random.randint(0, 999999)

#���ʺ�
accountSid= '�������ʺ�';

#���ʺ�Token
accountToken= '�������ʺ�Token';

#Ӧ��Id
appId='����Ӧ��ID';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿� 
serverPort='8883';

#REST�汾��
softVersion='2013-12-26';

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

class YunTongXun(object):
    """���Ͷ�����֤�룬����ģʽ"""

    def __new__(cls):
        # �ж���û��������instance
        if not hasattr(cls, "instance"):
            # ���û�У��򴴽������Ķ��󣬲����浽������instance��
            obj = super(YunTongXun, cls).__new__(cls)

            # ��ʼ��REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        # ����У���ֱ�ӷ��ض���
        return cls.instance

    def send_template_sms(self, to, datas=[six_code, 2], temp_id=1):
        try:
            # ������ͨѶ�Ĺ���rest���Ͷ���
            result = self.rest.sendTemplateSMS(to, datas, temp_id)  # �ֻ�����,��������[��֤��,ʱ��],ģ��Id
            
        except Exception as error:
            raise error

        status_code = result.get("statusCode")
        if status_code == "000000":
            # ��ʾ���ͳɹ�
            return 0, six_code
        else:
            # ����ʧ��
            return -1, six_code

#sendTemplateSMS(�ֻ�����,��������,ģ��Id)  
def sendTemplateSMS(to,datas,tempId):
   
    #��ʼ��REST SDK
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
    
   
