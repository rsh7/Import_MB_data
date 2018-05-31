from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT release_group_primary_type.id, release_group_primary_type.name,
                           release_group_primary_type.parent, release_group_primary_type.child_order,
                           release_group_primary_type.description, release_group_primary_type.gid
                    FROM release_group_primary_type INNER JOIN release_group 
                    ON release_group_primary_type.id = release_group.type where release_group.id = :MB_release_group_data
    """)
    result = connection.execute(query, {"MB_release_group_data": MB_release_group_data[0]})
    MB_release_group_primary_type_data = result.fetchall()
