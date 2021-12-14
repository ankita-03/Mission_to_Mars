from flask import Flask, app, render_template, redirect, url_for
from flask_pymongo import Pymongo
import scrape_mars

app = Flask()
