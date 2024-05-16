from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MusicMrsMia(object):
    def setupUi(self, MusicMrsMia):
        MusicMrsMia.setObjectName("MusicMrsMia")
        MusicMrsMia.resize(380, 671)
        MusicMrsMia.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MusicMrsMia)
        self.centralwidget.setObjectName("centralwidget")
        self.base = QtWidgets.QFrame(self.centralwidget)
        self.base.setGeometry(QtCore.QRect(0, 0, 381, 671))
        self.base.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.base.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base.setObjectName("base")
        self.wt_base = QtWidgets.QWidget(self.base)
        self.wt_base.setGeometry(QtCore.QRect(0, 0, 381, 671))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wt_base.setFont(font)
        self.wt_base.setStyleSheet("background-color:     qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(31,209,249), stop:1 rgba(182, 33,254 ));")
        self.wt_base.setObjectName("wt_base")
        self.wt_top_panel = QtWidgets.QWidget(self.wt_base)
        self.wt_top_panel.setGeometry(QtCore.QRect(0, 0, 381, 31))
        self.wt_top_panel.setStyleSheet("background-color: rgb(50, 187, 250);")
        self.wt_top_panel.setObjectName("wt_top_panel")
        self.label_internet = QtWidgets.QLabel(self.wt_top_panel)
        self.label_internet.setGeometry(QtCore.QRect(300, -10, 41, 51))
        self.label_internet.setText("")
        self.label_internet.setPixmap(QtGui.QPixmap("phone icons/6.png"))
        self.label_internet.setScaledContents(True)
        self.label_internet.setObjectName("label_internet")
        self.label_wifi = QtWidgets.QLabel(self.wt_top_panel)
        self.label_wifi.setGeometry(QtCore.QRect(270, -10, 41, 51))
        self.label_wifi.setText("")
        self.label_wifi.setPixmap(QtGui.QPixmap("phone icons/5.png"))
        self.label_wifi.setScaledContents(True)
        self.label_wifi.setObjectName("label_wifi")
        self.label_charging = QtWidgets.QLabel(self.wt_top_panel)
        self.label_charging.setGeometry(QtCore.QRect(340, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_charging.setFont(font)
        self.label_charging.setText("")
        self.label_charging.setScaledContents(True)
        self.label_charging.setObjectName("label_charging")
        self.time = QtWidgets.QLabel(self.wt_top_panel)
        self.time.setGeometry(QtCore.QRect(15, 0, 48, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setKerning(True)
        self.time.setFont(font)
        self.time.setText("")
        self.time.setObjectName("time")
        self.wt_bottom_panel = QtWidgets.QWidget(self.wt_base)
        self.wt_bottom_panel.setGeometry(QtCore.QRect(0, 640, 381, 31))
        self.wt_bottom_panel.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.wt_bottom_panel.setObjectName("wt_bottom_panel")
        self.label_back = QtWidgets.QLabel(self.wt_bottom_panel)
        self.label_back.setGeometry(QtCore.QRect(80, 0, 41, 31))
        self.label_back.setText("")
        self.label_back.setPixmap(QtGui.QPixmap("phone icons/1.png"))
        self.label_back.setScaledContents(True)
        self.label_back.setObjectName("label_back")
        self.label_home = QtWidgets.QLabel(self.wt_bottom_panel)
        self.label_home.setGeometry(QtCore.QRect(160, 0, 51, 31))
        self.label_home.setText("")
        self.label_home.setPixmap(QtGui.QPixmap("phone icons/2.png"))
        self.label_home.setScaledContents(True)
        self.label_home.setObjectName("label_home")
        self.label_wt = QtWidgets.QLabel(self.wt_bottom_panel)
        self.label_wt.setGeometry(QtCore.QRect(250, 0, 51, 31))
        self.label_wt.setText("")
        self.label_wt.setPixmap(QtGui.QPixmap("phone icons/3.png"))
        self.label_wt.setScaledContents(True)
        self.label_wt.setObjectName("label_wt")
        self.frame_music_and_3pl = QtWidgets.QFrame(self.wt_base)
        self.frame_music_and_3pl.setGeometry(QtCore.QRect(0, 30, 381, 41))
        self.frame_music_and_3pl.setStyleSheet("background-color: rgb(86, 145, 251);\n"
"")
        self.frame_music_and_3pl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_music_and_3pl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_music_and_3pl.setObjectName("frame_music_and_3pl")
        self.label_music = QtWidgets.QLabel(self.frame_music_and_3pl)
        self.label_music.setGeometry(QtCore.QRect(80, 0, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_music.setFont(font)
        self.label_music.setStyleSheet("")
        self.label_music.setObjectName("label_music")
        self.addMusic = QtWidgets.QPushButton(self.frame_music_and_3pl)
        self.addMusic.setGeometry(QtCore.QRect(0, 0, 71, 41))
        self.addMusic.setStyleSheet("QPushButton{\n"
"background-color: rgb(86, 145, 251);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(72, 123, 211)\n"
"}")
        self.addMusic.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("phone icons/13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addMusic.setIcon(icon)
        self.addMusic.setIconSize(QtCore.QSize(40, 40))
        self.addMusic.setFlat(True)
        self.addMusic.setObjectName("addMusic")
        self.prev = QtWidgets.QPushButton(self.wt_base)
        self.prev.setGeometry(QtCore.QRect(10, 140, 51, 31))
        self.prev.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 170, 250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}")
        self.prev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("phone icons/9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev.setIcon(icon1)
        self.prev.setFlat(True)
        self.prev.setObjectName("prev")
        self.play = QtWidgets.QPushButton(self.wt_base)
        self.play.setGeometry(QtCore.QRect(70, 140, 51, 31))
        self.play.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 170, 250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}")
        self.play.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("phone icons/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon2)
        self.play.setIconSize(QtCore.QSize(30, 30))
        self.play.setFlat(True)
        self.play.setObjectName("play")
        self.next = QtWidgets.QPushButton(self.wt_base)
        self.next.setGeometry(QtCore.QRect(130, 140, 51, 31))
        self.next.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 170, 250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}")
        self.next.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("phone icons/10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon3)
        self.next.setFlat(True)
        self.next.setObjectName("next")
        self.mix_it_up = QtWidgets.QPushButton(self.wt_base)
        self.mix_it_up.setGeometry(QtCore.QRect(240, 140, 51, 28))
        self.mix_it_up.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 170, 250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}")
        self.mix_it_up.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("phone icons/12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mix_it_up.setIcon(icon4)
        self.mix_it_up.setIconSize(QtCore.QSize(30, 30))
        self.mix_it_up.setFlat(True)
        self.mix_it_up.setObjectName("mix_it_up")
        self.song_list = QtWidgets.QListWidget(self.wt_base)
        self.song_list.setGeometry(QtCore.QRect(0, 180, 381, 461))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.song_list.setFont(font)
        self.song_list.setStyleSheet("QListWidget {\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-color: rgba(255, 255, 255,14);\n"
"    border-radius: 1px;\n"
"}\n"
"QListWidget::item {\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.song_list.setLineWidth(3)
        self.song_list.setObjectName("song_list")
        self.search = QtWidgets.QPushButton(self.wt_base)
        self.search.setEnabled(True)
        self.search.setGeometry(QtCore.QRect(310, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.search.setFont(font)
        self.search.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}\n"
"\n"
"")
        self.search.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("phone icons/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon5)
        self.search.setIconSize(QtCore.QSize(30, 25))
        self.search.setCheckable(False)
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.search_text = QtWidgets.QLineEdit(self.wt_base)
        self.search_text.setGeometry(QtCore.QRect(10, 90, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_text.setFont(font)
        self.search_text.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255,100);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(0, 0, 0, 0.1); \n"
"}\n"
"")
        self.search_text.setMaxLength(20)
        self.search_text.setCursorPosition(0)
        self.search_text.setObjectName("search_text")
        self.delete_music = QtWidgets.QPushButton(self.wt_base)
        self.delete_music.setGeometry(QtCore.QRect(310, 140, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_music.setFont(font)
        self.delete_music.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.delete_music.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 10px;\n"
"color:white\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}")
        self.delete_music.setIconSize(QtCore.QSize(30, 30))
        self.delete_music.setFlat(True)
        self.delete_music.setObjectName("delete_music")
        self.delete_search = QtWidgets.QPushButton(self.wt_base)
        self.delete_search.setGeometry(QtCore.QRect(279, 90, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.delete_search.setFont(font)
        self.delete_search.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid rgb(255, 255, 255,20); \n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}\n"
"")
        self.delete_search.setFlat(True)
        self.delete_search.setObjectName("delete_search")
        self.sound_slider = QtWidgets.QPushButton(self.wt_base)
        self.sound_slider.setGeometry(QtCore.QRect(190, 140, 41, 28))
        self.sound_slider.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 170, 250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}")
        self.sound_slider.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("phone icons/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sound_slider.setIcon(icon6)
        self.sound_slider.setIconSize(QtCore.QSize(25, 25))
        self.sound_slider.setFlat(True)
        self.sound_slider.setObjectName("sound_slider")
        self.horizontalSlider = QtWidgets.QSlider(self.wt_base)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 180, 201, 25))
        self.horizontalSlider.setStyleSheet("QSlider{\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(35)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        MusicMrsMia.setCentralWidget(self.centralwidget)

        self.retranslateUi(MusicMrsMia)
        QtCore.QMetaObject.connectSlotsByName(MusicMrsMia)

    def retranslateUi(self, MusicMrsMia):
        _translate = QtCore.QCoreApplication.translate
        MusicMrsMia.setWindowTitle(_translate("MusicMrsMia", "Music Mrs Mia"))
        self.label_music.setText(_translate("MusicMrsMia", "Music Mrs Mia"))
        self.search_text.setPlaceholderText(_translate("MusicMrsMia", "Search..."))
        self.delete_music.setText(_translate("MusicMrsMia", "Del"))
        self.delete_search.setText(_translate("MusicMrsMia", "X"))
