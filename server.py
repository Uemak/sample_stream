from flask import Flask, Response
import time

app = Flask(__name__)


# ================= Basic Streaming =================

@app.route('/sample-stream')
def hello_world():
    with open("sample.txt", "r") as f:
        s = f.read()

    comments = [s[i:i+10000] for i in range(0, len(s), 10000)]
    print(comments)

    def generate():
        for comment in comments:
            yield comment
            time.sleep(0.01)  # 動作をわかりやすくするために追加

    return Response(generate())


if __name__ == "__main__":
    app.run(debug=True)
