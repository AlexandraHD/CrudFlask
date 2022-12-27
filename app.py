from importlib.metadata import requires
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

    
    return user(datos)


@app.route("/users/edit/<id_user>")
def edit(id_user: str):
    datos = dict()
    try:
        if id_user == None or len(id_user) == 0:
            raise Exception("El codigo no puede estar vacio")
        
        # Consultar la informacion del estudiante con codigo = id
        sql = f"""
            SELECT id_user, name, message
            FROM users
            WHERE id_user = '{id_user}'
            """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        # Cargar la informacion del estudiante en la plantilla
        datos["users"] = cursor.fetchone()
        print(datos)
        cursor.close()

        # Mostrar la plantilla
        return render_template("users_edit.html", modelo = datos)
    except Exception as ex:
        datos["error"] = str(ex)
        return user(datos)
    
@app.route("/users/update", methods = ["POST"])
def update():
    id_user = request.form["id_user"]
    name = request.form["name"]
    message = request.form["message"]

    datos = dict()
    try:
        sql = f"""
                UPDATE users
                SET name = '{name}',
                    message = '{message}',
                WHERE id_user = '{id_user}'
            """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        filas = cursor.rowcount
        mysql.connection.commit()
        cursor.close()
        if filas != 1:
            datos["error"] = "Numero de filas afectadas no es correcto"
        else:
            datos["exito"] = f"Usuario '{id_user}' fue actualizado exitosamente"

    except:
        datos["error"] = "Error al actualizar los datos"

    return user(datos)

@app.route("/users/delete/<id_user>")
def delete(id_user: str):
    datos = dict()
    try:
        if id_user == None or len(id_user) == 0:
            raise Exception("El codigo no puede estar vacio")
        
        # Consultar la informacion del estudiante con codigo = id
        sql = f"""
            DELETE
            FROM users
            WHERE id_user = '{id_user}'
            """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        filas = cursor.rowcount
        mysql.connection.commit()
        cursor.close()
        if filas != 1:
            datos["error"] = "Numero de filas afectadas no es correcto"
        else:
            datos["exito"] = f"Usuario eliminado exitosamente"
    except Exception as ex:
        datos["error"] = str(ex)
        
    return user(datos)

@app.route("/match")
def match ():
    return render_template("match.html")

app.run()