# import requests
# from .access_token import generate_access_token
# from .utils import timestamp_convertion
# from . import keys
# from requests.auth import HTTPBasicAuth
# from .encode_base64 import generate_password


# def lipa_na_mpesa():
#     # time formatting
#     formarted_time = timestamp_convertion()

#     # base64 encode
#     decoded_password = generate_password(formarted_time)
#     access_token = generate_access_token()
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = { "Authorization": "Bearer %s" % access_token }
#     request = {
#         "BusinessShortCode": keys.business_short_code,
#         "Password": decoded_password,
#         "Timestamp": formarted_time,
#         "TransactionType": "CustomerBuyGoodsOnline",#CustomerPayBillOnline
#         "Amount": "1", 
#         "PartyA": keys.phone_number,
#         "PartyB": keys.business_short_code,
#         "PhoneNumber": keys.phone_number,
#         "CallBackURL": "https://m-pay.herokuapp.com/api/payments/lnm/",
#         "AccountReference": "Test004Clinton",
#         "TransactionDesc": "Rent pay"
#     }
    
#     response = requests.post(api_url, json = request, headers=headers)

#     print (response.text)

# lipa_na_mpesa()