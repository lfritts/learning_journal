# -*- coding: utf-8 -*-
from flask import Flask
import os

DB_SCHEMA = """
DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
    id serial PRIMARY KEY,
    title VARCHAR (127) NOT NULL,
    text TEXT NOT NULL,
    created TIMESTAMP NOT NULL
)
"""

app = Flask(__name__)
app.config['DATABASE'] = os.environ.get(
    'DATABASE_URL', 'dbname=learning_journal user=miked, lfritts'
)


@app.route('/')
def hello():
    return u'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)
