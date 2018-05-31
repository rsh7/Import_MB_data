from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT gender.id,
                           gender.name,
                           gender.parent,
                           gender.child_order,
                           gender.description,
                           gender.gid
                      FROM gender
                INNER JOIN artist
                        ON artist.gender = gender.id
                     WHERE artist.id = :MB_artist_data
    """)
    result = connection.execute(query, {"MB_artist_data": MB_artist_data[0]})
    MB_gender_data = result.fetchall()
