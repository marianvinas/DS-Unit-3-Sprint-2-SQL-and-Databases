import os
import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH = "rpg_db.sqlite3"
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# How many total Characters are there?
query1 = '''
SELECT
  COUNT(*)
FROM charactercreator_character'''

result1 = cursor.execute(query1).fetchone()
print(result1)

# How many of each specific subclass?
query2 = '''
SELECT
  name,
  level,
  exp
FROM charactercreator_character
'''

result2 = cursor.execute(query2).fetchone()
print(result2)

# How many total Items?
query3 = '''
SELECT
  COUNT(*)
FROM armory_item'''

result3 = cursor.execute(query3).fetchone()
print(result3)

# How many of the Items are weapons? How many are not?
query4 = '''
SELECT *
FROM charactercreator_character_inventory as cci
JOIN armory_weapon AS aw ON cci.item_id == aw.item_ptr_id 

'''

result4 = cursor.execute(query4).fetchone()
print(result4)

# How many Items does each character have? (Return first 20 rows)
query5 = '''
SELECT *
FROM charactercreator_character_inventory as cci
JOIN armory_item AS ai ON cci.item_id == ai.item_id
'''

result5 = cursor.execute(query5).fetchone()
print(result5)

# How many Weapons does each character have? (Return first 20 rows)
query6 = '''
SELECT *
FROM charactercreator_character_inventory as cci
JOIN armory_weapon AS aw ON cci.item_id == aw.item_ptr_id
'''

result6 = cursor.execute(query6).fetchone()
print(result6)

# How many Weapons does each character have? (Return first 20 rows)
query7 = '''
SELECT AVG(Weapon_Count) as Average_Weapons
FROM (
	SELECT
	  cci.character_id,
	  -- cci.item_id,
	  COUNT(aw.item_ptr_id) as Weapon_Count
	FROM charactercreator_character_inventory as cci
	LEFT JOIN armory_weapon AS aw ON cci.item_id == aw.item_ptr_id
	GROUP BY cci.character_id
)
'''

result7 = cursor.execute(query7).fetchone()
print(result7)

#query = "SELECT * FROM customers;"
query8 = '''
SELECT AVG(Items_Count) as Average_Items
FROM (
	SELECT
	  cci.character_id,
	  COUNT(ai.item_id) as Items_Count
	FROM charactercreator_character_inventory as cci
	LEFT JOIN armory_item AS ai ON cci.item_id == ai.item_id
	GROUP BY cci.character_id
) 

'''

result8 = cursor.execute(query8).fetchone()
print(result8)

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

#result2 = cursor.execute(query).fetchall()
#print("RESULT 2", result2)