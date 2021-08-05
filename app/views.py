from flask import render_template, request, redirect, url_for
from app import newsy

@newsy.route('/')
def homepagecontent():
    return render_template('homepage.html')