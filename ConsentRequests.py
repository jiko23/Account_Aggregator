import requests

class ConsentRequests:

    def __init__(self):
        self.__header = {'x-client-id': "SETU Client id", 'x-client-secret': "SETU client secret key"}
        self.__requests = requests.Session()
    

    def sendConsentPayload(self, consent_details):
        try:
                response = self.__requests.post("https://fiu-uat.setu.co/consents", json = consent_details, headers = self.__header)
                if(response.status_code == 201):
                    return {"status_code": response.status_code, "response": response.json()}
        except Exception as ex:
                return {"error": ex}


    def getConsents(self, id):
        url = ''.join(["https://fiu-uat.setu.co/consents/", id])
        try:
                response = self.__requests.get(url, headers=self.__header)
                if(response.status_code == 200):
                    return {"response": response.status_code, "data": response.json()}
        except Exception as ex:
                return {"error": ex}


    def sendSessionPayload(self, session_data):
        count = 0
        #print("Session Payload: ", session_data)
        try:
            while(count < 5):
                response = self.__requests.post("https://fiu-uat.setu.co/sessions", json = session_data, headers=self.__header)
                if(response.status_code == 201):
                    return {"status_code": response.status_code, "response": response.json()}
                elif((response.status_code != 201) and (count < 5)):
                    count += 1
                    continue

        except Exception as ex:
                return {"error": ex}


    def getSession(self, id):
        url = ''.join(["https://fiu-uat.setu.co/sessions/", id])

        try:
                response = self.__requests.get(url, headers=self.__header)
                if(response.status_code == 200):
                    return {"response": response.status_code, "data": response.json()}
        except Exception as ex:
                return {"error": ex}


    def getFIPs(self):
        try:
                response = self.__requests.get("https://fiu-uat.setu.co/fips", headers=self.__header)
                if(response.status_code == 200):
                    return {"response": response.status_code, "data": response.json()}
        except Exception as ex:
                return {"error": ex}
