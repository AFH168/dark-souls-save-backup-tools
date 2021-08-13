import sys
import os
import shutil
import winsound
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QFileDialog, QErrorMessage
from pynput import keyboard

import constant


selectedSaveFile = {
    'path' : os.environ['USERPROFILE'] + constant.DARK_SOULS_I_DEFAULT_SAVE_PATH,
    'name' : constant.DARK_SOULS_I_SAVE_FILE_NAME
}

class AppDemo(QWidget):
    
    DS1SavePath = os.environ['USERPROFILE'] + constant.DARK_SOULS_I_DEFAULT_SAVE_PATH
    DS2SavePath = os.environ['USERPROFILE'] + constant.DARK_SOULS_II_DEFAULT_SAVE_PATH
    DS3SavePath = os.environ['USERPROFILE'] + constant.DARK_SOULS_III_DEFAULT_SAVE_PATH


    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Users/alifh/OneDrive/Desktop/py gui/main.ui', self)
        self.SaveFolderPath.setText(selectedSaveFile['path'])
        self.comboBox.currentIndexChanged.connect(self.selectGame)
        self.selectSaveFolderButton.clicked.connect(self.selectPath)
        self.saveButton.clicked.connect(self.careatSaveBackup)
        self.loadButton.clicked.connect(self.loadSaveBackup)


    def selectGame(self):

        if(self.comboBox.currentIndex() == 0):
            self.updateSelectedSaveFile(self.DS1SavePath, constant.DARK_SOULS_I_SAVE_FILE_NAME)
            self.SaveFolderPath.setText(selectedSaveFile['path'])

        elif(self.comboBox.currentIndex() == 1):
            self.updateSelectedSaveFile(self.DS2SavePath, constant.DARK_SOULS_II_SAVE_FILE_NAME)
            self.SaveFolderPath.setText(selectedSaveFile['path'])

        elif(self.comboBox.currentIndex() == 2):
            self.updateSelectedSaveFile(self.DS3SavePath, constant.DARK_SOULS_III_SAVE_FILE_NAME)
            self.SaveFolderPath.setText(selectedSaveFile['path'])


    def selectPath(self):

        self.SaveFolderPath.setText(QFileDialog.getExistingDirectory(self, "Select Directory"))

        if(self.comboBox.currentIndex() == 0):
            self.updateSelectedSaveFile(self.SaveFolderPath.text(), constant.DARK_SOULS_I_SAVE_FILE_NAME)
            self.DS1SavePath = self.SaveFolderPath.text()

        elif(self.comboBox.currentIndex() == 1):
            self.updateSelectedSaveFile(self.SaveFolderPath.text(), constant.DARK_SOULS_II_SAVE_FILE_NAME)
            self.DS2SavePath = self.SaveFolderPath.text()

        elif(self.comboBox.currentIndex() == 2):
            self.updateSelectedSaveFile(self.SaveFolderPath.text(), constant.DARK_SOULS_II_SAVE_FILE_NAME)
            self.DS3SavePath = self.SaveFolderPath.text()


    def updateSelectedSaveFile(self, path, name):
        selectedSaveFile['path'] = path
        selectedSaveFile['name'] = name

    def careatSaveBackup(self):
        try:
            shutil.copy2(selectedSaveFile['path'] + '/' + selectedSaveFile['name'], selectedSaveFile['path'] + '\\backup_' + selectedSaveFile['name'])
            self.labelStatus.setText('<html><head/><body><p>Status : <span style=" color:#00aa00;"> Save backup created.</span></p></body></html>')
            winsound.PlaySound('C:/Users/alifh/OneDrive/Desktop/py gui/save_Backup_Careated.wav', winsound.SND_FILENAME)
        except:
            self.labelStatus.setText('<html><head/><body><p>Status : <span style=" color:#ff0000;"> Save file not found.</span></p></body></html>')
        
    def loadSaveBackup(self):
        try:
            shutil.copy2(selectedSaveFile['path'] + '\\backup_' + selectedSaveFile['name'], selectedSaveFile['path'] + '/' + selectedSaveFile['name'])
            self.labelStatus.setText('<html><head/><body><p>Status : <span style=" color:#00aa00;"> Save backup loaded.</span></p></body></html>')
            winsound.PlaySound('C:/Users/alifh/OneDrive/Desktop/py gui/save_Backup_Loaded.wav', winsound.SND_FILENAME)
        except:
            self.labelStatus.setText('<html><head/><body><p>Status : <span style=" color:#ff0000;"> Save backup not found.</span></p></body></html>')
    
    

if __name__ == "__main__":  


    def press_callback(key):
        if (key == keyboard.Key.f1):
            try:
                shutil.copy2(selectedSaveFile['path'] + '/' + selectedSaveFile['name'], selectedSaveFile['path'] + '\\backup_' + selectedSaveFile['name'])
                winsound.PlaySound('C:/Users/alifh/OneDrive/Desktop/py gui/save_Backup_Careated.wav', winsound.SND_FILENAME)
            except:
                print('Error')
        if (key == keyboard.Key.f2):
            try:
                shutil.copy2(selectedSaveFile['path'] + '\\backup_' + selectedSaveFile['name'], selectedSaveFile['path'] + '/' + selectedSaveFile['name'])
                winsound.PlaySound('C:/Users/alifh/OneDrive/Desktop/py gui/save_Backup_Loaded.wav', winsound.SND_FILENAME)
            except:
                print('Error')

    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()

    l = keyboard.Listener(on_press=press_callback)
    l.start()

    sys.exit(app.exec_())
