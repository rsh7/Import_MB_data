from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT medium_format.id,
                           medium_format.name,
                           medium_format.parent,
                           medium_format.child_order,
                           medium_format.year,
                           medium_format.has_discids,
                           medium_format.description,
                           medium_format.gid
                      FROM medium_format
                INNER JOIN medium
                        ON medium_format.id = medium.format
                     WHERE medium.id = :MB_medium_data
    """)
    result = connection.execute(query, {"MB_release_data": MB_release_data[0]})
    MB_medium_format_data = result.fetchall()
