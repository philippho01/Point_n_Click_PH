from PyQt6.QtCore import QRect, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel

from TemplateRoom import TemplateRoom

class EigenerRaum(TemplateRoom):
    def __init__(self, parent=None):
        super(EigenerRaum, self).__init__(parent)

        # Hintergrundbild Aula wird gesetzt
        self.init_room("images.jpeg")

        # Sprechblase erstellen
        self.offset_balloon_x = int((1440-500)/2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(972, 556, 50, 150)

        # wenn offset_mouth nicht zu sehen sein soll:
        #self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              #self.offset_balloon_width, 972, 556)

        # offset_ballon (Sprechblase) wird mit Text gefüllt
        self.text_line_1 = "\t\tTest-Text:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = "Test-Zeile"
        self.text_line_5 = "2. Test-Zeile"
        self.text_line_6 = ""

        # Hitbox zur Verwaltung setzen
        self.hitbox_zurVerwaltung = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurVerwaltung)

        # Datum- und Uhrzeit-Label hinzufügen
        self.datetime_label = QLabel(self)
        self.datetime_label.setGeometry(600, 50, 200, 40)  # Position und Größe des Labels
        self.datetime_label.setStyleSheet("background-color: lightgray; color: black; font-size: 16px;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Timer wird alle 1000 Millisekunden (1 Sekunde) ausgelöst

        self.update_datetime()

    def update_datetime(self):
        # Aktuelles Datum und Uhrzeit abrufen und im Label anzeigen
        current_datetime = QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm:ss")
        self.datetime_label.setText(current_datetime)
