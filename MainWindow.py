from PyQt6.QtCore import pyqtSlot, Qt, QRandomGenerator
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QStatusBar, QMessageBox
from Aula import Aula
from Eingang import Eingang
from TestRaum import TestRaum
from EigenerRaum import EigenerRaum

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Aufrufen des Konstruktors der Basisklasse QMainWindow

        # Erstellen eines zufällig initialisierten Generators für sichere Zufallszahlen
        self.__random_generator = QRandomGenerator().securelySeeded()

        # Initialisieren eines Sets zur Speicherung der besuchten Räume mit gefundenen Easter Eggs
        self.__set_rooms = set()
        # Festlegen der Anzahl der zu findenden Easter Eggs
        self.__number_of_easter_eggs = 5

        # Erstellen und Konfigurieren der Statusleiste
        self.__status_bar = QStatusBar(parent)
        self.setStatusBar(self.__status_bar)

        # Setzen des Fenstertitels und Anzeigen im Vollbildmodus
        self.setWindowTitle("Schulhausrundgang")
        self.showFullScreen()

        # Erstellen der Menüleiste und Hinzufügen der Menüs und Menüpunkte
        menu_bar = QMenuBar(self)
        settings = menu_bar.addMenu("Einstellungen")
        self.__hitbox_action = settings.addAction("Hitboxen anzeigen")
        self.__hitbox_action.setCheckable(True)  # Aktion zum Umschalten der Hitbox-Anzeige
        self.__hitbox_action.setChecked(True)

        # Erstellen des "Über"-Menüs und Verbindung der Aktionen mit Slots
        about = menu_bar.addMenu("Über")
        about_us = about.addAction("Projekt")
        about_us.triggered.connect(self.about_us)
        self.setMenuBar(menu_bar)

        # Initialisieren und Einstellen des zentralen Widgets, Start im Eingangsraum
        self.central_widget = Eingang(parent)
        self.setup_new_room()

    def setup_new_room(self):
        # Setup-Funktion zum Initialisieren des neuen Raums und Konfigurieren der Verbindungen
        self.central_widget.setHitBoxVisible(self.__hitbox_action.isChecked())
        self.central_widget.leave_room.connect(self.change_room)
        self.central_widget.new_room.connect(self.renew_room)
        self.central_widget.found_easter_egg.connect(self.handler_easter_egg)
        self.__hitbox_action.toggled.connect(self.central_widget.setHitBoxVisible)
        self.setCentralWidget(self.central_widget)

# Hier erweitern, wenn ich neuen Raum hinzufüge
    @pyqtSlot(str)
    def renew_room(self, new_room):
        # Slot zum Wechseln des Raumes basierend auf dem übergebenen Raumnamen
        if new_room == "Aula.jpg":
            self.central_widget = Aula()
        elif new_room == "weis.png":
            self.central_widget = TestRaum()
        elif new_room == "images.jpeg":
            self.central_widget = EigenerRaum()

        else:
            print("Fehler: new_room nicht vergeben")
        self.setup_new_room()

# Hier erweitern, wenn ich neuen Raum hinzufüge (in welchen Raum gehe ich zurück, wenn ich EXIT drücke)
    @pyqtSlot(str)
    def change_room(self, old_room):
        # Slot zum Wechseln des Raumes, ähnlich wie renew_room, aber für den Verlassen-Event
        if old_room == "Aula.jpg":
            self.central_widget = Eingang()
        elif old_room == "weis.png":
            self.central_widget = TestRaum()
        elif old_room =="images.jpeg":
            self.central_widget = Aula()
        else:
            print("Fehler: change_room nicht vergeben")
        self.setup_new_room()

    @pyqtSlot(str)
    def handler_easter_egg(self, room_name):
        # Slot zum Verarbeiten des Findens eines Easter Eggs
        self.__set_rooms.add(room_name)
        number_found_rooms = len(self.__set_rooms)
        if number_found_rooms < self.__number_of_easter_eggs:
            message = f"Sie haben {number_found_rooms} von {self.__number_of_easter_eggs} Kaffeetassen gefunden!"
            self.__status_bar.showMessage(message)
        else:
            self.__status_bar.showMessage("Sie haben alle Kaffeetassen gefunden")
            # Anzeigen einer Nachricht und Drucken eines Gutscheins
            msg_box = QMessageBox()
            msg_box.setText("Herzlichen Glückwunsch!")
            msg_box.setInformativeText("Sie haben alle Kaffeetassen gefunden. Holen Sie sich mit dem Ausdruck Ihre "
                                       "Kaffeetasse im Raum EG 23 ab.")
            msg_box.exec()
            self.print_voucher()

    def print_voucher(self):
        # Funktion zum Drucken eines Gutscheins
        printer = QPrinter()
        print_dialog = QPrintDialog(printer)
        if print_dialog.exec() == QPrintDialog.DialogCode.Accepted:
            painter = QPainter()
            painter.begin(printer)
            painter.setPen(QColor("black"))
            # Drucken verschiedener Textelemente und Generierung eines Gutscheincodes
            page_rect = printer.pageRect(QPrinter.Unit.DevicePixel)
            painter.setFont(QFont("Helvetica [Cronyx]", 36))
            text = "Gutschein"
            bounding_rect = painter.boundingRect(page_rect, Qt.AlignmentFlag.AlignHCenter, text)
            painter.drawText(bounding_rect, text)
            # Weiteres Drucken von Text und Informationen
            # (Vollständiges Textlayout im Druckprozess wurde hier ausgelassen, sollte der Vollständigkeit halber implementiert sein)
            painter.end()

    def about_us(self):
        # Funktion zum Anzeigen von Informationen über das Projekt
        msg_box = QMessageBox(self)
        msg_box.setText("Über das Programm")
        msg_box.setInformativeText("Unser virtueller Schulhausrundgang ist im Rahmen eines Projekts der Klasse FSWI-1"
                                   " im Schuljahr 2022/23 entstanden. Wir haben die App im Fach Programmieren erstellt"
                                   " und nutzen Python mit Qt.")
        msg_box.show()
