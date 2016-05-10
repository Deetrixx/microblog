#!/usr/bin/python

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user={'nickname':'Robot'} #fake user
    posts =[ #fake array of posts
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Susan'},
            'body':'The Avengers movie was so cool!'
         }
     ]
    return render_template('index.html',
                            title='Home',
                            user=user
                            posts=posts)

@app.route('/')
@app.route('/about')

def about():
    user={'nickname':''} #fake user
    posts =[ #fake array of posts
        {
            'author':{'nickname':'Joan'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Suan'},
            'body':'The Avengers movie was so cool!'
         }
     ]

    return render_template('about.html',
                            title='About',
                            user=user,
                            posts=posts)

