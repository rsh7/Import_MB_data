from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT medium.id,
                           medium.release,
                           medium.position,
                           medium.format,
                           medium.name,
                           medium.edits_pending,
                           medium.last_updated,
                           medium.track_count
                      FROM medium
                INNER JOIN release
                        ON release.id = medium.release
                     WHERE release.id = :MB_release_data
    """)
    result = connection.execute(query, {"MB_release_data": MB_release_data[0]})
    MB_medium_data = result.fetchall()
