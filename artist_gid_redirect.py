from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT artist_gid_redirect.gid,
                           artist_gid_redirect.new_id,
                           artist_gid_redirect.created
                      FROM artist_gid_redirect
                INNER JOIN artist
                        ON artist.id = artist_gid_redirect.new_id
                     WHERE artist.id = :MB_artist_id
    """)
    result = connection.execute(query, {"MB_artist_id": MB_artist_data[0]})
    MB_artist_gid_redirect_data = result.fetchall()
