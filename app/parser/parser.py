from time import sleep

from parser.frames.basic import BasicArtistFrame
from parser.frames.search import SearchFrame
from parser.frames.info import ArtistInfoFrame
from parser.types import ArtistDict


class YandexMusicParser(SearchFrame, BasicArtistFrame, ArtistInfoFrame):
    def start(self, artist_name: str) -> ArtistDict:
        data = {}
        artist_id = self.parse_search_frame(artist_name)
        data.update(self.parse_basic_artist_frame(artist_id))
        data.update(self.parse_artist_info(artist_id))
        self.logger.info(f"Artist: {data}")
        return data
