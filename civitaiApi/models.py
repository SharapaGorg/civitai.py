from enum import Enum

class Creator:
    def __init__(self, link : str, username : str, model_count : int):
        self.link = link
        self.username = username
        
        self.model_count = model_count
        if model_count is None:
            self.model_count = 0

class Model:
    def __init__(
        self, 
        name : str, 
        description : str,
        type : Enum,
        nsfw : bool):

        self.name = name
        self.description = description
        self.type = type
        self.nsfw = nsfw