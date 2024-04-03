-- lists all shows conatined in hbtn_0d_tvshows without genre linked.
-- You can only use one SELECT statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_show.title, tv_show_genres.genre_id;
