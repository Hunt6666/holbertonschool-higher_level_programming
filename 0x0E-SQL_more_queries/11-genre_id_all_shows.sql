-- lists all shows contained in the database
SELECT x.title, y.genre_id FROM tv_shows x LEFT JOIN tv_show_genres y ON
x.id = y.show_id ORDER BY x.title ASC, y.genre_id ASC
