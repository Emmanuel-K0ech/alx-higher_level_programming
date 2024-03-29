-- Lists all cities contained in databas 'hbtn_0d_usa'
SELECT cities.id, cities.name AS name, states.name AS name
FROM hbtn_0d_usa.cities
JOIN hbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id ASC;
