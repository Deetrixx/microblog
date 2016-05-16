#!/usr/bin/python
import os

WTF_CRSF_ENABLED =True
SECRET_KEY='you-will-never-guess'


OPENID_PROVIDERS = [
    {'name':'Google','url':'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo','url':'https://me.yahoo.com'},
    {'name':'AOL','url':'https://openid.aol.com/<username>'},
    {'name':'Flickr','url':'https://www.flickr.com/<username>'},
    {'name':'MyOpenID','url':'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))s

SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir,'app.db') #required by Flask SQLALchemy ext,path to of our database file
SQLALCHEMY_DATABASE_REPO= os.path.join(basedir,'db_repository') #folder where we will store the SQLAlchemy-migrate data files.
