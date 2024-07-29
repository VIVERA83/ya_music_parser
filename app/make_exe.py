from cx_Freeze import setup, Executable

executables = [Executable("main.py", target_name="ya_music_parser.exe")]

setup(
    name="Яндекс музыка 'parser'",
    version="0.0.1",
    description="Поиск информации о исполнителе на одноименном сервисе,"
    " найденная информация сохраняется в файле csv",
    executables=executables,
)
