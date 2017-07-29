import os
# Функция возвращает список найденных файлов
def SearchFiles(dirr: str, mask = '', ListFiles = 0):                                 # Параметр dirr -- каталог поиска, параметр mask (не обязательный) -- маска поиска
    """
    SearchFiles(dirr: str, mask = '', ListFiles = 0) -- default setting
    """

    #dirr = "i:\\PROGRAMM\\PHYTHON\\test"
    #mask = ''
    dir_root = []                                                          # создаем список Корневого каталога
    files_in_dir = []                                                      # создаем список Файлов в каталогах
    SearchRezult = []
    SearchRezultM = []
    SearchRezultMF = []
    tree = os.walk(dirr)                                                   # функция walk возвращает список, в котором указывается 1) путь корневого каталока;  2)список вложенных папок (кортеж); 3) список файлов в папках (кортеж)
    for d, dirs, files in tree:
        dir_root.append(d)                                                 # Заполняем список каталогов
        files_in_dir.append(files)                                         # Заполяем список файлов в каталогах

    for dd in range(0, len(dir_root)):                                     # Перебираем все элементы списка коневого каталога
        list_files = files_in_dir[dd]                                      # Заполяем временный списко list_files
        for j in range(0, len(list_files)):                                # Пробегам каждый элементы временного списка
            x = os.path.join(dir_root[int(dd)], list_files[int(j)])        # Соединяем пути, полученные из списков dir_root и list_files
            SearchRezult.append(x)                                         # Заполняем список полным путем


    if not mask and not ListFiles:                                         # не указана маска и флаг вывода только имен файлов
        return SearchRezult                                                # Если пользователь не указал маску файлов для поиска, то выводится весь список файлов

    elif mask and not ListFiles:                                           # указана маска и не указан флаг вывода только имен файлов
        for i in SearchRezult:
            if mask in i:
                SearchRezultM.append(i)
        return SearchRezultM                                               # Если пользователь указал маску файлов для поиска, то выводится список файлов по маске

    elif not mask and ListFiles:                                           # не указана маска, но указан флаг вывода только имен файлов
        for k in range(0, len(files_in_dir)):
            list_files = files_in_dir[k]
            for j in range(0, len(list_files)):
                x = list_files[int(j)]
                SearchRezultMF.append(x)
        return SearchRezultMF


    elif mask and ListFiles:                                               # указана маска и флаг вывода только имен файлов
        for k in range(0, len(files_in_dir)):
            list_files = files_in_dir[k]
            for j in range(0, len(list_files)):
                x = list_files[int(j)]
                SearchRezultM.append(x)
        for i in SearchRezultM:
            if mask in i:
                SearchRezultMF.append(i)
        return SearchRezultMF                                              # Если пользователь указал флаг вывода только имени файла, то выводится список файлов без указания пути

# работа с SQLite
import sqlite3
def OpenDB(nameDB: str):
    """ nameDB -- имя создаваемой базы"""

    con = sqlite3.connect(nameDB)    # открываем базу
    cur = con.cursor()  # создаем курсов
    sql = """                              
    CREATE TABLE film (
        id_film INTEGER PRIMARY KEY AUTOINCREMENT,
        name_or TEXT,
        name_ru TEXT,
        director TEXT,
        actors TEXT 
        );
        """
    # обрабатываем исключение
    # -----------------------
    try:
        # cur.executescript(sql)              # Выполняем SQL-запрос, несколько за один раз
        cur.execute(sql)                    # Выполняем ОДИН SQL-запрос
    except sqlite3.DatabaseError as err:
        print("Ошибка:", err)
    else:
        print("База создана")
        # con.commit()                      # Завершаем транзакцию, такие как (INSERT, REPLACE, UPDATE, DELETE)
    # -----------------------
    cur.close()                             # Закрываем объект-курсор
    con.close()                             # Закрываем соединение
    return ()

# Функция вставки названий фильмов по результату поиска
def InsertFilms(nameDB: str, dirr: str, mask = '', names = 1):
    """
    nameDB -- Имя базы

    dirr -- каталог поиска файлов для занесения имен

    mask -- маска поиска

    names -- флаг для вывода полного пути к найденному файлу (0) или только имени (1)
    """

    #nameDB = "TEST.db"
    #OpenDB(nameDB)
    arr_films = SearchFiles(dirr, mask, names)
    con = sqlite3.connect(nameDB)  # открываем базу
    cur = con.cursor()  # создаем курсов
    sql_t1 = "INSERT INTO film (name_or) VALUES (?)"
    # обрабатываем исключение
    # -----------------------
    try:
        for i in arr_films:
            t1 = (i,)                       # Преобразуем строку в кортеж
            cur.execute(sql_t1, t1)         # Выполняем ОДИН SQL-запрос
    except sqlite3.DatabaseError as err:
        print("Ошибка:", err)
    else:
        print("Данные добавлены")
        con.commit()                        # Завершаем транзакцию, такие как (INSERT, REPLACE, UPDATE, DELETE)
    # -----------------------
    cur.close()                             # Закрываем объект-курсор
    con.close()                             # Закрываем соединение
    return ()
