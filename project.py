import mysql.connector
from mysql.connector import Error

def create_connection():
    connection=None
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="python_connect"
        )
        print("Connexion établi à la database")
    except Error as e:
        print(f"Erreur:{e} est survenu")
    return connection

connection=create_connection()

# crée une table.
def create_table(connection):
    sql_create_project_table="""CREATE TABLE IF NOT EXISTS projects(
                                        id INT AUTO_INCREMENT,
                                        name VARCHAR(255),
                                        description TEXT,
                                        PRIMARY KEY (id)
                                    )"""
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.execute(sql_create_project_table)
        print("la table a été crée avec succes")
    else:
        print("Erreur: l'opération à échouer !")

# => table=create_table(connection)

project={
     'id':1,
     'name':'vente de vetement tradit/moderne',
     'description':"création d'un stand de vente de vétement"
}


   
def create_project(connection, project):
    cursor=connection.cursor()
    query="INSERT INTO projects(name, description) VALUES(%s, %s)"
    cursor.execute(query, (project['name'], project['description']))
    connection.commit()
    print("Projet crée avec succes !")

# =>ajout_projet=create_project(connection, project)

def read_projects(connection):
    cursor=connection.cursor()
    query="SELECT* FROM projects"
    cursor.execute(query)
    rows=cursor.fetchall()

    for row in rows:
        print(f"ID:{row[0]}, Name:{row[1]}, Description: {row[2]}")

# =>lire=read_projects(connection)

def update_project(connection, project):
    cursor=connection.cursor()
    query="UPDATE projects SET name = %s, description = %s WHERE id = %s"
    cursor.execute(query, (project['name'], project['description'], project['id']))
    connection.commit()
    print("Projet mis à jour")

# => mise_a_jour=update_project(connection, project)

def delete_project(connection, project_id):
    cursor=connection.cursor()
    query="DELETE FROM projects WHERE id=%s"
    cursor.execute(query, (project_id,))
    connection.commit()
    print("Le projet a été supprimé")

# =>project_id= project['id']
# => Supprimer_projet=delete_project(connection, project_id)

def read_one_project(connection,project_id):
    cursor=connection.cursor()
    query="SELECT*FROM projects WHERE id=%s"
    cursor.execute(query, (project_id,))
    rows=cursor.fetchall()
    for row in rows:
     print(f"ID:{row[0]}, Name:{row[1]}, Description:{row[2]}")

project_id=project["id"]
read_one=read_one_project(connection, project_id)