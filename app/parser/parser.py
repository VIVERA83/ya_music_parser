from time import sleep

from parser.frames.basic import BasicArtistFrame
from parser.frames.search import SearchFrame
from parser.frames.info import ArtistInfoFrame


class YandexMusicParser(SearchFrame, BasicArtistFrame, ArtistInfoFrame):
    def start(self, artist_name: str):
        data = []
        artist_id = self.parse_search_frame(artist_name)
        sleep(0.5)
        data.append(self.parse_basic_artist_frame(artist_id))
        sleep(0.5)
        data.extend(self.parse_artist_info(artist_id))
        self.logger.info(f"Artist: {data}")
