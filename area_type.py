from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT area_type.id,
                           area_type.name,
                           area_type.parent,
                           area_type.child_order,
                           area_type.description,
                           area_type.gid
                      FROM area_type
                INNER JOIN area
                        ON area.type = area_type.id
                     WHERE area.id = :MB_area_data
    """)
    result = connection.execute(query, {"MB_area_data": MB_area_data[0]})
    MB_area_type_data = result.fetchall()
