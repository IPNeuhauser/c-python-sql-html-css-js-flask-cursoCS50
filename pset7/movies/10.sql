SELECT DISTINCT name FROM movies
JOIN directors ON directors.movie_id = movies.id
JOIN people ON people.id = directors.person_id
JOIN ratings ON ratings.movie_id = movies.id
WHERE rating >= 9.0;