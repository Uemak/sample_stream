from urllib import request
import json


def sample_stream():
    with request.urlopen('http://127.0.0.1:5000/sample-stream') as response:
        res_txt = response.read().decode('utf-8')

    res_txt = f'[{res_txt.replace("}{", "},{")}]'
    json_load = json.loads(res_txt)
    print(json_load[20]["a"])


def sample_download():
    with request.urlopen('http://127.0.0.1:5000/download') as response:
        data = response.read()
        filename = response.headers.get_filename()
        print(response.status)
    if filename:
        with open(f'output/{filename}', mode="wb") as f:
            f.write(data)


if __name__ == '__main__':
    # sample_stream()
    sample_download()
