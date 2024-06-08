# 1. Imports etc
        #from PyQt6.QtCore import QRect
        #from PyQt6.QtGui import QMouseEvent

        #from TemplateRoom import TemplateRoom

        #class NemeNeuerRaum(TemplateRoom):
            #def __init__(self, parent=None):
                #super(NemeNeuerRaum, self).__init__(parent)

# 2. Bild hochladen
        # Hintergrundbild Aula wird gesetzt
                #self.init_room("images.jpeg")

# 3. Sprechblase setzen (MUSS GESTZT WERDEN)
# Sprechblase erstellen
        #self.offset_balloon_x = int((1440-500)/2)
        #self.offset_balloon_y = 25
        #self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              #self.offset_balloon_width, 0, 0)

# 4. Sprechblase befüllen
# offset_ballon (Sprechblase) wird mit Text gefüllt
        #self.text_line_1 = "\t\tTest-Text:"
        #self.text_line_2 = ""
        #self.text_line_3 = ""
        #self.text_line_4 = "Test-Zeile"
        #self.text_line_5 = "2. Test-Zeile"
        #self.text_line_6 = ""

# 5. Annahme: Von Aula in NeuerRaum
    #Hitbox in aula setzten
    #siehe Zeile 20 in Aula

    #self.hitbox_zurNeuerRaumName = QRect(1, 1, 250, 800) # (X_koordinate, y_Koordinate, breite, höhe)
            #self.append_hitbox(self.hitbox_zurNeuerRaumName)


# 6. Raum in MainWindow setzen (bei def renew_room)
    # siehe zeile 58

        #elif new_room == "images.jpeg": #(Hintergrundbild)
        #self.central_widget = NeuerRaumName()

# 7. In Welchen Raum gehe ich, wenn ich auf "Zurück" klicke
    # siehe Zeile 73

        #elif old_room == "images.jpeg": #(Hinergrundbild)
        #self.central_widget = Aula() #(Wenn ich in Aula zurück will)

    
# 8. Hitobox in anderen Raum
# Hitbox zur Verwaltung setzen
        #self.hitbox_zurVerwaltung = QRect(1, 1, 250, 800)
        #self.append_hitbox(self.hitbox_zurVerwaltung)
