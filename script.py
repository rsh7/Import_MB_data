from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT script.id,
                           script.iso_code,
                           script.iso_number,
                           script.name,
                           script.frequency
                      FROM script
                INNER JOIN release
                        ON release.script = script.id
                     WHERE release.id = :MB_release_data
    """)
    result = connection.execute(query, {"MB_release_data": MB_release_data[0]})
    MB_script_data = result.fetchall()
