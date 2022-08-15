from polls.connection import get_connection
from mysql.connector import Error
from werkzeug.security import generate_password_hash

def create_all_tables():
    try:
        con = get_connection()
        with con.cursor() as cur:
            create_election_table_query = """
                    CREATE TABLE IF NOT EXISTS election ( 
                    idElection INT PRIMARY KEY AUTO_INCREMENT,
                    year YEAR(4) NOT NULL,
                    votecount INT NOT NULL,
                    political_party VARCHAR(100) NOT NULL,
                    county VARCHAR(50) NOT NULL ) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci"""
            create_county_table_query = """
                    CREATE TABLE IF NOT EXISTS county (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    code_county INT(50) NOT NULL,
                    county VARCHAR(50) NOT NULL,
                    population INT NOT NULL,
                    area DECIMAL(16,3) NOT NULL) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci"""
            create_coordinator_table_query = """
                    CREATE TABLE IF NOT EXISTS coordinator (
                    idCoordinator INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    document INT(9) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    password VARCHAR(200) NOT NULL) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci"""

            cur.execute(create_election_table_query)
            cur.execute(create_county_table_query)
            cur.execute(create_coordinator_table_query)
            con.commit()
            con.close()
            print("The tables were created successfully.")
    except Error as e:
        print("Error while we try to create the databases", e)
      
def create_user():
    try:
        con = get_connection()
        with con.cursor() as cur:
            name, document, email, password = "pepe", 123456789, "pepe@gmail.com", "pepepepe"
            pwd_hash = generate_password_hash(password)
            cur.execute("INSERT INTO coordinator(name, document, email, password) VALUES (%s, %s, %s, %s)" ,
                                (name, document, email, pwd_hash))
            print('User created successfully')
            con.commit()
            con.close()
    except Error as e:
        print("Error while creating a new user", e)

def check_user_exists(email):
    try: 
        con = get_connection()
        with con.cursor() as cur:
            cur.execute(f"SELECT * FROM coordinator WHERE email = '{email}'") #Check the user exists.
            user = cur.fetchone()
            con.close()
            return user
    except Error as e:
        print("Error while creating a new user", e)    
        
def create_election(year, votecount, political_party, county):
    try:
        con = get_connection()
        with con.cursor() as cur:
            cur.execute("INSERT INTO election(year, votecount, political_party, county) VALUES (%s, %s, %s, %s)",
                    (year, votecount, political_party, county))
            con.commit()
            con.close()
    except Error as e:
        print("Error while creating a new election", e)

def create_county(code_county, county, population, area):
    try:
        con = get_connection()
        with con.cursor() as cur:
            cur.execute("INSERT INTO county(code_county, county, population, area) VALUES (%s, %s, %s, %s)",
                    (code_county, county, population, area))
            con.commit()
            con.close()
    except Error as e:
        print("Error while creating a new county", e)