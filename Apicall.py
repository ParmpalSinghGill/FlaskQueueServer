import time

import requests,json

baseAddress="http://127.0.0.1:5000/"
def simpleApi():
    resp=requests.get(baseAddress)
    print(resp.text)

def enqueueTask():
    resp = requests.post(baseAddress+"enqueue",json='Shonki')
    jobid=json.loads(resp.text)["job_id"]
    print(jobid,"Started")
    return jobid

def checkstatus(jobid):
    while True:
        resp=requests.get(baseAddress+"check_status?job_id="+jobid)
        job_status = json.loads(resp.text)["job_status"]
        print("job_status ",job_status)
        if job_status=="finished":
            return
        time.sleep(1)


def getresult(jobid):
    resp=requests.get(baseAddress+"get_result?job_id="+jobid)
    print(resp.text)


# simpleApi()

for i in range(5):
    jobid=enqueueTask()

# checkstatus(jobid)
#
# getresult(jobid)