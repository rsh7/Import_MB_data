from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT release_status.id,
                           release_status.name,
                           release_status.parent,
                           release_status.child_order,
                           release_status.description,
                           release_status.gid
                      FROM release_status
                INNER JOIN release
                        ON release.status = release_status.id
                     WHERE release.status = :MB_release_data
    """)
    result = connection.execute(query, {"MB_artist_data": MB_artist_data[0][5]})
    MB_release_status_data = result.fetchall()
