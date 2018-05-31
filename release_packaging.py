from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT release_packaging.id,
                           release_packaging.name,
                           release_packaging.parent,
                           release_packaging.child_order,
                           release_packaging.description,
                           release_packaging.gid
                      FROM release_packaging
                INNER JOIN release
                        ON release.packaging = release_packaging.id
                     WHERE release.packaging = :MB_release_data
    """)
    result = connection.execute(query, {"MB_artist_data": MB_artist_data[0][6]})
    MB_release_packaging_data = result.fetchall()
