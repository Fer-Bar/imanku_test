import mysql.connector

def get_connection():
  """Return the connection to the db"""
  con = mysql.connector.connect(
  user="user",
  host="127.0.0.1",
  password="yourpassword",
  database="election"
  )
  return con

    
