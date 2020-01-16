# coding: utf-8

# CODE Made by NAM O KIM, MIN BAEK KIM
# copyright by Geekble co.. ltd
# last update 2020.01.15
#
# For ALS

import sys
import requests
import csv
from gtts import gTTS
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from tempfile import TemporaryFile
from pygame import mixer
from datetime import datetime

target_url = ''

flags = [0, 0, 0]

titleList = []
contentList = []
userList = []
numberList = []

class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("UI/GeekUI(V3).ui", self) # ui파일을 로드
        self.setWindowTitle('GeekTracker') # 프로그램 제목 설정
        self.setWindowIcon(QIcon('Spec/geekblelogo.jpg')) # 프로그램 로고 설정
        self.ui.show() # 설정된 UI를 보여주기

        self.ReadData() # csv 파일의 데이터를 불러오는 함수
        self.SetButton() # 각 버튼의 기능을 부여하는 함수
        print('Program Setting Completed!')

    def ReadData(self):
        CustomFile = open('Custom/Menu.csv', 'r', encoding='utf-8-sig')
        UserFile = open('Custom/User.csv', 'r', encoding='utf-8-sig')
        KeyFile = open('Custom/Key.csv', 'r', encoding='utf-8-sig')

        customRdr = csv.reader(CustomFile)
        userRdr = csv.reader(UserFile)
        keyRdr = csv.reader(KeyFile)
        
        for line in customRdr: # 버튼의 제목과 메세지 불러오기
            titleList.append(line[1])
            contentList.append(line[2])
        
        for line2 in userRdr: # 사용자의 이름과 전화번호 불러오기
            userList.append(line2[0])
            numberList.append(line2[1])

        for line3 in keyRdr: # Key값 불러오기
            global target_url
            target_url = 'https://maker.ifttt.com/trigger/signal/with/key/'+line3[0]

        CustomFile.close()
        UserFile.close()
        KeyFile.close()

    def SetButton(self):
        self.push01.setText(titleList[0])
        self.push02.setText(titleList[1])
        self.push03.setText(titleList[2])
        self.push04.setText(titleList[3])
        self.push05.setText(titleList[4])
        self.push06.setText(titleList[5])
        self.push07.setText(titleList[6])
        self.push08.setText(titleList[7])
        self.push09.setText(titleList[8])
        self.push10.setText(titleList[9])
        self.push11.setText(titleList[10])
        self.push12.setText(titleList[11])
        self.push13.setText(titleList[12])
        self.push14.setText(titleList[13])
        self.push15.setText(titleList[14])
        self.push16.setText(titleList[15])
        self.push17.setText(titleList[16])
        self.push18.setText(titleList[17])
        self.push19.setText(titleList[18])
        self.push20.setText(titleList[19])
        self.push21.setText(titleList[20])
        self.push22.setText(titleList[21])
        self.push23.setText(titleList[22])
        self.push24.setText(titleList[23])
        self.check01.setText(userList[0])
        self.check02.setText(userList[1])
        self.check03.setText(userList[2])

    def Send_SMS_TTS(self, _string):
        isSendSMS = True
        string = _string  # SMS TTS 될 문장

        if not string.strip():
            string = "메세지를 입력해주세요"
            isSendSMS = False

        # 현재 시간 및 메세지를 출력
        now = datetime.now()
        self.textBrowser.append('%s:%s %s' % (now.hour, now.minute, string))

        # 메세지를 TTS 음성 파일로 변환 후 재생
        tts = gTTS(text=string, lang='ko') # 스트링을 mp3 파일로
        mixer.init()      # mp3 파일 재생 초기화
        f = TemporaryFile() # 임시 저장소 생성
        tts.write_to_fp(f) # mp3 파일을 임시 저장소에 올려 놓음
        f.seek(0)
        mixer.music.load(f) 
        mixer.music.play() # mp3 재생

        if not isSendSMS:
            return

        for i in range(len(flags)):
            if flags[i] == 1:
                r = requests.post(target_url, data={"value1": string,"value2": numberList[i]})
                print(i+1,"번 sms 전송!")

    @pyqtSlot()
    def slot26(self):
        string = self.lineEdit.text()
        self.lineEdit.clear()
        self.Send_SMS_TTS(string)

    def SetFlag(self, _number, _state):
        flags[_number-1] = 1 if _state else 0
        print("flag",_number,": ",flags[_number-1])

    @pyqtSlot(bool)
    def slot27(self, state):
        self.SetFlag(1,state)

    @pyqtSlot(bool)
    def slot28(self, state):
        self.SetFlag(2,state)

    @pyqtSlot(bool)
    def slot29(self, state):
        self.SetFlag(3,state)

    # === PushButton ===
    @pyqtSlot()
    def slot1(self):
        print('1번 출력')
        string = contentList[0]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot2(self):
        print('2번 출력')
        string = contentList[1]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot3(self):
        print('3번 출력')
        string = contentList[2]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot4(self):
        print('4번 출력')
        string = contentList[3]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot5(self):
        print('5번 출력')
        string = contentList[4]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot6(self):
        print('6번 출력')
        string = contentList[5]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot7(self):
        print('7번 출력')
        string = contentList[6]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot8(self):
        print('8번 출력')
        string = contentList[7]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot9(self):
        print('9번 출력')
        string = contentList[8]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot10(self):
        print('10번 출력')
        string = contentList[9]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot11(self):
        print('11번 출력')
        string = contentList[10]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot12(self):
        print('12번 출력')
        string = contentList[11]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot13(self):
        print('13번 출력')
        string = contentList[12]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot14(self):
        print('14번 출력')
        string = contentList[13]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot15(self):
        print('15번 출력')
        string = contentList[14]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot16(self):
        print('16번 출력')
        string = contentList[15]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot17(self):
        print('17번 출력')
        string = contentList[16]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot18(self):
        print('18번 출력')
        string = contentList[17]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot19(self):
        print('19번 출력')
        string = contentList[18]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot20(self):
        print('20번 출력')
        string = contentList[19]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot21(self):
        print('21번 출력')
        string = contentList[20]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot22(self):
        print('22번 출력')
        string = contentList[21]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot23(self):
        print('23번 출력')
        string = contentList[22]
        self.Send_SMS_TTS(string)

    @pyqtSlot()
    def slot24(self):
        print('24번 출력')
        string = contentList[23]
        self.Send_SMS_TTS(string)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Form()
    sys.exit(app.exec_())