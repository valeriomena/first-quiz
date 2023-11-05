import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

def sql_pets_owned_by_nobody ():
    conn = sqlite3.connect("quiz_pets")
    c = conn.cursor()
    c.execute('''
        SELECT name, species, age 
        FROM animals 
        WHERE animal_id NOT IN (SELECT pet_id FROM people_animals)
    ''')
    pet = c.fetchall()
    conn.close()
    return pet
    
# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

def sql_pets_older_than_owner ():
    conn = sqlite3.connect('quiz_pets')
    c = conn.cursor()
    c.execute('''
        SELECT COUNT(*) AS count
        FROM animals A
        JOIN people_animals PA ON A.animal_id = PA.pet_id
        JOIN people P ON PA.owner_id = P.person_id
        WHERE A.age > P.age
    ''')
    pet = c.fetchone()[0]
    print(pet)
    conn.close()
    return pet

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)

def sql_only_owned_by_bessie ():
    conn = sqlite3.connect("quiz_pets")
    c = conn.cursor()
    c.execute('''
        SELECT P.name, A.name, A.species
        FROM animals A
        JOIN people_animals PA ON A.animal_id = PA.pet_id
        JOIN people P ON PA.owner_id = P.person_id
        WHERE P.name = 'bessie'
          AND NOT EXISTS (
            SELECT 1 FROM people_animals PA2
            WHERE PA2.pet_id = A.animal_id AND PA2.owner_id != P.person_id
        )
    ''')
    pet = c.fetchall()
    conn.close()
    return pet