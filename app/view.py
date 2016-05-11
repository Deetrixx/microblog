#!/usr/bin/python

from flask import render_template, flash, redirect
from app import app
from .form import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="%s", remember_me=%s' %
               (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])



@app.route('/')
@app.route('/index')

def index():
    user={'nickname':'Deetrixx'} #fake user
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
                            user=user,
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
