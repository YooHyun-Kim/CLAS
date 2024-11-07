from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# 데이터베이스 연결
def get_db():
    db = sqlite3.connect('recipes.db')
    return db

# 홈페이지
@app.route('/')
def home():
    return render_template('home.html')

# 레시피 목록 보기
@app.route('/recipes')
def recipes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM recipes')
    recipes = cursor.fetchall()
    return render_template('recipe.html', recipes=recipes)

# 레시피 추가하기
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)',
                      (title, ingredients, instructions))
        db.commit()
        return redirect(url_for('recipes'))
    
    return render_template('recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
