import requests, json, settings 
headers = {'content-type': 'application/json'}
BASE_URL=settings.BASEURL
def runtest():
    try:
        print("============GET LOGS=============")
        url = 'http://{}/logs'.format(BASE_URL)
        x = requests.get(url,headers=headers)
        x.raise_for_status
        print("GET {}".format(x.text))
        print("============Finished GET LOGS=============")

        print("============POST LOGS=============")
        url = 'http://{}/addlog'.format(BASE_URL)
        myobj = json.dumps({'source': 'online','logs':"asdfsdafsdafa"})
        x = requests.post(url, data = myobj,headers=headers)
        x.raise_for_status
        id=x.json().get('id')
        print("POST {}".format(x.text))
        if not id:
            raise Exception("Post failed to add data")
        print("TEST OK.")
        print("============POST LOGS=============")

        print("============GET SINGLE LOGS=============")
        url = 'http://{0}/logs/{1}'.format(BASE_URL,id)
        x = requests.get(url,headers=headers )
        x.raise_for_status
        print("GET OBJECT {}".format(x.text))
        print("============Finished GET SINGLE LOGS=============")
        
        print("============Delete SINGLE LOGS=============")
        url = 'http://{0}/deletelog/{1}'.format(BASE_URL,id)
        x = requests.get(url,headers=headers )
        x.raise_for_status
        print("Delete OBJECT {}".format(x.text))
        print("============Finished Delete SINGLE LOGS=============")

        print("TEST OK.")
    except:
        print("TEST FAILED")
        raise
    
if __name__ == '__main__':
  runtest()