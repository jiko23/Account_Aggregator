from fastapi import FastAPI
from ConsentRequests import ConsentRequests
from ConsentDetails import ConsentDetail, FilterData, Fidata, DataLifeSpan, PurposeforDetail, SessionData

global connection
connection = ConsentRequests()

app = FastAPI()

@app.get("/home", tags = ["Welcome Page"])
def welcomePage():
    return {"Welcome to AA Integration Project API!!!!!"}


@app.post("/postconsent", tags = ["Post Consent"])
def postConsent(consent_detail : ConsentDetail, filter_data : FilterData, freq : Fidata, datalife : DataLifeSpan, purpose: PurposeforDetail):
    consent_details = {
    "Detail": {
        "consentStart": consent_detail.consentStart,
        "consentExpiry": consent_detail.consentExpiry,
        "Customer": consent_detail.Customer,
        "FIDataRange": consent_detail.FIDataRange,
        "consentMode": consent_detail.consentMode,
        "consentTypes": consent_detail.consentTypes,
        "fetchType": consent_detail.fetchType,
        "Frequency": {
            "value": freq.value,
            "unit": freq.unit
        },
        "DataFilter": [
            {
                "type": filter_data.type,
                "value": filter_data.value,
                "operator": filter_data.operator
            }
        ],
        "DataLife": {
            "value": datalife.value,
            "unit": datalife.unit
        },
        "DataConsumer": consent_detail.DataConsumer,
        "Purpose": {
            "Category": purpose.Category,
            "code": purpose.code,
            "text": purpose.text,
            "refUri": purpose.refUri
        },
        "fiTypes": consent_detail.fiTypes
    },
    "redirectUrl": consent_detail.redirectUrl
    }

    response = connection.sendConsentPayload(consent_details)

    if(response["status_code"] == 201):
        return {"status_code": response["status_code"], "id": response["response"]["id"], "consent_status": response["response"]["status"], "consent_details": response["response"]}
    else:
        return {"Error in sending payload"}



@app.get("/getconsent/{consentId}", tags = ["Get Consent"])
def getConsent(consentId : str):
    reply = connection.getConsents(consentId)

    if reply["response"] == 200:
        return {"status_code": reply["response"], "consent_status": reply["data"]}
    else:
        return {"Couldnot fetch consent details"}


@app.post("/createsession", tags = ["Create Data Session"])
def postDataSession(session : SessionData):
    session_data = {"consentId":session.consentId,
                    "DataRange":{
                            "from":session.fromdate,
                            "to":session.todate
                        },
                    "format":session.format
                    }
    
    response = connection.sendSessionPayload(session_data)
    print(response["response"])
    if((response["status_code"] == 201) or (response["status_code"] == 200)):
        return {"status_code": response["status_code"], "session": response["response"]}
    else:
        return {"Could not create data session"}


@app.get("/getsession/{sessionId}", tags = ["Get FI Data"])
def getDataSession(sessionId: str):
    reply = connection.getSession(sessionId)

    if reply["response"] == 200:
        return {"status_code": reply["response"], "session": reply["data"]}
    else:
        return {"Couldnot fetch session details for the consentID"}


@app.get("/fips", tags = ["FIPs List"])
def getFIP():
    reply = connection.getFIPs()

    if reply["response"] == 200:
        return {"status_code": reply["response"], "fips": reply["data"]}
    else:
        return {"Couldnot fetch fips data"}

