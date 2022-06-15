#create a simple flask app
#import the flask modules
from flask import *

#import the text_summarizer function from .worker.py
from worker import text_summarizer

#initialize the flask app
app = Flask(__name__)

#create a route for the default page
@app.route('/' , methods=['POST'])
def index():
    if request.method == 'POST':
        #get the text from the form
        text = request.form['text']
        return {
            "summary" : text_summarizer(str(text))
        }
    else:
        #method not allowed
        return "Method not allowed"


#run the app on threaded mode
if __name__ == '__main__':
    app.run(threaded=True , debug=True)