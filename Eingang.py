from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Eingang(TemplateRoom):
    def __init__(self, parent=None):
        super(Eingang, self).__init__(parent)
        self.show_exit_button(False)

        self.init_room("Eingang.jpg")

        self.offset_balloon_x = 750
        self.offset_balloon_y = 20
        self.offset_balloon_width = 180
        self.offset_balloon_length = 650

        self.set_offset_mouth(787, 271, 50, 150)

        self.hitbox_door_1 = QRect(5, 215, 350, 600)
        self.append_hitbox(self.hitbox_door_1)

        self.hitbox_door_2 = QRect(1150, 215, 275, 600)
        self.append_hitbox(self.hitbox_door_2)

        self.hitbox_forward = QRect(1270, 150, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        self.__counter = 0

        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        self.text_line_1 = ""
        self.text_line_2 = "Hallo und herzlich willkommen,"
        self.text_line_3 = "zum Tag der offenen Tür am 16. März 2024"
        self.text_line_4 = "im SBS Herzogenaurach."
        self.text_line_5 = ""
        self.text_line_6 = "                                    weiter"

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Eingang, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_easter_egg.contains(mouse_pos):
            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = "GLÜCKWUNSCH!!!"
            self.text_line_4 = "Du hast deine erste Kaffeetasse gefunden."
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.play_sound("TemplateRoom.mp3")

            self.update()

        if self.hitbox_door_1.contains(mouse_pos):
            self.stop_player()

            self.new_room.emit("Aula.jpg")

        if self.hitbox_door_2.contains(mouse_pos):
            self.stop_player()

            self.new_room.emit("Aula.jpg")

        if self.hitbox_forward.contains(mouse_pos):
            if self.__counter == 0:
                self.text_line_1 = ""
                self.text_line_2 = "Ich heiße David Ojimba"
                self.text_line_3 = "und begleite dich heute"
                self.text_line_4 = "durch unsere Schule."
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

                self.__counter = 1

            elif self.__counter == 1:
                self.text_line_1 = "Hier ist unser Point & Click Adventure."
                self.text_line_2 = "Wir haben es für dich erstellt,"
                self.text_line_3 = "um dir einen Einblick in unsere"
                self.text_line_4 = "verschiedenen Fachschulen zu geben."
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

                self.__counter = 2

            elif self.__counter == 2:
                self.text_line_1 = ""
                self.text_line_2 = "Die grünen Hitboxen zeigen dir an,"
                self.text_line_3 = "worauf du klicken kannst."
                self.text_line_4 = "Falls du Fragen hast melde "
                self.text_line_5 = "dich gerne bei uns."
                self.text_line_6 = "                                    weiter"

                self.__counter = 3

            elif self.__counter == 3:
                self.text_line_1 = "In manchen Räumen ist eine Tasse versteckt."
                self.text_line_2 = ""
                self.text_line_3 = "Gehe von Raum zu Raum,"
                self.text_line_4 = "denn am Ende hast du die Chance"
                self.text_line_5 = "eine Kaffeetasse zu gewinnen."
                self.text_line_6 = "                                    weiter"

                self.__counter = 4

            elif self.__counter == 4:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = "Naaa, hast du schon"
                self.text_line_4 = "eine Tasse entdeckt?"
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

                self.__counter = 5

            elif self.__counter == 5:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = "Besuche jede Raum"
                self.text_line_4 = "und finde die Tassen!."
                self.text_line_5 = ""
                self.text_line_6 = "                                    weiter"

                self.__counter = 6

            elif self.__counter == 6:
                self.text_line_1 = ""
                self.text_line_2 = ""
                self.text_line_3 = ""
                self.text_line_4 = "Viel Spaß bei der Suche!"
                self.text_line_5 = ""
                self.text_line_6 = ""

            self.update()
