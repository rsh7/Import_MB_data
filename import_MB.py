from brainzutils import musicbrainz_db
musicbrainz_db.init_db_engine("postgresql://musicbrainz:musicbrainz@musicbrainz_db:5432/musicbrainz_db")  # It is already initialized while server is up i guess
from sqlalchemy import text
import db

with db.engine.begin() as conn:
	lowlevel_query = text("""SELECT gid from lowlevel""")
	gids_in_AB = conn.execute(lowlevel_query)
	for recording_gid in gids_in_AB.fetchall():
		MB_artist_credit_data = 0
		MB_recording_data = 0
		#SIMILARLY FOR OTHER TABLES

		# FROM MUSICBRAINZ
		with musicbrainz_db.engine.begin() as connection:  # Make it a function
			artist_credit_query = text("""SELECT * from artist_credit where gid= recording_gid""") # Correct the SYNTAX HERE
			result = connection.execute(artist_credit_query)
			MB_artist_credit_data = result.fetchone()

			recording_query = text("""SELECT * from recording where gid= recording_gid""") # Correct the SYNTAX HERE
			result = connection.execute(recording_query)
			MB_recording_data = result.fetchone()

			# TODO: (Most Important [Should be done by 30, May])
			# * SIMILARY FOR EVERY OTHER TABLE
			# * NEED TO FIGURE OUT HOW TO SELECT THE DATA,
			# * BECAUSE EVERY TABLE DOESN'T HAVE A GID COLUMN
		# TO ACOUSTICBRAINZ
		with db.engine.begin() as connection:
			artist_credit_query = text("""Insert into musicbrainz.artist_credit(id, name, artist_count, ref_count, created)
					Values (:id, :name, :artist_count, :ref_count, :created)""")
			result = connection.execute(artist_credit_query, {"id" : MB_artist_credit_data[0],
															  "name" : MB_artist_credit_data[1],
															  "artist_count" : MB_artist_credit_data[2],
															  "ref_count" : MB_artist_credit_data[3],
															  "created" : MB_artist_credit_data[4]
															  }
			)
			# SIMILARLY FOR RECORDING AND OTHER TABLES IN MUSICBRAINZ SCHEMA IN AB DATABASE
			# PROBABLY IT'LL ALSO BE A NEW FUNCTION
