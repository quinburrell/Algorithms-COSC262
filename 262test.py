import sys
sys.setrecursionlimit(2000)

class Song:
    """An song to (maybe) put in a playlist. Weight must be an int."""
    def __init__(self, rating, duration_in_minutes):
        self.rating = rating
        self.duration = duration_in_minutes

    def __repr__(self):
        """The representation of a song"""
        return "({}, {})".format(self.rating, self.duration)

def max_total_rating(songs, total_duration, n=None):
    """Return the maximum total rating achievable by taking a subset of the first
       'n' songs to fit within a playlist of the given total_duration.
    """
    known = {}
    
    def mem(total_duration, n=None):
        if total_duration in known:
            return known[total_duration]
        else:
            if n is None:
                n = len(songs)
            
            if n == 0 or total_duration <= 0:
                return 0
            else:
                # Not the base case. First compute the maximum we can achieve without
                # using the nth song.
                max_without_nth_song = mem(total_duration, n - 1)
                
                # Now decide whether to use that result or the result obtained by
                # using the nth song.
                if songs[n - 1].duration > total_duration:
                    answer = max_without_nth_song
                else:
                    max_with_nth_song = songs[n-1].rating + mem(total_duration - songs[n-1].duration)
                    known[total_duration] = max(max_without_nth_song, max_with_nth_song)
    mem(total_duration)
    return known[total_duration]
