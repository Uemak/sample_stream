import base64
import os

from flask import Flask, Response, make_response, request, jsonify
import time

app = Flask(__name__)


# ================= Basic Streaming =================

@app.route('/sample-stream')
def hello_world():
    with open("sample.txt", "r") as f:
        s = f.read()

    comments = [s[i:i+100] for i in range(0, len(s), 100)]
    print(comments)

    def generate():
        for comment in comments:
            yield comment
            time.sleep(0.01)  # 動作をわかりやすくするために追加

    return Response(generate())


@app.route('/download')
def sample_download():
    filename = 'c03.zip'
    response = make_response()
    with open(filename, 'rb') as file_data_binary:
        response.data = file_data_binary.read()
    response.headers["Content-Disposition"] = "attachment; filename=" + filename
    response.mimetype = 'application/octet-stream'

    return response


@app.route('/upload', methods=['POST'])
def sample_upload():
    req_file = request.files['file']
    file_name = req_file.filename
    req_file.save(os.path.join('upload', file_name))

    return make_response(jsonify({'result': 'upload json OK.'}))


if __name__ == "__main__":
    app.run(debug=True)
