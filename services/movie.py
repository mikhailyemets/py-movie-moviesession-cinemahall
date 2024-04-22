from django.db.models import Q, QuerySet
from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids is None and actors_ids is None:
        return queryset

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            Q(genres__id__in=genres_ids) & Q(actors__id__in=actors_ids)
        )
    if genres_ids and actors_ids is None:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )
    if actors_ids and genres_ids is None:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
