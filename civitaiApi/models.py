from enum import Enum


class Creator:
    def __init__(
        self, 
        link: str = None, 
        username: str = None, 
        model_count: int = None,
        image :str = None
        ):
        self.link = link
        self.username = username
        self.image = image

        self.model_count = model_count
        if model_count is None:
            self.model_count = 0


class Stats:
    def __init__(self, downloads, likes, comments, reviews, rating):
        self.downloads = downloads
        self.likes = likes
        self.comments = comments
        self.reviews = reviews
        self.rating = rating


class Model:
    def __init__(
        self,
        name: str,
        description: str,
        type: str,
        nsfw: bool,
        stats: dict,
        creator: dict
    ):

        self.name = name
        self.description = description
        self.type = type
        self.nsfw = nsfw

        self.creator = Creator(username=creator['username'])

        self.stats = Stats(
            stats['downloadCount'],
            stats['favoriteCount'],
            stats['commentCount'],
            stats['ratingCount'],
            stats['rating']
        )
