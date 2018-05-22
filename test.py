from flask import Flask, redirect, render_template, request, url_for
import sqlite3


def createDbTable():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    text TEXT
                    )''')
    con.commit()
    con.close()


def textToDb(text):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO data (text)
                    VALUES('{}')
                    '''.format(text))
    con.commit()
    cur.execute('''SELECT text FROM data
                    ORDER BY RANDOM()
                    LIMIT 3''')
    con.commit()
    result = cur.fetchall()
    con.close()
    return result

app = Flask(__name__)
createDbTable()


@app.route('/', methods=['POST', 'GET'])
def index():
    text = []
    if request.method == 'POST':
        text = textToDb(request.form['input-text'])
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(port=7777, debug=True)
