from flask import Flask, render_template, jsonify, abort
import csv

app = Flask(__name__)

def cargar_productos():
    productos = []
    with open('productos.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            fila['id'] = int(fila['id'])
            fila['precio'] = float(fila['precio'])
            productos.append(fila)
    return productos

@app.route('/productos')
def lista_productos():
    productos = cargar_productos()
    return render_template('productos.html', productos=productos)

@app.route('/api/productos')
def api_productos():
    productos = cargar_productos()
    return jsonify(productos)

@app.route('/productos/<int:id>')
def detalle_producto(id):
    productos = cargar_productos()
    producto = next((p for p in productos if p['id'] == id), None)
    if not producto:
        abort(404)
    return render_template('producto_detalle.html', producto=producto)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/productos/tabla')
def tabla_productos():
    productos = cargar_productos()
    return render_template('productos_tabla.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
