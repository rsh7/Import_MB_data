from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    artist_query = text("""
                        SELECT artist.id, artist.gid, artist.name, artist.sort_name, artist.begin_date_year,
                               artist.begin_date_month, artist.begin_date_day, artist.end_date_year, artist.end_date_month,
                               artist.end_date_day, artist.type, artist.area, artist.gender, artist.comment, artist.edits_pending,
                               artist.last_updated, artist.ended, artist.begin_area, artist.end_area
                          FROM artist
                    INNER JOIN artist_credit 
                            ON artist_credit.id = artist.id
                    INNER JOIN recording
                            ON artist_credit.id = recording.artist_credit
                    WHERE recording.gid = :recording_gid""")
    result = connection.execute(artist_query, {"recording_gid": recording_gid})
    MB_artist_data = result.fetchone()
