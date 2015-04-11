__author__ = 'Jake'

from pyechonest import config
from pyechonest import song

config.ECHO_NEST_API_KEY = "DLBFUV54VPZIDBJO7"

rkp_results = song.search(mood="happy, excited", artist_min_familiarity=.75)
resultant_song = rkp_results[0]
print resultant_song.artist_location
print 'tempo:',resultant_song.audio_summary['tempo'],'duration:',resultant_song.audio_summary['duration']


