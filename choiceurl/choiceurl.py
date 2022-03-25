#import all important modules
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
from werkzeug.utils import secure_filename
#create a blueprint for the app to be broken into multiple file
bp = Blueprint('choiceurl',__name__)

#establish a route to homepage using the app blueprint
@bp.route('/')
def home():
    return render_template('home.html',codes=session.keys())

#create another routes that redirects user to a page with their url
@bp.route('/your_url', methods=['GET','POST'])
def your_url():
    #determine type of request first
    if request.method == 'POST':
        #if request is POST, then 
        urls = {}
        #check to see if json document exists and load data into a dictionary
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        
        #check to see if code already exists and send a message to user
        if request.form['code'] in urls.keys():
            flash('That name has already been taken, choose another one')
            return redirect(url_for('choiceurl.home'))

        #allocate a url to a particular genearated code
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            #if input from form is a file, save it as a file and enter code in json
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/home/prussy/url-shortener/choiceurl/static/user_files/' + full_name)
            urls[request.form['code']] = {'file': full_name}

        #display code in your_url page
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
            session[request.form['code']] = True
        return render_template('your-url.html', code=request.form['code'])
    else:
        #if method is get, redirect user to homepage
        return redirect(url_for('choiceurl.home'))

#route takes in code as input and redirects user to the code url
@bp.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static',filename='user_files/'+urls[code]['file']))
    #if wrong string code is entered, return error
    return abort(404)

#route creates a better error message
@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page-not-found.html'), 404

#route creates an API endpoint for user
@bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))

#route redirects user to siteplan
@bp.route('/site')
def site():
    return render_template('siteplan.html')
