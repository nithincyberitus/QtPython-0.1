

def paintEvent(self, event):
    rect = QRect(10, 20, 80, 60)
    startAngle = 30 * 16
    arcLength = 120 * 16
    painter = QPainter()
    painter.begin(self)
    painter.setPen(self.pen)
    painter.setBrush(self.brush)
    if self.shape == PaintArea.Line:
        painter.drawLine(rect.bottomLeft(), rect.topRight())
    elif self.shape == PaintArea.Points:
        painter.drawPoints(PaintArea.points)
    elif self.shape == PaintArea.Polyline:
        painter.drawPolyline(PaintArea.points)
    elif self.shape == PaintArea.Polygon:
        painter.drawPolygon(PaintArea.points)
    elif self.shape == PaintArea.Rect:
        painter.drawRect(rect)
    elif self.shape == PaintArea.RoundRect:
        painter.drawRoundRect(rect)
    elif self.shape == PaintArea.Ellipse:
        painter.drawEllipse(rect)
    elif self.shape == PaintArea.Arc:
        painter.drawArc(rect, startAngle, arcLength)
    elif self.shape == PaintArea.Chord:
        painter.drawChord(rect, startAngle, arcLength)
    elif self.shape == PaintArea.Pie:
        painter.drawPie(rect, startAngle, arcLength)
    elif self.shape == PaintArea.Path:
        painter.drawPath(path)
    elif self.shape == PaintArea.Text:
        painter.drawText(rect, QtCore.Qt.AlignCenter, "Basic Drawing Widget")
    painter.end()
