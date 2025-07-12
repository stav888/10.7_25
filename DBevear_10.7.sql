
--5 CROSS JOIN | הצג את כל הצירופים האפשריים בין נוסעים למוניות --
SELECT p.id AS passenger_id, p.name AS passenger_name, p.destination, t.id AS taxi_id, t.driver_name, t.car_type
FROM passengers p
CROSS JOIN taxis t;
