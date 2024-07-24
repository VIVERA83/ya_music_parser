# Яндекс музыка "parser"

Сервис вынимает из платформы __Яндекс музыка__ основные данные по исполнителю и результат сохраняет в cvs файл

### Запуск

1. клонируем репозиторий
2. исполняемый файл находится `app/main.py`
3. устанавливаем зависимости `pip install -r requirements.txt`
4. переходим в папку app `cd app`
5. запуск `python main.py`

Появится текстовое сообщение, предлагающие ввести имя исполнителя,
вводим и через несколько мгновений у вас появится файлик на подобия `имя исполнителя.csv`
в файлик будет внесена следующая информация:

```json
{
  "name": "Король и Шут",
  "listeners": "5 511 883",
  "likes": "106 898",
  "last_release": "12 апреля 2024",
  "vk": "http://vk.com/korol_i_shut_ru",
  "twitter": "https://twitter.com/korol_i_shut",
  "youtube": "http://www.youtube.com/thekorolishut",
  "website_1": "http://www.korol-i-shut.ru/",
  "website_2": "https://band.link/scanner?search=41052&type=artist_id&service=yandex_music"
}
```




