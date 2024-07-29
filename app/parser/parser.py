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
        # открываем результат поиска по жанру
        self.move_to_page_by_params(search_data["genre"], "artist", page=0)
        # кликаем все исполнители
        count_artists = self._click_link_all_artists()
        # обновляем страничку, что бы был доступ ко всем исполнителям на страничке обычно их 48
        self.driver.refresh()
        page = 0
        while count_artists > 0:
            for artist_id in self._get_artists_articles():
                artist_data = self.parse_artist_info(artist_id)
                self.logger.info(
                    f"осталось просмотреть {count_artists}, текущий артист: {artist_data['name']}"
                )

                if (
                    int(artist_data["listeners"].replace(" ", "") or 0)
                    >= search_data["listeners_from"]
                ):
                    artist_data.update(self.parse_basic_artist_frame(artist_id))
                    data.append(artist_data)
                    self.logger.info(f"добавлен артист: {artist_data}")

                count_artists -= 1

            self.move_to_page_by_params(search_data["genre"], "artist", page=page)

        page += 1
        return data
