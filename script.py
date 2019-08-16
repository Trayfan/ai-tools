from get_text import GetText
from get_screen import GetScreen
from database import DataBase


"""
---This part for text recognition and picture acquisition by OOP---

image_name = 'screenshot.png'

Screen = GetScreen()
Screen.get_screen(image_name)

Text = GetText()
Text.get_text(image_name)
"""

table_name = "Lots"
# data = (count, name, lvl, cost, price, nickname)
data = [(1,'Shield of Gods',50,5000000,5000000,'FaceOfDeath'),
        (2,'Sword of Gods',50,5000000,2500000,'Ботвинник')]

DB = DataBase()
DB.create(table_name)
DB.insert(table_name, data)
print(DB.select("SELECT * FROM Lots WHERE lvl=50"))
