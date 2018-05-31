from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT artist_credit_name.artist_credit,
                           artist_credit_name.position,
                           artist_credit_name.recording,
                           artist_credit_name.artist,
                           artist_credit_name.name,
                           artist_credit_name.join_phrase
                      FROM artist_credit_name
                INNER JOIN artist_credit
                        ON artist_credit_name.artist_credit = artist_credit.id
                     WHERE artist_credit.id = :MB_artist_data
    """)
    result = connection.execute(query, {"MB_artist_data": MB_artist_data[0]})
    MB_artist_credit_name_data = result.fetchall()
