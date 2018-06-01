from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:  # Make it a function
    # ARTIST CREDIT
    artist_credit_query = text("""SELECT artist_credit.id, artist_credit.name, artist_credit.artist_count,
                                    artist_credit.ref_count, artist_credit.created
                                    FROM artist_credit
                                    INNER JOIN recording
                                    ON artist_credit.id = recording.artist_credit
                                    WHERE recording.gid= :recording_gid""") # Correct the SYNTAX HERE
    result = connection.execute(artist_credit_query, {"recording_gid" : recording_gid[0]})
    MB_artist_credit_data = result.fetchone()
