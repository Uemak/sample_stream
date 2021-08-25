from urllib import request
import json


def sample_stream():
    with request.urlopen('http://127.0.0.1:5000/sample-stream') as response:
        json_load = [json.loads(line) for line in response]
    print(json_load)
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
    sample_stream()
    # sample_download()
