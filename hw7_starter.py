# Name:
# Student ID:
# Email:
# List who you have worked with on this homework:
# List any AI tool (e.g. ChatGPT, GitHub Copilot):


import unittest
import sqlite3
import json
import os


def read_data_from_file(filename):
    """
    Reads data from a file with the given filename.

    Parameters
    -----------------------
    filename: str
        The name of the file to read.

    Returns
    -----------------------
    dict:
        Parsed JSON data from the file.
    """
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data


def set_up_database(db_name):
    """
    Sets up a SQLite database connection and cursor.

    Parameters
    -----------------------
    db_name: str
        The name of the SQLite database.

    Returns
    -----------------------
    Tuple (Cursor, Connection):
        A tuple containing the database cursor and connection objects.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn


def set_up_types_table(data, cur, conn):
    """
    Sets up the Types table in the database using the provided Pokemon data.

    Parameters
    -----------------------
    data: list
        List of Pokemon data in JSON format.

    cur: Cursor
        The database cursor object.

    conn: Connection
        The database connection object.

    Returns
    -----------------------
    None
    """
    type_list = []
    for pokemon in data:
        pokemon_type = pokemon["type"][0]
        if pokemon_type not in type_list:
            type_list.append(pokemon_type)
        if len(pokemon["type"]) > 1:
            pokemon_type = pokemon["type"][1]
            if pokemon_type not in type_list:
                type_list.append(pokemon_type)
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Types (id INTEGER PRIMARY KEY, type TEXT UNIQUE)"
    )
    for i in range(len(type_list)):
        cur.execute(
            "INSERT OR IGNORE INTO Types (id,type) VALUES (?,?)", (i,
                                                                   type_list[i])
        )
    conn.commit()


#############################################################################
####### START HERE, DO NOT CHANGE THE CODE FROM THE ABOVE FUNCTIONS ########
#############################################################################

def create_pokemon_table(data, cur, conn):
    """
    Parameters
    -----------------------
    data: str
        Stores pokemon.json, written in JSON format
    
    cur: 
        database cursor
    
    conn: 
        database connection

    Returns
    -----------------------
    Nothing
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_pokemon_by_attack_range(attack_min, attack_max, cur):
    """
    Parameters
    -----------------------
    attack_min: int

    attack_max: int
    
    cur: 
        database cursor

    Returns
    -----------------------
    list:
        list of tuples [(pokemon_id, name, attack),...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_balanced_pokemon_above_health(health_min, cur):
    """
    Parameters
    -----------------------
    health_min: int
    
    cur: 
        database cursor

    Returns
    -----------------------
    list:
        list of tuples [(pokemon_id, name, special_attack, special_defense, health_points),...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_pokemon_HP_above_speed_attack(health_points, speed, attack, cur):
    """
    Parameters
    -----------------------
    health_points: int
    
    speed: int

    attack: int

    Returns
    -----------------------
    list:
        list of tuples [(pokemon name, speed, attack, defense),...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_pokemon_by_type(type_value, cur):
    """
    Parameters
    -----------------------
    type_value: str

    Returns
    -----------------------
    list:
        list of tuples [(pokemon_id, name, type1, type2),...]

    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_fastest_pokemon_of_type(type, cur):
    """
    Parameters
    -----------------------
    type: str

    cur:
        database cursor
    
    Parameters
    -----------------------
    list:
        list of tuples: [(name, type, speed), ...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass





### DO NOT CHANGE TEST CASES ###
class TestAllMethods(unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(path + "/" + "pokemon.db")
        self.cur = self.conn.cursor()
        self.data = read_data_from_file("pokemon.json")


    def test_pokemon_table(self):
        self.cur.execute("SELECT * from Pokemon")
        pokemon_list = self.cur.fetchall()
        self.assertEqual(len(pokemon_list), 500)
        self.assertEqual(len(pokemon_list[0]), 10)
        self.assertIs(type(pokemon_list[0][0]), int)
        self.assertIs(type(pokemon_list[0][1]), str)
        self.assertIs(type(pokemon_list[0][2]), int)
        self.assertIs(type(pokemon_list[0][3]), int)
        self.assertTrue(pokemon_list[3][3] is None)
        self.assertIs(type(pokemon_list[0][4]), int)
        self.assertIs(type(pokemon_list[0][5]), int)
        self.assertIs(type(pokemon_list[0][6]), int)
        self.assertIs(type(pokemon_list[0][7]), int)
        self.assertIs(type(pokemon_list[0][8]), int)
        self.assertIs(type(pokemon_list[0][9]), int)


    def test_get_pokemon_by_attack_range(self):
        x = get_pokemon_by_attack_range(40, 50, self.cur)
        self.assertEqual(len(x), 77)
        self.assertEqual(len(x[0]), 3)
        self.assertEqual(x[0], (0, "bulbasaur", 49))
        self.assertEqual(x[1], (6, "squirtle", 48))
        self.assertEqual(x[-1], (494, "snivy", 45))

        y = get_pokemon_by_attack_range(100, 200, self.cur)
        self.assertEqual(len(y), 102)
        self.assertEqual(len(y[0]), 3)
        self.assertEqual(y[0], (27, "sandslash", 100))
        self.assertEqual(y[1], (33, "nidoking", 102))
        self.assertEqual(y[-1], (499, "emboar", 123))


    def test_get_balanced_pokemon_above_health(self):
        x = get_balanced_pokemon_above_health(50, self.cur)
        self.assertEqual(len(x), 78)
        self.assertEqual(len(x[0]), 5)
        self.assertEqual(x[0], (1, "ivysaur", 80, 80, 60))
        self.assertEqual(x[1], (2, "venusaur", 100, 100, 80))
        self.assertEqual(x[-1], (497, "tepig", 45, 45, 65))

        y = get_balanced_pokemon_above_health(100, self.cur)
        self.assertEqual(len(y), 12)
        self.assertEqual(len(y[0]), 5)
        self.assertEqual(y[0], (111, "rhydon", 45, 45, 105))
        self.assertEqual(y[1], (150, "mew", 100, 100, 100))
        self.assertEqual(y[-1], (493, "victini", 100, 100, 100))


    def test_get_pokemon_HP_above_speed_attack(self):
        x = get_pokemon_HP_above_speed_attack(60, 20, 85, self.cur)
        self.assertEqual(len(x), 8)
        self.assertEqual(len(x[0]), 4)
        self.assertEqual(x[0], ("arbok", 80, 95, 69))
        self.assertEqual(x[1], ("raichu", 110, 90, 55))
        self.assertEqual(x[-1], ("kecleon", 40, 90, 70))

        y = get_pokemon_HP_above_speed_attack(50, 10, 60, self.cur)
        self.assertEqual(len(y), 19)
        self.assertEqual(len(y[0]), 4)
        self.assertEqual(y[0], ("sandshrew", 40, 75, 85))
        self.assertEqual(y[1], ("bellsprout", 40, 75, 35))
        self.assertEqual(y[-1], ("spiritomb", 35, 92, 108))


    def test_get_pokemon_by_type(self):
        x = get_pokemon_by_type("grass", self.cur)
        self.assertEqual(len(x), 58)
        self.assertEqual(len(x[0]), 4)
        self.assertEqual(x[0], (0, "bulbasaur", "grass", "poison"))
        self.assertEqual(x[-1], (496, "serperior", "grass", None))

        y = get_pokemon_by_type("water", self.cur)
        self.assertEqual(len(y), 92)
        self.assertEqual(len(y[0]), 4)
        self.assertEqual(y[0], (6, "squirtle", "water", None))
        self.assertEqual(y[-1], (489, "manaphy", "water", None))


    ### UNCOMMENT TEST CASES BELOW FOR EXTRA CREDIT ###

    # def test_get_fastest_pokemon_of_type(self):
    #     x = get_fastest_pokemon_of_type("fire", self.cur)
    #     self.assertEqual(len(x), 1)
    #     self.assertEqual(len(x[0]), 3)
    #     self.assertEqual(x[0], ("infernape", "fire", 108))

    #     y = get_fastest_pokemon_of_type("water", self.cur)
    #     self.assertEqual(len(y), 2)
    #     self.assertEqual(len(y[0]), 3)
    #     self.assertEqual(y[0], ('floatzel', 'water', 115))
    #     self.assertEqual(y[1], ('starmie', 'water', 115))

    #     z = get_fastest_pokemon_of_type("ice", self.cur)
    #     self.assertEqual(len(z), 1)
    #     self.assertEqual(len(z[0]), 3)
    #     self.assertEqual(z[0], ('weavile', 'dark', 125))
    #     z = get_fastest_pokemon_of_type("dark", self.cur)
    #     self.assertEqual(z[1], ('weavile', 'dark', 125))


def main():
    json_data = read_data_from_file("pokemon.json")
    cur, conn = set_up_database("pokemon.db")
    set_up_types_table(json_data, cur, conn)
    create_pokemon_table(json_data, cur, conn)
    conn.close()
    # FEEL FREE TO USE THIS SPACE TO TEST OUT YOUR FUNCTIONS


if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)