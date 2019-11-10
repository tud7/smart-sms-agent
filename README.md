# smart-sms-agent
Copyright © 2018, 2019 Tu Duong

## Install the SMS API Provider
### Twilio
```
pip install twilio
```
## The SMSAgent Abstraction Layer

SMSAgent is an API that abstract out all the different SMS providers
Your SMS provider's account information is stored in the configuration file (JSON) that will be passed in SMSAgent's constructor.

To instantiate a SMSAgent object:
```
smsagent = SMSAgent('/path/to/your/config/file');
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

Your configuration file will look like this:
```
{
    "SMS_API_Provider" : "Twilio",
    "Authentication" : {
        "account_id" : "{your Twillio account ID}",
        "auth_token" : "{your authentication token number}",
        "from_number": "{your phone number (or sender's number)}"
    }
}
```
