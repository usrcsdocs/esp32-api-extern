from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

conexion = MySQL(app)


@app.route('/')
def index():
    return "unknow - suscribete versión dos"

@app.route('/cursos')
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        
        cursos = []
        for fila in datos:
            curso = {'codigo': fila[0], 'nombre': fila[1], 'creditos': fila[2],}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': "Cursos Listados.", 'exito': True})

    except Exception as ex:
        return jsonify({'mensaje':"Error", 'exito': False})




def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>"



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)

    app.run()

