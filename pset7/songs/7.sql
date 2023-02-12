-- Escreva uma consulta SQL que retorne a energia média das músicas de Drake.
SELECT avg(energy) FROM songs
WHERE artist_id = (
    SELECT id FROM artists
    WHERE name = "Drake"
);