#! /usr/bin/env python3

"""Create a media website"""

import media
import fresh_tomatoes


def main():
    # Create
    grand_budapest_hotel = media.Movie(
        "The Grand Budapest Hotel",
        "The adventures of Gustave H, a legendary concierge at The \
        Grand Budapest Hotel",
        "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
        "https://youtu.be/1Fg5iWmQjwk")

    life_aquatic = media.Movie(
        "The Life Aquatic with Steve Zissou",
        "Zissou, an eccentric oceanographer who sets out to exact \
        revenge on the jaguar shark that ate his partner Esteban",
        "https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg",
        "https://youtu.be/sThuSCJItmQ")

    darjeeling_limited = media.Movie(
        "The Darjeeling Limited",
        "An emotional comedy about three brothers re-forging family \
        bonds.",
        "https://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg",
        "https://youtu.be/aO1bYukdvLI")

    moonrise_kingdom = media.Movie(
        "Moonrise Kingdom",
        "An eccentric pubescent love story.",
        "https://upload.wikimedia.org/wikipedia/en/4/4f/Moonrise_Kingdom_FilmPoster.jpeg",
        "https://youtu.be/G2EWlnod4V8")

    fantastic_fox = media.Movie(
        "Fantastic Mr. Fox",
        "A fox who steals food each night from three mean and wealthy \
        farmers.",
        "https://upload.wikimedia.org/wikipedia/en/a/af/Fantastic_mr_fox.jpg",
        "https://youtu.be/BhyOvvKjdnY")

    royal_tenenbaums = media.Movie(
        "The Royal Tenenbaums",
        "The lives of three gifted siblings who experience great \
        success in youth, and even greater disappointment and failure \
        after their eccentric father leaves them in their adolescent \
        years.",
        "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",
        "https://youtu.be/FeBa2s4ldU4")

    #
    movies = [grand_budapest_hotel, life_aquatic, darjeeling_limited,
              moonrise_kingdom, fantastic_fox, royal_tenenbaums]
    #
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()

