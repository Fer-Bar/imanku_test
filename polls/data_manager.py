import json
from csv import reader
from polls.db_actions import create_county, create_election

def populate_db_with_counties_data():     
    with open('clean_counties.csv', 'r', encoding='utf-8') as read_obj:
        csv_reader = reader(read_obj)
        try:
            print('Adding county data to the database...')
            for row in csv_reader:
                code_county = row[1]
                county = row[2]
                population = row[3]
                area = row[4]           
                create_county(int(code_county), county, int(population), float(area))
            print("The counties were added.")
        except Exception as e:
            print("There was an error creating the counties: ", e)
            
def populate_db_with_election_data():
    f = open('elections.json', 'r')
    data = json.load(f)
    code_county_dict = code_and_county_dict()
    try:
        print('Adding election data to the database...')   
        for i in range(1, len(data)+1):
            list_pol_party = {'democrat': data[i]['democrat'], 
                                'republic': data[i]['republic'],
                                'other': data[i]['other']}
            year = data[i]['year']
            total_votecount = sum([data[i]['democrat'], data[i]['republic'], data[i]['other']])
            win_political_party = max(list_pol_party, key=list_pol_party.get)
            county = code_county_dict.get(data[i]['codecounty'], 'Unknown')
            create_election(year, total_votecount, win_political_party, county)
    except Exception as e:
        print()

def code_and_county_dict():
    with open('county_and_code.csv', 'r', encoding='utf-8') as read_obj:
        csv_reader = reader(read_obj)
        code = []
        county = []
        for row in csv_reader:
            code.append(row[0])
            county.append(row[1])
        dict_from_list = dict(zip(code, county))
        return dict_from_list
    
