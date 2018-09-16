from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from graphtool import drawNetworkGraph
from keywords import *

app = Flask(__name__)

searchTerm = ''

@app.route('/', methods=['GET'])
def main():
    global searchTerm
    searchTerm = ''
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():
    global searchTerm
    d = request.get_json(force=True)
    searchTerm = d['query']
    return url_for('dashboard')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if searchTerm == '':
        return redirect(url_for('main'))
    # drawNetworkGraph(d, sentiments)
    d, sentiments = get_graph(searchTerm)
    # d, sentiments = ({'computer science': {'students': {'weight': 57.34121863799287},
    #                                        'googleforedu': {'weight': 43.776749446893206},
    #                                        'teachers': {'weight': 19.974516129032263},
    #                                        'intimidating': {'weight': 14.41436172812139},
    #                                        'math': {'weight': 4.6117383512544805},
    #                                        'history': {'weight': 3.381807108084572},
    #                                        'passions': {'weight': 16.631955840140066},
    #                                        'skills': {'weight': 16.631955840140066},
    #                                        'hobby_touya': {'weight': 3.8626543629611594},
    #                                        'lid': {'weight': 3.6351882240373516},
    #                                        'lightwave3d': {'weight': 4.335188224037354},
    #                                        '3dcg': {'weight': 5.11109625813707}},
    #                   'students': {'computer science': {'weight': 57.34121863799287},
    #                                'students': {'weight': 80.27102426247589},
    #                                'googleforedu': {'weight': 9.229677419354838}},
    #                   'googleforedu': {'computer science': {'weight': 43.776749446893206},
    #                                    'students': {'weight': 9.229677419354838},
    #                                    'googleforedu': {'weight': 78.43000417070324},
    #                                    'teachers': {'weight': 16.429354838709685}},
    #                   'teachers': {'computer science': {'weight': 19.974516129032263},
    #                                'googleforedu': {'weight': 16.429354838709685},
    #                                'teachers': {'weight': 51.96007765830343}}, 'intimidating': {'computer science': {
    #         'weight': 14.41436172812139}, 'intimidating': {'weight': 77.37188465444267}}, 'math': {
    #         'computer science': {'weight': 4.6117383512544805}, 'math': {'weight': 78.49886704096394}}, 'history': {
    #         'computer science': {'weight': 3.381807108084572}, 'history': {'weight': 23.416395429284158}}, 'passions': {
    #         'computer science': {'weight': 16.631955840140066}, 'passions': {'weight': 37.248391306813176}}, 'skills': {
    #         'computer science': {'weight': 16.631955840140066}, 'skills': {'weight': 54.028462235956134}},
    #                   'hobby_touya': {
    #                       'computer science': {'weight': 3.8626543629611594}, 'lightwave3d': {'weight':
    #                                                                                               15.210010918832165},
    #                       '3dcg': {'weight': 11.690900420715861}},
    #                   'lid': {'computer science': {'weight': 3.6351882240373516},
    #                           'lid': {'weight': 53.348649856476214}}, 'lightwave3d': {
    #         'computer science': {'weight': 4.335188224037354}, 'hobby_touya': {'weight': 15.210010918832165},
    #         'lightwave3d': {'weight': 26.494926400233453}, '3dcg': {'weight': 13.52710773395026}},
    #                   '3dcg': {'computer science': {'weight': 5.11109625813707},
    #                            'hobby_touya': {'weight': 11.690900420715861}, 'lightwave3d':
    #                                {'weight': 13.52710773395026}}},
    #                  {'computer science': {'color': 0.5491607279678484}, 'students': {'color': 0.48402029937170526},
    #                   'googleforedu': {'color': 0.7073953376641555}, 'teachers': {'color': 0.5599710810039497},
    #                   'intimidating': {'color': 0.6408747145018667}, 'math': {'color': 0.44731760775914725},
    #                   'history': {'color': 0.6185327157544797}, 'passions': {'color': 0.5814836978733093},
    #                   'skills': {'color': 0.6308493535838404}, 'hobby_touya': {'color': 0.5959127433140696},
    #                   'lid': {'color': 0.3889967700511042}, 'lightwave3d': {'color': 0.5795693029344643},
    #                   '3dcg': {'color': 0.5669733824400874}})
    drawNetworkGraph(d, sentiments)
    return render_template('dashboard.html')

@app.route('/getImage', methods=['GET'])
def getImage():
    return send_from_directory('static', 'Graph.png')

app.run()
