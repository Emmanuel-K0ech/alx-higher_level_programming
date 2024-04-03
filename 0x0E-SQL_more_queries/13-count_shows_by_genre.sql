-- Lists all genres from hbtn_0d)tvshows database with the number of shows
-- linked to each other
-- Does not display genres without linked shows
-- Records are ordered by desceding order of number of shows linked

SELECT x.`name` AS `genre`,
	COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS x
	INNER JOIN `tv_show_genres` AS t
	ON x.`id` = t.`genre_id`
GROUP BY x.`name`
ORDER BY `number_of_shows` DESC;
