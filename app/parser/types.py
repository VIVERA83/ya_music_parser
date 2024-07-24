from typing import TypedDict, NotRequired


class ArtistDict(TypedDict):
    name: NotRequired[str]
    listeners: NotRequired[str]
    likes: NotRequired[str]
    last_release: NotRequired[str]
    vk: NotRequired[str]
    twitter: NotRequired[str]
    youtube: NotRequired[str]
    website_1: NotRequired[str]
    website_2: NotRequired[str]
