SELECT movie_id, person_id, COUNT(*)
FROM stars
GROUP BY movie_id, person_id
HAVING COUNT(*) > 1;