from flask import Flask, request, redirect

app = Flask(__name__)


class CustomExceptionHandler(Exception):
    pass


# Our options are to either modify the debugger file or modify the exception itself, the latter is cleaner.
CustomExceptionHandler.__name__ = "CTF{Bug_F0unD!}"


@app.after_request
def add_flag(response):
    response.headers["Server"] = "CTF{Werkzeug/3.0.1}"
    return response


@app.route('/')
def calculator():
    x = request.args.get("x")
    y = request.args.get("y")

    if not x or not y:
        return redirect("/?x=1&y=1")
    try:
        return f"{x} + {y} = {int(x) + int(y)}"
    except Exception as e:
        raise CustomExceptionHandler(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
