import base64
import mimetypes
import os
from urllib import request
import json
import binascii
from io import BytesIO
import codecs

writer = codecs.lookup("utf-8")[3]


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


def choose_boundary():
    """
    Our embarrassingly-simple replacement for mimetools.choose_boundary.
    """
    return binascii.hexlify(os.urandom(16)).decode('utf-8')


boundary = choose_boundary()


def upload_data(filename, file_data):
    # value = f'--{boundary}\n'
    # value += f'Content-Disposition: form-data; name="file"; filename="{filename}"\n'
    # value += 'Content-Type: application/octet-stream\n'
    # value += '\n'
    # value += str(base64.b64encode(file_data))
    # value += '\n'
    # value += f'--{boundary}--\n'
    # value += '\n'
    mine = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    body = BytesIO()
    body.write(f"--{boundary}\r\n".encode('utf-8'))
    body.write(f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode('utf-8'))
    body.write(f"Content-Type: {mine}\r\n".encode('utf-8'))
    body.write(b"\r\n")
    body.write(file_data)
    body.write(b"\r\n")
    body.write(f"--{boundary}--\r\n".encode('utf-8'))

    return body.getvalue()


def sample_upload():
    filename = 'sample.txt'
    with open(filename, 'rb') as f:
        data = upload_data(filename, f.read())
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}"
    }
    req = request.Request(
        url='http://127.0.0.1:5000/upload',
        data=data,
        headers=headers,
        method="POST"
    )
    with request.urlopen(req) as response:
        data = response.read()
        print(response.status)
        print(data)


if __name__ == '__main__':
    # sample_stream()
    # sample_download()
    sample_upload()
