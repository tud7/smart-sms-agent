'''
Author: Tu Duong
'''

import os
import json

from twilio.rest import Client

class SMSAPIProvider(object):

    def __init__(self, auth_dict):
        if auth_dict is None:
            raise RuntimeError('error: missing authentication information for Twilio')
            
        self.authentication_dict = auth_dict

    
    @property
    def send_msg(self, phone_number, text_message):
        raise NotImplementedError('error: subclasses should implement this!')

        
class Twilio(SMSAPIProvider):
     
    ACCOUNT_ID   = 'account_id'
    AUTH_TOKEN   = 'auth_token'
    FROM_NUMBER  = 'from_number'

    def __init__(self, auth_dict):
        
        SMSAPIProvider.__init__(self, auth_dict)
        
        # get Twilio authentication from configuration file
        self.account_id      = self.authentication_dict.get(Twilio.ACCOUNT_ID,   None)
        self.auth_token      = self.authentication_dict.get(Twilio.AUTH_TOKEN,   None)
        self.my_phone_number = self.authentication_dict.get(Twilio.FROM_NUMBER,  None)
        
        # validate the authentication
        if not self.account_id:
            raise RuntimeError('Twilio --missing %s') % Twilio.ACCOUNT_ID
        if not self.auth_token:
            raise RuntimeError('Twilio --missing %s') % Twilio.AUTH_TOKEN
        if not self.my_phone_number:
            raise RuntimeError('Twilio --missing %s') % Twilio.FROM_NUMBER
        
        # create Twilio client
        self.client  = Client(self.account_id, self.auth_token)
    
    
    def send_msg(self, phone_number, text_message):
    
        if not phone_number:
            raise RuntimeError('Twilio --missing to phone number')
        if not text_message:
            raise RuntimeError('Twilio --missing text message')
            
        message = self.client.messages.create(to=phone_number, from_=self.my_phone_number, body=text_message)



