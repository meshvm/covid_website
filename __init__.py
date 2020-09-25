import os
import requests
import json
from flask import Flask,render_template
'''
This function is known as the application factory. Any configuration, registration, and
other setup the application needs will happen inside the function, then the application will be returned.
'''

def create_app(test_config=None):  
    #application factory function
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/SearchMedicalColg')
    def index5():
        response = requests.get("https://api.rootnet.in/covid19-in/hospitals/medical-colleges")
        todos = json.loads(response.text)
        pr=todos['data']['medicalColleges']
        return render_template('SearchMedicalColg.html',pr=pr)  
    @app.route('/SearchHospitals')
    def index1():
        response = requests.get("https://api.rootnet.in/covid19-in/hospitals/beds")
        odos = json.loads(response.text)
        smry=odos['data']['summary']
        #print(pr)
        reg=odos['data']['regional']
        #print(pra)
        return render_template('SearchHospitals.html',smry=smry,reg=reg)      
    @app.route('/TestsReport')
    def index2():
        return render_template('TestsReport.html')
    @app.route('/HelplineCentre')
    def index3():
        response = requests.get("https://api.rootnet.in/covid19-in/contacts")
        todos = json.loads(response.text)
        a=todos['data']['contacts']['regional'] 
        return render_template('HelplineCentre.html',a=a)
    @app.route('/Notifications')
    def index4():
        responses = requests.get("https://api.rootnet.in/covid19-in/notifications")
        todo = json.loads(responses.text)
        tod=todo['data']['notifications']
        return render_template('Notifications.html',tod=tod)              

    return app
