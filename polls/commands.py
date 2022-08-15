from polls import app
from polls.db_actions import create_all_tables, create_user
from polls.data_manager import populate_db_with_counties_data, populate_db_with_election_data

@app.cli.command("create_tables")
def create_tables():
    create_all_tables()
      
@app.cli.command("create_user_to_test")     
def create_user_to_test():
    create_user()
    
@app.cli.command("populate_db_with_counties")     
def populate_db_with_counties():
    populate_db_with_counties_data()
    
@app.cli.command("populate_db_with_election")     
def populate_db_with_election():
    populate_db_with_election_data()