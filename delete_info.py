#Delete Info with DELETE Rqequest
import requests

url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

parameters = {"UCID": "mkm", "section": "103"}

response = requests.delete(url, params=parameters)

if response.status_code == 200:
    print("Success")
    print("Status: ", response.status_code)
    print("Body: ", response.text)
else:
    print("Failure")
    print("Status: ", response.status_code)
    print("Body: ", response.text)