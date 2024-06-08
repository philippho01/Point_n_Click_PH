from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Aula(TemplateRoom):
    def __init__(self, parent=None):
        super(Aula, self).__init__(parent)

        # Hintergrundbild Aula wird gesetzt
        self.init_room("Aula.jpg")

        # Sprechblase erstellen
        self.offset_balloon_x = int((1440-500)/2)
        self.offset_balloon_y = 25
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        # Hitbox zur Verwaltung setzen
        self.hitbox_zurVerwaltung = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurVerwaltung)


        # offset_ballon (Sprechblase) wird mit Text gefüllt
        self.text_line_1 = "\t\tWegweiser:"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = "Links: zur Verwaltung"
        self.text_line_5 = "Rechts: zu den Unterrichtsräumen"
        self.text_line_6 = ""

        self.hitbox_zu_EigenerRaum = QRect(1150, 215, 275, 600)
        self.append_hitbox(self.hitbox_zu_EigenerRaum)

    # Es passiert was, wenn ich auf etwas klicke
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Aula, self).mousePressEvent(ev)

        mouse_pos = ev.pos()
    # wenn ich aud die Hitbox "zur Verwaltung" klicke, komme ich zu "weis.png"
        if self.hitbox_zurVerwaltung.contains(mouse_pos):
            self.new_room.emit("weis.png")

        if self.hitbox_zu_EigenerRaum.contains(mouse_pos):
            self.new_room.emit("images.jpeg")


        self.update()
