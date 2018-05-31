from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT release_gid_redirect.gid,
                           release_gid_redirect.new_id,
                           release_gid_redirect.created,
                      FROM release_gid_redirect
                INNER JOIN release
                        ON release.id = release_gid_redirect.new_id
                     WHERE release.id = :MB_release_data
    """)
    result = connection.execute(query, {"MB_artist_data": MB_artist_data[0][0]})
    MB_release_gid_redirect_data = result.fetchall()
