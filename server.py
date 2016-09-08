from helloworld import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/request-counter', methods=['GET'])
def counter():
    n = Random.select()
    if len(n) > 0:
        p = n[0].count + 1
        Random.update(count=p).execute()
    else:
        Random.create(count=1)
    count = Random.select()[0].count
    return 'Count: {}'.format(count)


app.run(debug=True)
