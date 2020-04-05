from flask import Flask
from flask import render_template

import googleapiclient.discovery as gcp
from oauth2client.client import GoogleCredentials

import os

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/phil/compte2.json'
credentials = GoogleCredentials.get_application_default()
service = gcp.build('compute', 'v1', credentials=credentials)


def start_instance(compute, project, zone, instance):
    compute.instances().start(project=project, zone=zone, instance=instance).execute()

def stop_instance(compute, project, zone, instance):
    compute.instances().stop(project=project, zone=zone, instance=instance).execute()


@app.route('/')
def hello_world():
    return render_template('base.html', title='minecraft')

@app.route('/demarrer')
def hello_world2():
    start_instance(service, 'colorisation', 'europe-west1-b', 'test4')
    return 'bouton'

@app.route('/arreter')
def hello_world3():
    stop_instance(service, 'colorisation', 'europe-west1-b', 'test4')
    return 'bouton'
