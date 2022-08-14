import mysql.connector

def get_connection():
  """Return the connection to the db"""
  con = mysql.connector.connect(
  user="root",
  host="127.0.0.1",
  password="fermysql3306",
  database="election"
  )
  return con

    
