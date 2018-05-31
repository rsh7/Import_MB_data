from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT release_group.id, release_group.gid, release_group.name,
                release_group.artist_credit, release_group.type, release_group.comment,
                release_group.edits_pending, release_group.last_updated
                FROM release_group INNER JOIN artist_credit 
                ON artist_credit.id = release_group.artist_credit where artist_credit.id=:MB_artist_credit_data
    """)
    result = connection.execute(query, {"MB_artist_credit_data": MB_artist_data[0]})
    print(result.fetchall())
