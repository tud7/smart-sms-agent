'''
Author: Tu Duong
Copyright 2018, 2019 Tu Duong
'''

import os
import json
import argparse
import sms_api_provider

class SMSAgent(object):

    SMS_API_PROVIDER = 'SMS_API_PROVIDER'
    TWILIO            = 'Twilio'
    SUPPORTED_SMS_API = [TWILIO]

    def __init__(self):
        self.sms_api_provider = self._sms_api_provider_factory()


    def send_msg(self, phone_number, text_message):
        self.sms_api_provider.send_msg(phone_number, text_message)


    def _sms_api_provider_factory(self):

        provider = os.getenv(SMSAgent.SMS_API_PROVIDER, None)
        if provider is None:
            raise RuntimeError('SMSAgent -- missing environment variable: %s' %SMSAgent.SMS_API_PROVIDER)

        if provider not in SMSAgent.SUPPORTED_SMS_API:
            raise RuntimeError('Unsupported SMS API Provider (%s). Supported provider(s): %s'
                                % (provider, ' '.join(SMSAgent.SUPPORTED_SMS_API)))

        module = __import__('sms_api_provider')
        klass  = getattr(module, provider)
        return klass()


def send_msg(to_number, message):
    """
    Call to send message to the provided to_number
    Arguments:
    to_number -- the string phone number of the person you want to send the message, start with +(country) (e.g.: "+12223334444")
    nessage   -- the string text message that you want to send(e.g. " Hello World")
    """
    smsagent = SMSAgent();
    smsagent.send_msg(to_number, message)


if __name__== "__main__":

    parser = argparse.ArgumentParser(description='Smart SMS Agent')
    parser.add_argument('to_number',          help='phone number of the person you want to send the message, start with +(country) (e.g.: +12223334444)')
    parser.add_argument('message', nargs='+', help='the text message that you want to send in double quote (e.g. " Hello World")')

    args = parser.parse_args()

    message  =  ' '.join(args.message) # solution to parse string with spaces from command line
    send_msg(args.to_number, message)
