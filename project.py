from flask import Flask, render_template
import sqlite3
import database_setup


app = Flask(__name__)
db_name = 'project_data.db'


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/list')
def listview():
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('select * from continent')
        rows = cur.fetchall()
        conn.close()
        return render_template('list.html', rows=rows)
    except RuntimeError:
        return render_template('error500.html')


@app.route('/continent_detail/<continent_id>')
def detail(continent_id):
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('select * from country where continent_id=?', continent_id)
        countries = cur.fetchall()
        conn.close()
        return render_template('detail.html', countries=countries)
    except RuntimeError:
        return render_template('error500.html')


@app.route('/country/<country_id>')
def livestock_list(country_id):
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('select * livestock where country_id=?', country_id)
        livestocks = cur.fetchall()
        conn.close()
        return render_template('livestock.html', livestocks=livestocks)
    except RuntimeError:
        return render_template('error500.html')


@app.errorhandler(404)
def pageDoesntExist(e):
    return render_template("error404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error500.html"), 500


if __name__ == "__main__":
    app.run()