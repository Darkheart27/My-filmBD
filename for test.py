import FindFiles
import sqlite3
import os

# Пример работы с функций SearchFiles
# -----------------
#for i in FindFiles.SearchFiles('i:\PROGRAMM\PHYTHON','.txt', 0):
#    print(i)

#for i in FindFiles.SearchFiles('r:\\','.mkv', 0):
#    print(i)
# -----------------

nameDB = "TEST.db"
print(FindFiles.SearchFiles("r:\\"))
FindFiles.OpenDB(nameDB)
FindFiles.InsertFilms(nameDB, 'r:\\','.mkv', 1)
