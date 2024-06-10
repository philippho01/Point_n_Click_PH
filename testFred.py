# Importieren der notwendigen Module aus PyQt6 für UI-Elemente und Ereignisverarbeitung
from PyQt6.QtCore import QRect, Qt, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel, QPushButton

# Importieren einer benutzerdefinierten Klasse TemplateRoom, die als Basis für diesen spezifischen Raum dient
from TemplateRoom import TemplateRoom


# Definition der Klasse TestRaum, die von TemplateRoom erbt
class TestRaum(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse, um die Basisklasseninitialisierung durchzuführen
        super(TestRaum, self).__init__(parent)

        # Initialisiert den Raum mit einem Bildhintergrund
        self.init_room("weis1.png")

        # Setzt die Offsets für einen Textballon
        self.offset_balloon_x = 608
        self.offset_balloon_y = 69
        self.offset_balloon_width = 250
        self.offset_balloon_length = 800

        # Setzt den Mund-Offset für den Textballon
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        # Definiert eine Hitbox, die zu einem anderen Raum führt
        self.hitbox_zurAula = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurAula)

        # Definiert eine Hitbox, die den Text weiterschaltet
        self.hitbox_forward = QRect(1094, 200, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        # Initialisiert einen internen Zähler
        self.__counter = 0

        # Definiert eine Hitbox für ein verstecktes Element (Osterei)
        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        # Initialisiert Textzeilen, die im Raum angezeigt werden
        self.text_line_1 = ""
        self.text_line_2 = "Hallo und herzlich willkommen,"
        self.text_line_3 = "das hier ist ein Testraum"
        self.text_line_4 = "es nervt alles neu anpassen zu müssen"
        self.text_line_5 = ""
        self.text_line_6 = "                         weiter"

    # Überschreibt das MousePressEvent, um auf Mausklicks zu reagieren
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        # Ruft das MousePressEvent der Elternklasse auf
        super(TestRaum, self).mousePressEvent(ev)

        # Holt die Position des Mausklicks
        mouse_pos = ev.pos()

        # Prüft, ob die Klickposition innerhalb der Osterei-Hitbox liegt
        if self.hitbox_easter_egg.contains(mouse_pos):
            # Ändert die Textzeilen, um eine Nachricht anzuzeigen
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "GLÜCKWUNSCH!!!"
            self.text_line_4 = "Du hast deine erste Kaffeetasse gefunden."
            self.text_line_5 = ""
            self.text_line_6 = ""

            # Spielt einen Sound ab
            self.play_sound("TemplateRoom.mp3")

            # Aktualisiert den Raum, um die Änderungen anzuzeigen
            self.update()

        # Prüft, ob die Klickposition innerhalb der Hitbox liegt, die zur Aula führt
        if self.hitbox_zurAula.contains(mouse_pos):
            # Stoppt den Player (vermutlich Audio oder Video)
            self.stop_player()

            # Sendet ein Signal, um den Raum zu wechseln
            self.new_room.emit("Aula.jpg")

        # Prüft, ob die Klickposition innerhalb der Hitbox liegt, die den Text weiterschaltet
        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                # Ändert die Textzeilen für den ersten Weiter-Klick
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weitere Test"
                self.text_line_3 = "und zwar test nummer 1"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                # Erhöht den Zähler
                self.__counter = 1

            elif self.__counter == 1:
                # Ändert die Textzeilen für den zweiten Weiter-Klick
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weitere Test"
                self.text_line_3 = "und zwar test nummer 2"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                # Erhöht den Zähler
                self.__counter = 2

            elif self.__counter == 2:
                # Ändert die Textzeilen für den dritten Weiter-Klick
                self.text_line_1 = ""
                self.text_line_2 = "das hier ist ein weitere Test"
                self.text_line_3 = "und zwar test nummer 2"
                self.text_line_4 = ""
                self.text_line_5 = ""
                self.text_line_6 = "                         weiter"

                # Erhöht den Zähler
                self.__counter = 3

            # Aktualisiert den Raum, um die Änderungen anzuzeigen
            self.update()
