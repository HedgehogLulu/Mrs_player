import interface
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime, QTimer, Qt
import random
import pygame
import psutil
import os
import sys


class MyPlayer(QtWidgets.QMainWindow, interface.Ui_MusicMrsMia):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.mixer.init()

        self.setupUi(self)
        # Фиксируем размер виджета
        self.setFixedSize(self.size())

        self.addMusic.clicked.connect(self.Add_music)
        self.play.clicked.connect(self.Play_pause_music)

        # Флаги для управления воспроизведением музыки
        self.playing = False
        self.paused = False

        # Текущая позиция воспроизведения
        self.play_pos = 0
        # Плейлист, список для воспроизведения песен
        self.playlist = []

        # Индекс текущей воспроизводимой песни
        self.current_song = 0
        # Список найденных песен после поиска
        self.found_songs = []

        self.prev.clicked.connect(self.Prev_music)
        self.next.clicked.connect(self.Next_music)
        self.mix_it_up.clicked.connect(self.Shuffle_music)
        self.delete_music.clicked.connect(self.Remove_music)
        self.search.clicked.connect(self.Search_music)
        self.search_text.returnPressed.connect(self.Search_music)
        self.delete_search.clicked.connect(self.Remove_search)

        self.horizontalSlider.setVisible(False)
        self.sound_slider.clicked.connect(self.show_hide_slider)
        self.horizontalSlider.valueChanged.connect(self.volume_control)

        # Создание таймера для обновления отображения времени
        self.timer = QTimer()
        self.timer.timeout.connect(self._time)
        self.timer.start(1000)

    def _time(self):
        """ Этот метод обновляет метку self.time текущим временем
        в формате "чч:мм" и вызывает метод self.charging().
        Метод _time вызывается каждый раз, когда истекает
        таймер, созданный в предыдущем фрагменте кода """

        self.time.setText((QDateTime.currentDateTime().toString("hh:mm")))
        self.charging()

    def charging(self):
        """ Этот метод обновляет отображение уровня заряда батареи """

        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            self.label_charging.setText(f"{percent}%")

    def Add_music(self):
        """ Этот метод открывает диалоговое окно выбора файла с заголовком
        "Выберите файлы с музыкой" и фильтром файлов, который отображает
        только MP3-файлы (*.mp3).
        Проверяет, бы ли раньше добавлены файлы, и добавляет их в плейлист
        только в том случае, если они еще не добавлены.
        Отображает имена файлов (без пути) в списке песен.
        Если файлы были добавлены, появляется окно с сообщением. """

        files, _ = QFileDialog.getOpenFileNames(self, "Выберите файлы с музыкой", "", "MP3 файлы (*.mp3)")
        if files:
            for file_path in files:
                if file_path not in self.playlist:
                    self.playlist.append(file_path)
                    self.song_list.addItem(os.path.basename(file_path))
                else:
                    QMessageBox.warning(self, "Ошибка", "Песня уже добавлена")

    def Play_pause_music(self):
        """ 1. Получение индекс строки (песни), которая выбрана
            2. Проверяет наличие песен в плейлисте или списке найденных песен.
            3. Проверяет выбран ли элемент в списке песен.
            4. Если список найденных песен не пуст:
            - Устанавливает в current_song выбранный индекс
            - Восстанавливает воспроизведение текущей песни, если она уже воспроизводилась и была приостановлена.
            - Приостанавливает воспроизведение текущей песни, если она воспроизводится.
            5. Если список найденных песен пуст и плейлист не пуст:
            - Устанавливает в current_song выбранный индекс.
            - Восстанавливает воспроизведение текущей песни, если она уже воспроизводилась и была приостановлена.
            - Приостанавливает воспроизведение текущей песни, если она воспроизводится. """

        selected_index = self.song_list.currentRow()
        if self.playlist or self.found_songs:
            if selected_index >= 0:
                if self.found_songs:
                    if selected_index < len(self.found_songs):
                        if self.current_song == selected_index and self.found_songs:
                            if self.paused:
                                pygame.mixer.music.unpause()
                                self.paused = False
                            else:
                                pygame.mixer.music.pause()
                                self.paused = True
                        else:
                            self.current_song = selected_index
                            if self.playing:
                                pygame.mixer.music.stop()
                            pygame.mixer.music.load(self.found_songs[self.current_song])
                            pygame.mixer.music.play()
                            self.playing = True
                            self.paused = False
                            self.song_list.setCurrentRow(self.current_song)
                else:
                    if selected_index < len(self.playlist):
                        if self.current_song == selected_index and self.playing:
                            if self.paused:
                                pygame.mixer.music.unpause()
                                self.paused = False
                            else:
                                pygame.mixer.music.pause()
                                self.paused = True
                        else:
                            self.current_song = selected_index
                            if self.playing:
                                pygame.mixer.music.stop()
                            pygame.mixer.music.load(self.playlist[self.current_song])
                            pygame.mixer.music.play()
                            self.playing = True
                            self.paused = False
                            self.song_list.setCurrentRow(self.current_song)

    def Prev_music(self):
        """ Этот метод уменьшает индекс текущей песни на 1,
        обрабатывая переход к началу плейлиста,
        загружает и воспроизводит предыдущую песню. """
        if self.playlist:
            self.current_song = (self.current_song - 1) % len(self.playlist)
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            self.song_list.setCurrentRow(self.current_song)

    def Next_music(self):
        """ Этот метод увеличивает индекс текущей песни на 1,
        обрабатывая переход к концу плейлиста,
        загружает и воспроизводит следующую песню. """

        if self.playlist:
            self.current_song = (self.current_song + 1) % len(self.playlist)
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            self.song_list.setCurrentRow(self.current_song)

    def Shuffle_music(self):
        """ Этот метод случайным образом переупорядочивает список песен,
        обновляет список песен в интерфейсе и начинает воспроизведение
        с первой песни из перемешанного списка.  """

        if self.playlist:
            random.shuffle(self.playlist)
            self.song_list.clear()
            for song in self.playlist:
                song_name = os.path.basename(song)
                self.song_list.addItem(song_name)
            self.current_song = 0
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            self.song_list.setCurrentRow(self.current_song)

    def show_hide_slider(self):
        """ Этот метод переключает видимость ползунка self.horizontalSlider.
         Если ползунок виден, он становится невидимым, и наоборот"""

        if self.horizontalSlider.isVisible():
            self.horizontalSlider.setVisible(False)
        else:
            self.horizontalSlider.setVisible(True)

    def volume_control(self):
        """ Этот метод получает значение ползунка и устанавливает громкость
        музыки в соответствии с этим значением.  """
        volume = self.horizontalSlider.value() / 100
        pygame.mixer.music.set_volume(volume)

    def Search_music(self):
        """ Этот метод получает текст из поля поиска,
        фильтрует список песен, отображая только те,
        которые соответствуют запросу (поиск по имени файла),
        и обновляет список песен в интерфейсе; если не найдено
        ни одной песни, отображается сообщение в текстовом поле поиска.
        Если запрос пустой, отображаются все песни плейлиста. """

        search_query = self.search_text.text()
        self.song_list.clear()
        if not search_query:
            self.Remove_song_list()
            return

        found = False
        for song_path in self.playlist:
            if search_query.lower() in os.path.basename(song_path).lower():
                self.found_songs.append(song_path)
                self.song_list.addItem(os.path.basename(song_path))
                found = True

        if not found:
            self.search_text.setText("Песня не найдена")

    def PressEvent(self, event):
        """ Этот метод проверяет, нажата ли клавиша Enter.
        Если нажата клавиша Enter, вызывается метод self.Search_music() для поиска музыки. """
        if event.key() == Qt.key_return:
            self.Search_music()

    def Remove_song_list(self):
        """ Этот метод очищает список песен и затем добавляет в него
         имена всех файлов (без пути) из плейлиста. """

        self.song_list.clear()
        for song_path in self.playlist:
            self.song_list.addItem(os.path.basename(song_path))

    def Remove_search(self):
        """ Этот метод очищает поисковое поле
        и обновляет список песен."""

        self.search_text.clear()
        self.Remove_song_list()

    def Remove_music(self):
        """ Этот метод получает выбранную песню из списка песен,
        удаляет ее из плейлиста и списка песен в интерфейсе,
        а также обновляет индекс текущей песни и останавливает
        воспроизведение, если это необходимо. """

        selected_item = self.song_list.currentItem()
        if selected_item:
            row = self.song_list.currentRow()
            self.song_list.takeItem(row)
            del self.playlist[row]

            if self.current_song == row:
                pygame.mixer.music.stop()

            if self.current_song >= row:
                self.current_song -= 1

    def closeEvent(self, event):
        """ Этот метод переопределяет метод closeEvent родительского класса.
        Он останавливает воспроизведение музыки перед закрытием окна. """
        pygame.mixer.music.stop()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = MyPlayer()
    player.setWindowIcon(QIcon("phone icons/po.ico"))
    player.show()
    sys.exit(app.exec_())
