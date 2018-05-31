from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT recording_gid_redirect.gid,
                           recording_gid_redirect.new_id,
                           recording_gid_redirect.created
                      FROM recording_gid_redirect
                INNER JOIN recording
                        ON recording.id = recording_gid_redirect.new_id
                     WHERE recording.gid = :recording_gid   # The one from lowlevel
    """)
    result = connection.execute(query, {"recording_gid": recording_gid})
    MB_recording_gid_redirect_data = result.fetchall()
