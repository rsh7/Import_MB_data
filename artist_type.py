from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT artist_type.id,
                           artist_type.name,
                           artist_type.parent,
                           artist_type.child_order,
                           artist_type.description,
                           artist_type.gid
                      FROM artist_type
                INNER JOIN artist
                        ON artist.type = artist_type.id
                     WHERE artist.id = :MB_artist_data
    """)
    result = connection.execute(query, {"MB_artist_data": MB_artist_data[0]})
    MB_artist_type_data = result.fetchall()
