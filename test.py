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
