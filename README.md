# smart-sms-agent
Copyright © 2018, 2019 Tu Duong

## Install the SMS API Provider
### Twilio
```
pip install twilio
```
## Environment Setup
Before running smart-sms-agent, make sure these environment variables are set

* **SMS_API_PROVIDER** : the SMS API provider you are using
* **ACCOUNT_ID**: your account ID provided by your SMS API provider
* **AUTH_TOKEN**: your authentication token provided by your SMS API provider
* **CALLER_PHONE_NUMBER**: the caller phone number that you registered with your SMS API provider

For example:
```bash
#!/bin/bash

export SMS_API_PROVIDER=Twilio
export ACCOUNT_ID=ABC112233
export AUTH_TOKEN=fdd3343fd
export CALLER_PHONE_NUMBER=+18443336666
```
## Calling smart-sms-agent from Command Line:
```
python smart_sms_agent.py <to_number> <message>

positional arguments:
  to_number   phone number of the person you want to send the message, start
              with +(country) (e.g.: +12223334444)
  message     the text message that you want to send in double quote (e.g. "
              Hello World")
```
## The SMSAgent Abstraction Layer

SMSAgent is an API that abstract out all the different SMS providers
Your SMS provider's account information is stored in the environment variables that will be processed in SMSAgent.

To instantiate a SMSAgent object:
```
smsagent = SMSAgent();
```
To send a text message:
```
smsagent.send_msg('+##########', 'Your message here!!!')
```
*Note: ########## is the receiver's phone number*

For example:
```
smsagent = SMSAgent('sms_api_provider.json');
smsagent.send_msg('+14158141829', 'Welcome to my GitHub!!!')
```
## Supported SMS Providers

Current supported SMS Providers: **TWILIO**

### TWILIO:

https://www.twilio.com/

Sign up for Twilio account. After you sign up, Twilio will provide you an **account ID** and **authentication token**.
