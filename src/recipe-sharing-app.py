# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS recipes
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT NOT NULL,
         ingredients TEXT NOT NULL,
         instructions TEXT NOT NULL,
         author TEXT NOT NULL,
         created_date DATETIME,
         rating FLOAT DEFAULT 0)
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM recipes ORDER BY created_date DESC')
    recipes = c.fetchall()
    conn.close()
    return render_template('index.html', recipes=recipes)

@app.route('/upload', methods=['GET', 'POST'])
def upload_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        author = request.form['author']
        
        conn = sqlite3.connect('recipes.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO recipes (title, ingredients, instructions, author, created_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, ingredients, instructions, author, datetime.now()))
        conn.commit()
        conn.close()
        
        return redirect(url_for('home'))
    return render_template('upload.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
