-- Lists all genres of the show Dexter.
-- The tv_shows table conatins one record where title=Dexter
-- Id can be different
-- Results sorted in ASC order by the genre name
-- You can only use SELECT statment

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
