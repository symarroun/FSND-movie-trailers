import webbrowser

# The Movie() class allow the creation of intances of a movie with four
# inputs (title, storyline, image, and youtube) and opens youtube in
# browswer:


class Movie():

        # This method initiates the class inputs; which are the title,
        # storyline, poster, and youtube URL of the movie
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This method takes in the YouTube URL of a movie and opens it in the
    # browswer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
