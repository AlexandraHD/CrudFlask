from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] =  'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] =  'flask_crudwebflask'
app.config['MYSQL_PORT'] =  3308
mysql = MySQL(app)

@app.route("/")
def saludo ():
    return render_template("index.html")

@app.route("/users")
def user (datos = dict()):
    try:
        sql = """
                SELECT id_user, name, message
                FROM users
            """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        datos["users"] = cursor.fetchall()
        cursor.close()

    except:
        datos["error"]="Error al consultar los usuarios"

    return render_template("users.html", modelo = datos)

@app.route("/users/new", methods = ["POST"] )
def new_user ():
    name = request.form["name"]
    message = request.form["message"]
    
    datos = dict()
    try:
        sql = f"""
                INSERT INTO users (name, message)
                VALUES ('{name}','{message}');
            """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        filas = cursor.rowcount
        mysql.connection.commit()
        cursor.close()
        if filas != 1:
            datos["error"] = "Numero de filas afectadas no es correcto"
        else:
            datos["exito"] = f"El mensaje fue registrado exitosamente"

    except:
        datos["error"] = "Error al insertar los datos del usuario."

    
    return users(datos)

@app.route("/match")
def match ():
    return render_template("match.html")

app.run()