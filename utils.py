from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6C4970344851423350316E6161664C67564B687A383834484D756269444B6258386C41327A314E644F38383D')
        params = {
            'sender': '2000500666',
            'receptor': phone_number,
            'message': f'پلتفرم پنجره\nکد تایید شما: {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        b = e
        c = b.decode('utf-8')
        print(c)
    except HTTPException as e:
        b = e
        c = b.decode('utf-8')
        print(c)

