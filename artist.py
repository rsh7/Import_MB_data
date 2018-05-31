from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT artist.id, artist.gid, artist.name, artist.sort_name,
                artist.begin_date_year, artist.begin_date_month, artist.begin_date_day,
                artist.end_date_year, artist.end_date_month, artist.end_date_day,
                artist.type, artist.area, artist.gender, artist.comment, artist.edits_pending,
                artist.last_updated, artist.ended, artist.begin_area, artist.end_area
                FROM artist INNER JOIN artist_credit 
                ON artist_credit.id = artist.id where artist_credit.id=:MB_artist_credit[0]
    """),{
        "MB_artist_credit_data": MB_artist_data,
    }
    result = connection.execute(query)
    MB_artist_data = result.fetchall()
