from urllib import request
import json

with request.urlopen('http://127.0.0.1:5000/sample-stream') as response:
    res_txt = response.read().decode('utf-8')

res_txt = f'[{res_txt.replace("}{", "},{")}]'
json_load = json.loads(res_txt)
print(json_load[20]["a"])
