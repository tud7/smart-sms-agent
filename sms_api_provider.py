'''
Author: Tu Duong
Copyright 2018, 2019 Tu Duong
'''

import os
import json

from twilio.rest import Client

class SMSAPIProvider(object):

    ACCOUNT_ID          = 'ACCOUNT_ID'
    AUTH_TOKEN          = 'AUTH_TOKEN'
    CALLER_PHONE_NUMBER = 'CALLER_PHONE_NUMBER'

    def __init__(self):

        _missing_env = []

        self.account_id          = os.getenv(SMSAPIProvider.ACCOUNT_ID, None)
        self.auth_token          = os.getenv(SMSAPIProvider.AUTH_TOKEN, None)
        self.caller_phone_number = os.getenv(SMSAPIProvider.CALLER_PHONE_NUMBER, None)

        # validate the authentication
        if not self.account_id:
            _missing_env.append(SMSAPIProvider.ACCOUNT_ID)
        if not self.auth_token:
            _missing_env.append(SMSAPIProvider.AUTH_TOKEN)
        if not self.caller_phone_number:
            _missing_env.append(SMSAPIProvider.CALLER_PHONE_NUMBER)

        if _missing_env:
            raise RuntimeError('SMSAPIProvider -- missing environment variable(s):  %s' %_missing_env)

    @property
    def send_msg(self, phone_number, text_message):
        raise NotImplementedError('error: subclasses should implement this!')


class Twilio(SMSAPIProvider):

    def __init__(self):

        SMSAPIProvider.__init__(self)

        # create Twilio client
        self.client  = Client(self.account_id, self.auth_token)


    def send_msg(self, phone_number, text_message):

        if not phone_number:
            raise RuntimeError('Twilio --invalid phone number')
        if not text_message:
            raise RuntimeError('Twilio --invalid text message')

        message = self.client.messages.create(to=phone_number, from_=self.caller_phone_number, body=text_message)
