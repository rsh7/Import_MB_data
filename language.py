from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT language.id,
                           language.iso_code_2t,
                           language.iso_code_2b,
                           language.iso_code_1,
                           language.name,
                           language.frequency,
                           language.iso_code_3
                      FROM language
                INNER JOIN release
                        ON release.language = language.id
                     WHERE release.id = :MB_release_data
    """)
    result = connection.execute(query, {"MB_release_data": MB_release_data[0]})
    MB_language_data = result.fetchall()
