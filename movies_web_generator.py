from movie_storage import *

def get_page_title():
    """Adds a title to the Web page"""
    output1 = 'Lais Movie App'
    return output1

def serialize_movie(movies_storage):
    """ Loops through the movie info and creates outputs for the cards in the HTML page """
    output2 = ''

    for movie, details in movies_storage.items():
        output2 += '<li>'
        output2 += '<div class="movie">'
        output2 += f"<div class=\"movie-title\">{movie}</div>"
        output2 += f"<div class=\"movie-year\">{details.get('year', 'Year not available')}</div>"
        output2 += f"<div class=\"movie-rating\">Rating: {details.get('rating', 'Rating not available')}</div>"
        if 'poster_url' in details:
            output2 += f"<img class=\"movie-poster\" src=\"{details['poster_url']}\" />"
        else:
            output2 += "<p>No poster available</p>"
        output2 += '</div>'
        output2 += '</li>'

    return output2


def generate_website(movies):
    """Generate a website with movie information"""
    with open('index_template.html', 'r') as file:
        html_content = file.read()

        output1 = get_page_title()
        output2 = serialize_movie(movies)

        updated_html_title = html_content.replace('__TEMPLATE_TITLE__', output1)
        updated_html_moviegrid = updated_html_title.replace('__TEMPLATE_MOVIE_GRID__', output2)

    with open('index.html', 'w') as file:
        file.write(updated_html_moviegrid)

    print("Website was generated successfully.")
