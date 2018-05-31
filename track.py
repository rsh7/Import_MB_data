from brainzutils import musicbrainz_db
from sqlalchemy import text

with musicbrainz_db.engine.begin() as connection:
    query = text("""SELECT track.id,
                           track.gid,
                           track.recording,
                           track.medium,
                           track.position,
                           track.number,
                           track.name,
                           track.artist_credit,
                           track.length,
                           track.edits_pending,
                           track.last_updated,
                           track.is_data_track
                      FROM track
                INNER JOIN recording
                        ON track.recording = recording.id
                     WHERE recording.gid = :recording_gid   # The one from lowlevel
    """)
    result = connection.execute(query, {"recording_gid": recording_gid})
    MB_track_data = result.fetchall()
