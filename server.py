from helloworld import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    hello = Random(text='Helloka')
    hello.save()
    return 'Hello world!'

app.run(debug=True)
