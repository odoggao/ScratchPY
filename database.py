import json
import os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 1. Initialize the app with a service account certificate
# Make sure to replace the path with your actual service account file path
cred = credentials.Certificate('firebase-cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://doggao-discord-default-rtdb.firebaseio.com/' # Replace with your database URL
})

load_dotenv()

version = "scratch"
def set_value(database: str, id, variable: str, value):
    if isinstance(id,str):
        pass
    else:
        id = str(id)
    ref = db.reference(version + "/" + database)
    if ref:
        users_ref = ref.child(id)
        users_ref.update({variable: value})
def get_value(database: str, id,variable: str, default = None):
    if isinstance(id,str):
        pass
    else:
        id = str(id)
    ref = db.reference(version + "/" + database + "/" + id)
    if ref.get() == None:
        if default != None:
            set_value(database,id,variable,default)
        return default
    else:
        try:
            value = ref.get()[variable]
            if value == None:
                set_value(database,id,variable,default)
                return default
            return value
        except KeyError:
            pass
        if default != None:
            set_value(database,id,variable,default)
        return default
def remove_value(database:str, id):
    try:
        ref = db.reference(version + "/" + database + "/" + id)
        ref.delete()
    except:
        pass
def get_values(database):
    ref = db.reference(version + "/" + database )
    if ref.get() == None:
        return {}
    return ref.get()