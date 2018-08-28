from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

COUNTS = 0

@app.route('/request_counter', methods=['GET'])
def request_counter():
    global COUNTS
    COUNTS += 1
    print(COUNTS)
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'qwerasdfzxcv1234'
    app.run(
        host='0.0.0.0',
        debug=True,
        port=4321
    )
