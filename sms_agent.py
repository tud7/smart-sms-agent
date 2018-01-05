'''
Author: Tu Duong
'''

import os
import json
import sms_api_provider

class SMSAgent(object):

    TWILIO            = 'Twilio'
    SUPPORTED_SMS_API = [TWILIO]

    def __init__(self, config_file):        
        with open(config_file) as f:
            self.config = json.load(f)

        self.sms_api_provider = self._sms_api_provider_factory()

    
    def send_msg(self, phone_number, text_message):
        self.sms_api_provider.send_msg(phone_number, text_message)
    

    def _sms_api_provider_factory(self):
        
        provider = self.config.get('SMS_API_Provider', None)
        if provider is None:
            raise RuntimeError('Missing SMS API Provider information')
        
        if provider not in SMSAgent.SUPPORTED_SMS_API:
            raise RuntimeError('Unsupported SMS API Provider (%s). Supported provider(s): %s' 
                                % (provider, ' '.join(SMSAgent.SUPPORTED_SMS_API)))
        
        auth   = self.config.get('Authentication')
        
        module = __import__('sms_api_provider')
        klass  = getattr(module, provider)
        return klass(auth)

'''
if __name__== "__main__":

    smsagent = SMSAgent('sms_api_provider.json');
    smsagent.send_msg('+xxxxxxxxxx', 'Your message here!!!')
'''
