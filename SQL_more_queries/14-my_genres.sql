-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows
-- Uses the tv_shows table to filter by title and joins with tv_genres
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
