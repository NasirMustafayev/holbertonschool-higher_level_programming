from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"items": []}

    return render_template('items.html', items=data.get('items', []))

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == "json":
        with open("products.json") as f:
            data = json.load(f)
    elif source == "csv":
        with open("products.csv") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    elif source == "sql":
        connect =  sqlite3.connect("products.db")
        cursor = connect.cursor()
        
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        connect.close()

    else:
        return render_template('product_display.html', error="Wrong source")

    if id:
        data = [item for item in data if str(item.get('id')) == id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    