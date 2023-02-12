from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QLabel
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont
import sys
import random
app=QApplication(sys.argv)
ls=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
random.shuffle(ls)
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Puzzle")
        self.setGeometry(200,200,600,600)
        self.start()
        self.n=0
    def winner(self):
        if self.but1.text()+self.but2.text()+self.but3.text()+self.but4.text()+self.but5.text()+self.but6.text()+self.but7.text()+self.but8.text()+self.but9.text() \
            +self.but10.text()+self.but11.text()+self.but12.text()+self.but13.text()+self.but14.text()+self.but15.text()=="123456789101112131415":
            miniwindow = QMessageBox(self)
            miniwindow.setText("YOU WIN!!!")
            miniwindow.setWindowTitle("Canguralation!")
            miniwindow.setIcon(QMessageBox.Information)
            miniwindow.show()
            self.n=0
            random.shuffle(ls)

    def font_but(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.move(x,y)
        obj.setFixedSize(70,70)

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 24))
        obj.move(x, y)

    def start(self):
        #Labels
        self.moves=QLabel("Moves:",self)
        self.font(self.moves,30,350)
        self.num=QLabel("0   ",self)
        self.font(self.num,130,350)
        self.num.adjustSize()
        self.moves.adjustSize()
        # Buttons
        self.but1=QPushButton(ls[0],self)
        self.font_but(self.but1,80,20)

        self.but2 = QPushButton(ls[1], self)
        self.font_but(self.but2, 150, 20)

        self.but3 = QPushButton(ls[2], self)
        self.font_but(self.but3, 220, 20)

        self.but4 = QPushButton(ls[3], self)
        self.font_but(self.but4, 290, 20)

        self.but5 = QPushButton(ls[4], self)
        self.font_but(self.but5, 80, 90)

        self.but6 = QPushButton(ls[5], self)
        self.font_but(self.but6, 150, 90)

        self.but7 = QPushButton(ls[6], self)
        self.font_but(self.but7, 220, 90)

        self.but8 = QPushButton(ls[7], self)
        self.font_but(self.but8, 290, 90)

        self.but9 = QPushButton(ls[8], self)
        self.font_but(self.but9, 80, 160)

        self.but10 = QPushButton(ls[9], self)
        self.font_but(self.but10, 150, 160)

        self.but11 = QPushButton(ls[10], self)
        self.font_but(self.but11, 220, 160)

        self.but12 = QPushButton(ls[11], self)
        self.font_but(self.but12, 290, 160)

        self.but13 = QPushButton(ls[12], self)
        self.font_but(self.but13, 80, 230)

        self.but14 = QPushButton(ls[13], self)
        self.font_but(self.but14, 150, 230)

        self.but15 = QPushButton(ls[14], self)
        self.font_but(self.but15, 220, 230)

        self.but16=QPushButton("",self)
        self.font_but(self.but16,290,230)
        self.but16.hide()

        self.but16.clicked.connect(self.run_but16)
        self.but15.clicked.connect(self.run_but15)
        self.but14.clicked.connect(self.run_but14)
        self.but13.clicked.connect(self.run_but13)
        self.but12.clicked.connect(self.run_but12)
        self.but11.clicked.connect(self.run_but11)
        self.but10.clicked.connect(self.run_but10)
        self.but9.clicked.connect(self.run_but9)
        self.but8.clicked.connect(self.run_but8)
        self.but7.clicked.connect(self.run_but7)
        self.but6.clicked.connect(self.run_but6)
        self.but5.clicked.connect(self.run_but5)
        self.but4.clicked.connect(self.run_but4)
        self.but3.clicked.connect(self.run_but3)
        self.but2.clicked.connect(self.run_but2)
        self.but1.clicked.connect(self.run_but1)
    def run_but16(self):
        if self.but15.isHidden():
            self.but15.show()
            self.but15.setText(self.but16.text())
            self.but16.hide()
            self.n += 1
        elif self.but12.isHidden():
            self.but12.show()
            self.but12.setText(self.but16.text())
            self.but16.hide()
            self.n += 1
        self.winner()
        self.num.setText(str(self.n))
    def run_but15(self):
        if self.but16.isHidden():
            self.but16.show()
            self.but16.setText(self.but15.text())
            self.but15.hide()
            self.n += 1
        elif self.but11.isHidden():
            self.but11.show()
            self.but11.setText(self.but15.text())
            self.but15.hide()
            self.n += 1
        elif self.but14.isHidden():
            self.but14.show()
            self.but14.setText(self.but15.text())
            self.but15.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but14(self):
        if self.but15.isHidden():
            self.but15.show()
            self.but15.setText(self.but14.text())
            self.but14.hide()
            self.n += 1
        elif self.but10.isHidden():
            self.but10.show()
            self.but10.setText(self.but14.text())
            self.but14.hide()
            self.n += 1
        elif self.but13.isHidden():
            self.but13.show()
            self.but13.setText(self.but14.text())
            self.but14.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but13(self):
        if self.but14.isHidden():
            self.but14.show()
            self.but14.setText(self.but13.text())
            self.but13.hide()
            self.n += 1
        elif self.but9.isHidden():
            self.but9.show()
            self.but9.setText(self.but13.text())
            self.but13.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but12(self):
        if self.but16.isHidden():
            self.but16.show()
            self.but16.setText(self.but12.text())
            self.but12.hide()
            self.n += 1
        elif self.but11.isHidden():
            self.but11.show()
            self.but11.setText(self.but12.text())
            self.but12.hide()
            self.n += 1
        elif self.but8.isHidden():
            self.but8.show()
            self.but8.setText(self.but12.text())
            self.but12.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but11(self):
        if self.but12.isHidden():
            self.but12.show()
            self.but12.setText(self.but11.text())
            self.but11.hide()
            self.n += 1
        elif self.but15.isHidden():
            self.but15.show()
            self.but15.setText(self.but11.text())
            self.but11.hide()
            self.n += 1
        elif self.but10.isHidden():
            self.but10.show()
            self.but10.setText(self.but11.text())
            self.but11.hide()
            self.n += 1
        elif self.but7.isHidden():
            self.but7.show()
            self.but7.setText(self.but11.text())
            self.but11.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but10(self):
        if self.but11.isHidden():
            self.but11.show()
            self.but11.setText(self.but10.text())
            self.but10.hide()
            self.n += 1
        elif self.but14.isHidden():
            self.but14.show()
            self.but14.setText(self.but10.text())
            self.but10.hide()
            self.n += 1
        elif self.but9.isHidden():
            self.but9.show()
            self.but9.setText(self.but10.text())
            self.but10.hide()
            self.n += 1
        elif self.but6.isHidden():
            self.but6.show()
            self.but6.setText(self.but10.text())
            self.but10.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but9(self):
        if self.but5.isHidden():
            self.but5.show()
            self.but5.setText(self.but9.text())
            self.but9.hide()
            self.n += 1
        elif self.but10.isHidden():
            self.but10.show()
            self.but10.setText(self.but9.text())
            self.but9.hide()
            self.n += 1
        elif self.but13.isHidden():
            self.but13.show()
            self.but13.setText(self.but9.text())
            self.but9.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but8(self):
        if self.but12.isHidden():
            self.but12.show()
            self.but12.setText(self.but8.text())
            self.but8.hide()
            self.n += 1
        elif self.but7.isHidden():
            self.but7.show()
            self.but7.setText(self.but8.text())
            self.but8.hide()
            self.n += 1
        elif self.but4.isHidden():
            self.but4.show()
            self.but4.setText(self.but8.text())
            self.but8.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but7(self):
        if self.but8.isHidden():
            self.but8.show()
            self.but8.setText(self.but7.text())
            self.but7.hide()
            self.n += 1
        elif self.but11.isHidden():
            self.but11.show()
            self.but11.setText(self.but7.text())
            self.but7.hide()
            self.n += 1
        elif self.but6.isHidden():
            self.but6.show()
            self.but6.setText(self.but7.text())
            self.but7.hide()
            self.n += 1
        elif self.but3.isHidden():
            self.but3.show()
            self.but3.setText(self.but7.text())
            self.but7.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but6(self):
        if self.but7.isHidden():
            self.but7.show()
            self.but7.setText(self.but6.text())
            self.but6.hide()
            self.n += 1
        elif self.but10.isHidden():
            self.but10.show()
            self.but10.setText(self.but6.text())
            self.but6.hide()
            self.n += 1
        elif self.but5.isHidden():
            self.but5.show()
            self.but5.setText(self.but6.text())
            self.but6.hide()
            self.n += 1
        elif self.but2.isHidden():
            self.but2.show()
            self.but2.setText(self.but6.text())
            self.but6.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but5(self):
        if self.but1.isHidden():
            self.but1.show()
            self.but1.setText(self.but5.text())
            self.but5.hide()
            self.n += 1
        elif self.but9.isHidden():
            self.but9.show()
            self.but9.setText(self.but5.text())
            self.but5.hide()
            self.n += 1
        elif self.but6.isHidden():
            self.but6.show()
            self.but6.setText(self.but5.text())
            self.but5.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but4(self):
        if self.but3.isHidden():
            self.but3.show()
            self.but3.setText(self.but4.text())
            self.but4.hide()
            self.n += 1
        elif self.but8.isHidden():
            self.but8.show()
            self.but8.setText(self.but4.text())
            self.but4.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but3(self):
        if self.but4.isHidden():
            self.but4.show()
            self.but4.setText(self.but3.text())
            self.but3.hide()
            self.n += 1
        elif self.but7.isHidden():
            self.but7.show()
            self.but7.setText(self.but3.text())
            self.but3.hide()
            self.n += 1
        elif self.but2.isHidden():
            self.but2.show()
            self.but2.setText(self.but3.text())
            self.but3.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but2(self):
        if self.but3.isHidden():
            self.but3.show()
            self.but3.setText(self.but2.text())
            self.but2.hide()
            self.n += 1
        elif self.but6.isHidden():
            self.but6.show()
            self.but6.setText(self.but2.text())
            self.but2.hide()
            self.n += 1
        elif self.but1.isHidden():
            self.but1.show()
            self.but1.setText(self.but2.text())
            self.but2.hide()
            self.n += 1
        self.num.setText(str(self.n))
    def run_but1(self):
        if self.but5.isHidden():
            self.but5.show()
            self.but5.setText(self.but1.text())
            self.but1.hide()
            self.n += 1
        elif self.but2.isHidden():
            self.but2.show()
            self.but2.setText(self.but1.text())
            self.but1.hide()
            self.n += 1
        self.num.setText(str(self.n))

oyna=window()
oyna.show()
app.exec_()