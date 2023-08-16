-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` as s
       LEFT JOIN `tv_show_genres` as g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
