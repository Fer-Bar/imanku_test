from polls import app
from connection import get_connection
from mysql.connector import Error
from werkzeug.security import generate_password_hash

@app.cli.command("create_tables")
def create_tables():
  try:
    con = get_connection()
    with con.cursor() as cur:
      create_election_table_query = """
                    CREATE TABLE IF NOT EXISTS election ( 
                    idElection INT PRIMARY KEY AUTO_INCREMENT,
                    year YEAR(4) NOT NULL,
                    votecount INT NOT NULL,
                    political_party VARCHAR(100) NOT NULL,
                    code_county INT(5) NOT NULL )"""
      create_county_table_query = """
                    CREATE TABLE IF NOT EXISTS county (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    county_code INT(50) NOT NULL,
                    county VARCHAR(50) NOT NULL,
                    population INT NOT NULL,
                    area DECIMAL(6,3) NOT NULL)"""
      create_coordinator_table_query = """
                    CREATE TABLE IF NOT EXISTS coordinator (
                    idCoordinator INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    document INT(9) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    password VARCHAR(200) NOT NULL ) """
                    
      cur.execute(create_election_table_query)
      cur.execute(create_county_table_query)
      cur.execute(create_coordinator_table_query)
      con.commit()
      print('The tables were created successfully.')
      
  except Error as e:
      print("Error while we try to create the databases", e)
      
@app.cli.command("create_user_to_test")     
def create_user_to_test():
  try:
    con = get_connection()
    with con.cursor() as cur:
      name, document, email, password = "pepe", 123456789, "pepe@gmail.com", "pepepepe"
      pwd_hash = generate_password_hash(password)
      cur.execute("INSERT INTO coordinator(name, document, email, password) VALUES (%s, %s, %s, %s)" ,
                          (name, document, email, pwd_hash))
      con.commit()
      con.close()
  except Error as e:
    print("Error while creating a new user", e)