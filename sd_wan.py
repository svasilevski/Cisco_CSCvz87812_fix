import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SdWan:
    def __init__(self, base_url, username, password):
        self._username = username
        self._password = password
        self._base_url = base_url
        self.session = requests.Session()
        self.headers = {}
        self.authenticate()
    
    def authenticate(self):
        res = self.session.post(self._base_url+"/j_security_check", data = {'j_username':self._username, "j_password": self._password}, verify=False)
        self.headers = {'Cookie': f'JSESSIONID={res.cookies.get("JSESSIONID")}'}
        url = f'{self._base_url}dataservice/client/token'
        token = requests.request("GET", url, headers=self.headers, verify=False)
        self.session.headers['X-XSRF-TOKEN'] = token.content
    
    def get_devices(self):
        url = f"{self._base_url}dataservice/system/device/vedges"
        res = self.session.get(url, verify=False, headers=self.headers)
        if res.status_code != 200:
            raise Exception("Connection error")
        return res.json()["data"]
    
    def migrate_device(self, device:dict):
        assert "ISR1100" in device["deviceModel"] and "-XE" not in device["deviceModel"], f'Device {device["deviceModel"]} not eligible for migration.'
        res = self.session.put(f'{self._base_url}dataservice/system/device/migrateDevice/{device["uuid"]}')
        if res.status_code != 200:
            raise Exception("Connection error")
        return "success"