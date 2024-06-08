from PyQt6.QtCore import QPoint, QRect, pyqtSignal, pyqtSlot, QSize, Qt, QUrl
from PyQt6.QtGui import QPixmap, QMouseEvent, QPaintEvent, QPainter, QColor, QFont, QPolygon, QPen, QBrush
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudioDevice
from PyQt6.QtWidgets import QLabel

# Grundgerüst für alle anderen Räume wird gebaut

class TemplateRoom(QLabel):
    leave_room = pyqtSignal(str)
    new_room = pyqtSignal(str)
    found_easter_egg = pyqtSignal(str)

    def __init__(self, parent=None):
        super(TemplateRoom, self).__init__(parent)
        self.__room_name = None
        self.__background_pixmap = None

        self.__show_exit_button = True
        self.__show_speech_bubble = True

        self.__size = QSize(1440, 900)
        self.__offset_exit = 10
        self.__heigth_box = 30

        self.__hitboxes = list()
        self.__hitbox_visible = False

        self.text_line_1 = None
        self.text_line_2 = None
        self.text_line_3 = None
        self.text_line_4 = None
        self.text_line_5 = None
        self.text_line_6 = None

        self.__mouse_pos = QPoint()

        #offset_ballon = Sprechblase
        self.offset_balloon_length = 500
        self.offset_balloon_width = 150

        self.hitbox_exit = QRect()
        self.append_hitbox(self.hitbox_exit)

        self.hitbox_easter_egg = QRect(0, 0, 0, 0)

        self.mouth_to_speech = QPolygon()

        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.CrossCursor)

        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        for hitbox in self.__hitboxes:
            if hitbox.contains(ev.pos()):
                if self.cursor().shape() != Qt.CursorShape.PointingHandCursor:
                    self.setCursor(Qt.CursorShape.PointingHandCursor)

                return

        if self.hitbox_easter_egg.contains(ev.pos()):
            if self.cursor().shape() != Qt.CursorShape.PointingHandCursor:
                self.setCursor(Qt.CursorShape.PointingHandCursor)

            return

        if self.cursor().shape() != Qt.CursorShape.CrossCursor:
            self.setCursor(Qt.CursorShape.CrossCursor)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.__mouse_pos = ev.pos()

        print(ev.pos())

        if self.hitbox_exit.contains(self.__mouse_pos):
            self.stop_player()

            self.leave_room.emit(self.__room_name)
        elif self.hitbox_easter_egg.contains(self.__mouse_pos):
            self.found_easter_egg.emit(self.__room_name)

        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.drawPixmap(QPoint(0, 0), self.__background_pixmap)

        old_pen = painter.pen()
        new_pen = QPen()
        new_pen.setColor(QColor("black"))
        new_pen.setWidth(5)
        painter.setPen(new_pen)

        old_brush = painter.brush()
        new_brush = QBrush()
        new_brush.setColor(QColor("white"))
        new_brush.setStyle(Qt.BrushStyle.Dense2Pattern)
        painter.setBrush(new_brush)

        if self.__show_speech_bubble:
            painter.drawRoundedRect(self.offset_balloon_x, self.offset_balloon_y, self.offset_balloon_length,
                                    self.offset_balloon_width, 10, 10)

            new_pen.setStyle(Qt.PenStyle.NoPen)
            painter.setPen(new_pen)

            painter.drawPolygon(self.mouth_to_speech)
            painter.drawRect(self.mouth_to_speech.at(1).x() + 5, self.mouth_to_speech.at(1).y() - 5,
                             self.mouth_to_speech.at(2).x() - self.mouth_to_speech.at(1).x() - 5, 5)

            new_pen.setStyle(Qt.PenStyle.SolidLine)
            painter.setPen(new_pen)

            painter.drawLine(self.mouth_to_speech.at(0), self.mouth_to_speech.at(1))
            painter.drawLine(self.mouth_to_speech.at(2), self.mouth_to_speech.at(0))

        if self.__show_exit_button:
            new_pen.setColor(QColor("goldenrod"))
            new_pen.setStyle(Qt.PenStyle.SolidLine)
            painter.setPen(new_pen)
            new_brush.setColor(QColor("gold"))
            painter.setBrush(new_brush)

            painter.drawRoundedRect(QRect(self.__offset_exit, self.__pos_x_exit, 100, self.__heigth_box), 10, 10)

        painter.setBrush(old_brush)
        painter.setPen(old_pen)

        font = QFont("Courier", 24)
        font.setBold(True)
        font.setItalic(True)
        painter.setFont(font)
        painter.setPen(QColor("black"))

        if self.__show_speech_bubble:
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 25, self.text_line_1)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 50, self.text_line_2)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 75, self.text_line_3)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 100, self.text_line_4)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 125, self.text_line_5)
            painter.drawText(self.offset_balloon_x + 10, self.offset_balloon_y + 150, self.text_line_6)

        if self.__show_exit_button:
            painter.drawText(self.__offset_exit + 10, self.__pos_x_exit + 25, "Zurück")

        if self.__hitbox_visible:
            if self.__mouse_pos:
                painter.setPen(QColor("red"))
                painter.drawEllipse(self.__mouse_pos, 10, 10)

            for hitbox in self.__hitboxes:
                painter.setPen(QColor("greenyellow"))
                painter.drawRect(hitbox)

            if self.hitbox_easter_egg:
                painter.setPen(QColor("cyan"))
                painter.drawRect(self.hitbox_easter_egg)

    @pyqtSlot(bool)
    def setHitBoxVisible(self, visible: bool):
        self.__hitbox_visible = visible

        self.update()

    def init_room(self, room_name):
        self.__room_name = room_name
        self.__background_pixmap = QPixmap(self.__room_name).scaled(self.__size.width(), self.__size.height())

        self.__pos_x_exit = self.__size.height() - self.__offset_exit - self.__heigth_box - 30
        self.hitbox_exit = QRect(self.__offset_exit, self.__pos_x_exit, 100, self.__heigth_box)

    def append_hitbox(self, hitbox):
        self.__hitboxes.append(hitbox)

    def set_offset_mouth(self, x, y, offset_x, width):
        self.mouth_to_speech.clear()

        self.mouth_to_speech.append(QPoint(x, y))
        self.mouth_to_speech.append(QPoint(self.offset_balloon_x + self.offset_balloon_width + offset_x,
                                           self.offset_balloon_y + self.offset_balloon_width))
        self.mouth_to_speech.append(QPoint(self.offset_balloon_x + self.offset_balloon_width + offset_x + width,
                                           self.offset_balloon_y + self.offset_balloon_width))

    def show_exit_button(self, visible):
        self.__show_exit_button = visible

    def show_speech_bubble(self, visible):
        self.__show_speech_bubble = visible

    def play_sound(self, source_path):
        if not self.player.isPlaying():
            self.player.setSource(QUrl.fromLocalFile(source_path))
            self.audioOutput.setVolume(50)
            self.player.play()

    def stop_player(self):
        if self.player.isPlaying():
            self.player.stop()
