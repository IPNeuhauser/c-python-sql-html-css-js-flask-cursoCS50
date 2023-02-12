SELECT DISTINCT name FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
WHERE year = 2004
ORDER BY birth ASC;