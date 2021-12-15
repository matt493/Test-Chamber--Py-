import requests
import time

while(True):
    try:
        res = requests.post('http://192.168.20.1:8002/index.php?zone=wifi', data={'auth_user':'addon', 'auth_pass':'rcss', 'redirurl':'', 'accept':'Login'})
        print(res)
    except:
        print("ERROR!")
    finally:
        time.sleep(5)