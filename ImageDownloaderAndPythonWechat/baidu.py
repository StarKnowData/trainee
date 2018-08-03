import requests

url = "https://www.lagou.com/jobs/list_%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86?px=default&city=%E5%8C%97%E4%BA%AC#filterBox"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "f8f67a4e-ce27-4a43-97bc-de35b4524638"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)