from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT release_group_gid_redirect.gid,
                           release_group_gid_redirect.new_id,
                           release_group_gid_redirect.created,
                      FROM release_group_gid_redirect
                INNER JOIN release_group
                        ON release_group.id = release_group_gid_redirect.new_id
                     WHERE release_group.id = :MB_release_group_data
    """)
    result = connection.execute(query, {"MB_release_group_data": MB_release_group_data[0][0]}) # check whether the result is a set or list of sets.
    MB_release_group_gid_redirect_data = result.fetchall()
