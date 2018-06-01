from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    area_query = text("""
        SELECT area.id,
                area.gid,
                area.name,
                area.type,
                area.edits_pending,
                area.last_updated,
                area.begin_date_year,
                area.begin_date_month,
                area.begin_date_day,
                area.end_date_year,
                area.end_date_month,
                area.end_date_day,
                area.ended, 
                area.comment
          FROM area
    INNER JOIN artist
            ON area.id = artist.area
    INNER JOIN artist_credit
            ON artist.id = artist_credit.id
         WHERE artist_credit.id = :MB_artist_data[0]
    """)
    result = connection.execute(area_query, {"MB_artist_data": MB_artist_data})
    MB_area_data = result.fetchall()
