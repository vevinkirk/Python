import requests
import multiprocessing

url = "https://kevin.nebulacyber.com/polls/1/vote/"
data ={'csrfmiddlewaretoken':'zM0zUiY3qaXPqfEHxFoDWuuAKsv58tDZISSINC4ncR51lNJTWkgneMYmejGlcHUt','choice':'1'}
cookies = {'csrftoken':'s3KLynghCAsyLCVWMpkpEDa975MmcBTHB9CUrHmBohAKGa08b4c9WVEVBWXCgPab'}

def req_split(r):
    #requests.head is much faster than requests.get if your intention is only to get the status code
    req = requests.post(url,data=data,cookies=cookies)

    if req.status_code == 200:
	    temp = r #return the url string if the server report OK
    else:
	    temp = 0
    return temp

requests.post(url,data=data,cookies=cookies)

with multiprocessing.Pool(100) as p:
    pm = p.imap_unordered(req_split,data)
    pm = [i for i in pm if i]
