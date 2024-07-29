from icecream import ic

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

    def search_params(self, search_data: dict) -> list[ArtistDict]:
        data = []

        for page in range(2):
            try:
                artists = self.search_by_params(
                    search_data["genre"], "artist", page=page
                )
            except Exception as e:
                self.logger.error(f"Ошибка при парсинге страницы {page}")
                break
            ic(artists)
            for artist_id in artists:
                artist_data = self.parse_artist_info(artist_id)
                if (int(artist_data["listeners"].replace(" ", "")) >= search_data["listeners_from"]) and (
                    int(artist_data["listeners"].replace(" ", "")) <= search_data["listeners_to"]
                ):
                    artist_data.update(self.parse_basic_artist_frame(artist_id))
                    data.append(artist_data)
                    self.logger.info(f"Artist: {artist_data}")
        return data
