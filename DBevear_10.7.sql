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



-- test (left join)
SELECT * FROM taxis t
LEFT JOIN passengers p ON t.id = p.taxi_id;
-- -- --


--3 - Join
--1 INNER JOIN | הצג את כל הנוסעים שהשיגו מונית יחד עם פרטי המונית --
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
INNER JOIN taxis t ON p.taxi_id = t.id;

--2 LEFT JOIN |הצג את כל הנוסעים כולל כאלה שמצאו מונית וכאלה שלא --
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id;

--3 LEFT JOIN | הצג רק את הנוסעים שלא מצאו מונית --
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id
WHERE p.taxi_id IS NULL;

--4 Combine LEFT JOIN and RIGHT JOIN to simulate FULL OUTER JOIN | הצג את כל הנוסעים וכל המוניות — נוסעים בלי מונית + נוסעים עם מונית + מונית בלי נוסעים --
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id

UNION

SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
RIGHT JOIN taxis t ON p.taxi_id = t.id
WHERE p.taxi_id IS NULL;

--5 CROSS JOIN | הצג את כל הצירופים האפשריים בין נוסעים למוניות --
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
CROSS JOIN taxis t;
