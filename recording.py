from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:                   
    recording_query = text("""SELECT recording.id, recording.gid, recording.name, recording.artist_credit,
                          recording.length, recording.comment, recording.edits_pending, recording.last_updated,
                          recording.video
                     FROM recording
                    WHERE recording.gid = :recording_gid""")
    result = connection.execute(recording_query, {"recording_gid": recording_gid[0]})
    MB_recording_data = result.fetchone()
