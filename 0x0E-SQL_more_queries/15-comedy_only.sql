-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.`title`
  FROM `tv_shows` as t
       INNER JOIN `tv_show_genres` as s
       ON t.`id` = s.`show_id`

       INNER JOIN `tv_genres` as g
       ON g.`id` = s.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY t.`title`;
