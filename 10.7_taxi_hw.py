import os
import sqlite3

if os.path.exists('taxis.db'):
    os.remove('taxis.db')

# Connect to the SQLite database
conn = sqlite3.connect('taxis.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Use executescript to run multiple SQL statements at once
cursor.executescript('''
CREATE TABLE taxis (
    id INTEGER PRIMARY KEY,
    driver_name TEXT NOT NULL,
    car_type TEXT NOT NULL
);
CREATE TABLE passengers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    destination TEXT,
    taxi_id INTEGER,
    FOREIGN KEY(taxi_id) REFERENCES taxis(id)
);
''')

cursor.executescript('''
INSERT INTO taxis (id, driver_name, car_type) VALUES
(1, 'Moshe Levi', 'Van'),
(2, 'Rina Cohen', 'Sedan'),
(3, 'David Azulay', 'Minibus'),
(4, 'Maya Bar', 'Electric'),
(5, 'Yossi Peretz', 'SUV');
INSERT INTO passengers (id, name, destination, taxi_id) VALUES
(1, 'Tamar', 'Jerusalem', 1),
(2, 'Eitan', 'Haifa', 2),
(3, 'Noa', 'Tel Aviv', NULL),
(4, 'Lior', 'Eilat', 1),
(5, 'Dana', 'Beer Sheva', NULL),
(6, 'Gil', 'Ashdod', 3),
(7, 'Moran', 'Netanya', NULL);
''')

# --1 INNER JOIN | הצג את כל המוניות והנוסעים שלהן --
print("--- 1 INNER JOIN: הצג את כל המוניות והנוסעים שלהן ---")
cursor.execute('''
SELECT t.id AS taxi_id, t.driver_name, t.car_type, 
       p.id AS passenger_id, p.name AS passenger_name, p.destination
FROM taxis t
INNER JOIN passengers p ON t.id = p.taxi_id;
''')
for row in cursor.fetchall():
    print(dict(row))

# --2 INNER JOIN | הצג את כל הנוסעים שהשיגו מונית יחד עם פרטי המונית --
print("\n--- 2 INNER JOIN: הצג את כל הנוסעים שהשיגו מונית יחד עם פרטי המונית ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, 
       t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
INNER JOIN taxis t ON p.taxi_id = t.id;
''')
for row in cursor.fetchall():
    print(dict(row))

# --3 LEFT JOIN | הצג את כל הנוסעים כולל כאלה שמצאו מונית וכאלה שלא --
print("\n--- 3 LEFT JOIN: הצג את כל הנוסעים כולל כאלה שמצאו מונית וכאלה שלא ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, 
       t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id;
''')
for row in cursor.fetchall():
    print(dict(row))

# --4 LEFT JOIN | הצג רק את הנוסעים שאין להם taxi_id תואם --
print("\n--- 4 LEFT JOIN: הצג רק את הנוסעים שאין להם taxi_id תואם ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id
WHERE p.taxi_id IS NULL;
''')
for row in cursor.fetchall():
    print(dict(row))

# --5 FULL OUTER JOIN | הצג את כל הנוסעים וכל המוניות — גם אם אין התאמה ביניהם --
print("\n--- 5 FULL OUTER JOIN: הצג את כל הנוסעים וכל המוניות — גם אם אין התאמה ביניהם ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, 
       t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id

UNION

SELECT NULL AS passenger_id, NULL AS passenger_name, NULL AS destination,
       t.id AS taxi_id, t.driver_name, t.car_type
FROM taxis t
WHERE t.id NOT IN (SELECT taxi_id FROM passengers WHERE taxi_id IS NOT NULL);
''')
for row in cursor.fetchall():
    print(dict(row))

# --6 CROSS JOIN | הצג את כל הצירופים האפשריים בין נוסעים למוניות --
print("\n--- 6 CROSS JOIN: הצג את כל הצירופים האפשריים בין נוסעים למוניות ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, 
       t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
CROSS JOIN taxis t;
''')
for row in cursor.fetchall():
    print(dict(row))

# --7 LEFT JOIN | הצג את כל הנוסעים כולל כאלה שמצאו מונית וכאלה שלא --
print("\n--- 7 LEFT JOIN: הצג את כל הנוסעים כולל כאלה שמצאו מונית וכאלה שלא ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, 
       t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id;
''')
for row in cursor.fetchall():
    print(dict(row))

# --8 LEFT JOIN | הצג רק את הנוסעים שאין להם taxi_id תואם --
print("\n--- 8 LEFT JOIN: הצג רק את הנוסעים שאין להם taxi_id תואם ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id
WHERE p.taxi_id IS NULL;
''')
for row in cursor.fetchall():
    print(dict(row))

# --9 FULL OUTER JOIN | הצג את כל הנוסעים וכל המוניות — גם אם אין התאמה ביניהם --
print("\n--- 9 FULL OUTER JOIN: הצג את כל הנוסעים וכל המוניות — גם אם אין התאמה ביניהם ---")
cursor.execute('''
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, 
       t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id

UNION

SELECT NULL AS passenger_id, NULL AS passenger_name, NULL AS destination,
       t.id AS taxi_id, t.driver_name, t.car_type
FROM taxis t
WHERE NOT EXISTS (
    SELECT 1 FROM passengers p WHERE p.taxi_id = t.id
);
''')
for row in cursor.fetchall():
    print(dict(row))

# --10 CROSS JOIN | הצג את כל הצירופים האפשריים בין נוסעים למוניות --
print("\n--- 10 CROSS JOIN: הצג את כל הצירופים האפשריים בין נוסעים למוניות ---")
cursor.execute('''
SELECT 
    p.id AS passenger_id,
    p.name AS passenger_name,
    p.destination,
    t.id AS taxi_id,
    t.driver_name,
    t.car_type
FROM 
    passengers p, taxis t
ORDER BY 
    p.id, t.id;
''')
for row in cursor.fetchall():
    print(dict(row))

# Commit the changes and close the connection
conn.commit()
conn.close()
