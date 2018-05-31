from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT release.id,
                           release.gid,
                           release.name,
                           release.artist_credit,
                           release.release_group,
                           release.status,
                           release.packaging,
                           release.language,
                           release.script,
                           release.barcode,
                           release.comment,
                           release.edits_pending,
                           release.quality,
                           release.last_updated
                      FROM release
                INNER JOIN artist_credit
                        ON artist_credit.id = release.artist_credit
                     WHERE artist_credit.id = :MB_artist_data
    """)
    result = connection.execute(query, {"MB_artist_data": MB_artist_data[0]})
    MB_release_data = result.fetchall()
