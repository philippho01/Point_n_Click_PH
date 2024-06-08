from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom

class EigenerRaum(TemplateRoom):
    def __init__(self, parent=None):
        super(EigenerRaum, self).__init__(parent)

        # Hintergrundbild Aula wird gesetzt
        self.init_room("images.jpeg")

        # Sprechblase erstellen
        self.offset_balloon_x = int((1440-500)/2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        # Hitbox zur Verwaltung setzen
        self.hitbox_zurVerwaltung = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurVerwaltung)


        # offset_ballon (Sprechblase) wird mit Text gefüllt
        self.text_line_1 = "\t\tTest-Text:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = "Test-Zeile"
        self.text_line_5 = "2. Test-Zeile"
        self.text_line_6 = ""
