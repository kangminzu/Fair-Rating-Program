import sys
from PyQt5.QtWidgets import *
import math
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#별점 선택 화면
class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        
        main_layout = QVBoxLayout()
        
        td_month = str(datetime.now().date())[5:7]
        url = f'http://icpa.icehs.kr/foodlist.do?year=2022&month={td_month}&m=070306&s=icpa'

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            title = str(soup.select_one('#con_body > div.tb_base_box.web_box > table > tbody > tr > td.today > a > ul'))
            new_title = title.replace('<br/>','''
        ''')
            today=new_title[5:-4]
            today=today.split("\n")
            
        for i in range(len(today)-3):
            food=QLabel(today[i])
            main_layout.addWidget(food)
        
        layout_starpoint = QFormLayout() 
        
        starinput_layout = QHBoxLayout()
        
        self.starinput = QHBoxLayout()

        #별점 위젯
        self.star1_radiobtn = QRadioButton()
        self.star2_radiobtn = QRadioButton()
        self.star3_radiobtn = QRadioButton()
        self.star4_radiobtn = QRadioButton()
        self.star5_radiobtn = QRadioButton()

        self.star1_radiobtn.setAutoExclusive(False)
        self.star2_radiobtn.setAutoExclusive(False)
        self.star3_radiobtn.setAutoExclusive(False)
        self.star4_radiobtn.setAutoExclusive(False)
        self.star5_radiobtn.setAutoExclusive(False)
        
        self.staroutput = QLabel()
        self.startotal = QLabel()
        
        check_btn = QPushButton("입력")
        
        starinput_layout.addWidget(self.star1_radiobtn)
        starinput_layout.addWidget(self.star2_radiobtn)
        starinput_layout.addWidget(self.star3_radiobtn)
        starinput_layout.addWidget(self.star4_radiobtn)
        starinput_layout.addWidget(self.star5_radiobtn)
        
        starinput_layout.addWidget(check_btn)
        
        self.star1_radiobtn.clicked.connect(self.radiobutton1_clicked)
        self.star2_radiobtn.clicked.connect(self.radiobutton2_clicked)
        self.star3_radiobtn.clicked.connect(self.radiobutton3_clicked)
        self.star4_radiobtn.clicked.connect(self.radiobutton4_clicked)
        self.star5_radiobtn.clicked.connect(self.radiobutton5_clicked)
        
        check_btn.clicked.connect(self.check_btn_clicked)
        
        layout_starpoint.addRow("별점 입력 : ",starinput_layout)
        layout_starpoint.addRow("별점 : ",self.staroutput)
        layout_starpoint.addRow("전체 별점 : ",self.startotal)
        
        main_layout.addLayout(layout_starpoint)
        self.setLayout(main_layout)
        self.show()
    
    #확인버튼 클릭
    def check_btn_clicked(self):
        self.staroutput.setText(str(self.starp))
        
        f = open("starpoint.txt", mode="r", encoding='utf-8')
        f_r = f.readlines()
        
        if player_num > len(f_r):
            f_r.append(str(self.starp)+'/')
            f_l = str(self.starp)
            f.close()
            
        else:
            f_rmem = f_r[player_num-1]
            f_r.pop(player_num-1)
            f_rmem = f_rmem.strip('\n')
            f_rmem += (str(self.starp)+'/')
            f_l = f_rmem.split('/')
            f_l.pop()
            f_r.insert(player_num-1,f_rmem)
            f.close()
        
        f = open("starpoint.txt", mode = "w", encoding = 'utf-8')
        
        for item in f_r:
            item = item.strip('\n')
            f.write(item)
            f.write('\n')
        f.close()
        
        total = 0
        number = 0
        ave = 0
        
        for i in f_l:
            number += 1
            
            if number == len(f_l):
                ave = total/(number)
                if ave != 0:
                    A = int(i)/ave
                else : 
                    A = int(i)
                
            else:
                total += int(i)
                
        k = math.log(A,5)
        
        total = total+3+2*k
        total = total / len(f_l)
        total = round(total,2)
        self.startotal.setText(str(total))
        
    #별점 입력    
    def radiobutton1_clicked(self):
        if  not self.star1_radiobtn.isChecked() and self.starp==1:
            self.star1_radiobtn.setChecked(False)
            self.star2_radiobtn.setChecked(False)
            self.star3_radiobtn.setChecked(False)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        else:
            self.star1_radiobtn.setChecked(True)
            self.star2_radiobtn.setChecked(False)
            self.star3_radiobtn.setChecked(False)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        self.starp=1
        
    def radiobutton2_clicked(self):
        if  not self.star2_radiobtn.isChecked() and self.starp==2:
            self.star1_radiobtn.setChecked(False)
            self.star2_radiobtn.setChecked(False)
            self.star3_radiobtn.setChecked(False)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        else:
            self.star1_radiobtn.setChecked(True)
            self.star2_radiobtn.setChecked(True)
            self.star3_radiobtn.setChecked(False)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        self.starp=2
        
    def radiobutton3_clicked(self):
        if  not self.star3_radiobtn.isChecked() and self.starp==3:
            self.star1_radiobtn.setChecked(False)
            self.star2_radiobtn.setChecked(False)
            self.star3_radiobtn.setChecked(False)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        else:
            self.star1_radiobtn.setChecked(True)
            self.star2_radiobtn.setChecked(True)
            self.star3_radiobtn.setChecked(True)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        self.starp=3
        
    def radiobutton4_clicked(self):
        if  not self.star4_radiobtn.isChecked() and self.starp==4:
            self.star1_radiobtn.setChecked(False)
            self.star2_radiobtn.setChecked(False)
            self.star3_radiobtn.setChecked(False)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        else:
            self.star1_radiobtn.setChecked(True)
            self.star2_radiobtn.setChecked(True)
            self.star3_radiobtn.setChecked(True)
            self.star4_radiobtn.setChecked(True)
            self.star5_radiobtn.setChecked(False)
        self.starp=4
        
    def radiobutton5_clicked(self):
        if  not self.star5_radiobtn.isChecked() and self.starp==5:
            self.star1_radiobtn.setChecked(False)
            self.star2_radiobtn.setChecked(False)
            self.star3_radiobtn.setChecked(False)
            self.star4_radiobtn.setChecked(False)
            self.star5_radiobtn.setChecked(False)
        else:
            self.star1_radiobtn.setChecked(True)
            self.star2_radiobtn.setChecked(True)
            self.star3_radiobtn.setChecked(True)
            self.star4_radiobtn.setChecked(True)
            self.star5_radiobtn.setChecked(True)
        self.starp=5

#로그인 화면(시작 화면)        
class loginpage(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        
        login_layout = QVBoxLayout()
        
        ID_layout = QHBoxLayout()
        PW_layout = QHBoxLayout()
        extra_layout = QHBoxLayout()
        
        ID_name = QLabel("아이디   ")
        PW_name = QLabel("비밀번호")
        
        self.ID_input = QLineEdit()
        self.PW_input = QLineEdit()
        
        login_btn = QPushButton("로그인")
        
        login_btn.clicked.connect(self.login_btn_clicked)
        
        new_login_btn = QPushButton("회원가입")
        
        new_login_btn.clicked.connect(self.new_login_btn_clicked)
        
        ID_layout.addWidget(ID_name)
        ID_layout.addWidget(self.ID_input)
        
        PW_layout.addWidget(PW_name)
        PW_layout.addWidget(self.PW_input)
        
        extra_layout.addWidget(new_login_btn)
        
        login_layout.addLayout(ID_layout)
        login_layout.addLayout(PW_layout)
        login_layout.addWidget(login_btn)
        login_layout.addLayout(extra_layout)
        
        self.setLayout(login_layout)
        self.setWindowTitle("로그인창")
        self.show()
        
    def login_btn_clicked(self): #로그인하기
        fm = open("member.txt", mode = "r", encoding = 'utf-8')
        
        global player_num
        player_num=0
        
        for line in fm:
            
            player_num+=1
            print(player_num)
            
            find = line.strip('\n')
            id,pw = find.split(',')
            
            if id == self.ID_input.text() and pw == self.PW_input.text():
                self.close()
                self.mainpage = Main()
                self.mainpage.show()
                break 
            
            elif id == self.ID_input.text() and pw != self.PW_input.text():
                self.close()
                self.notice = nopw()
                self.notice.show()
                break
            
        else: 
            self.close()
            self.mainpage = nomem()
            self.mainpage.show()
            
    def new_login_btn_clicked(self): #"회원가입"버튼 누르면 회원가입 창으로 가기
        self.hide()
        self.second = new_login()
        self.second.show()
        
class new_login(QDialog,QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def initUI(self):
        new_login_layout = QVBoxLayout()
        
        newID_layout = QHBoxLayout()
        newPW_layout = QHBoxLayout()
        newextra_layout = QHBoxLayout()
        
        newID_name = QLabel("아이디   ")
        newPW_name = QLabel("비밀번호")
        
        self.new_ID_input = QLineEdit()
        self.new_PW_input = QLineEdit()
        
        newlogin_btn = QPushButton("회원가입")
        newback_btn = QPushButton("로그인창으로 가기")
        
        newlogin_btn.clicked.connect(self.login_btn_clicked)
        newback_btn.clicked.connect(self.back_btn_clicked)
        
        newID_layout.addWidget(newID_name)
        newID_layout.addWidget(self.new_ID_input)
        
        newPW_layout.addWidget(newPW_name)
        newPW_layout.addWidget(self.new_PW_input)
        
        new_login_layout.addLayout(newID_layout)
        new_login_layout.addLayout(newPW_layout)
        new_login_layout.addWidget(newlogin_btn)
        new_login_layout.addLayout(newextra_layout)
        new_login_layout.addWidget(newback_btn)
        
        self.setLayout(new_login_layout)
        self.setWindowTitle("회원가입창")
        
    def back_btn_clicked(self): #"로그인창으로 가기" 버튼 누르면 창닫기
        self.close()
        self.first = loginpage()
        self.first.show()
    
    def login_btn_clicked(self,member): #회원가입하기
        
        if self.new_ID_input.text() == "" or self.new_PW_input.text() == "":
            self.close()
            self.errormes = nonotice()
            self.errormes.show()
            
        else :
            fm = open("member.txt", mode = 'a', encoding = 'utf-8')
            fm.write(str(self.new_ID_input.text())+ ","+ str(self.new_PW_input.text()) + "\n")
            fm.close()
            
            self.close()
            self.first = loginpage()
            self.first.show()

class nonotice (QDialog,QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        self.show()
    
    def initui(self):
        main_layout = QHBoxLayout()
        
        no = QLabel("아이디 혹은 비밀번호를 입력해주세요")
        check_btn = QPushButton("확인")
        
        check_btn.clicked.connect(self.check_btn_clicked)
        
        main_layout.addWidget(no)
        main_layout.addWidget(check_btn)
        
        self.setLayout(main_layout)
        self.setWindowTitle("안내")
        
    def check_btn_clicked(self):
        self.close()    
        self.second = new_login()
        self.second.show()
                
class notice (QDialog,QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        self.show()
    
    def initui(self):
        main_layout = QHBoxLayout()
        
        no = QLabel("중복된 아이디입니다")
        check_btn = QPushButton("확인")
        
        check_btn.clicked.connect(self.check_btn_clicked)
        
        main_layout.addWidget(no)
        main_layout.addWidget(check_btn)
        
        self.setLayout(main_layout)
        self.setWindowTitle("안내")
        
    def check_btn_clicked(self):
        self.close()    
        self.second = new_login()
        self.second.show()

class nopw (QDialog,QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        self.show()
    
    def initui(self):
        main_layout = QHBoxLayout()
        
        no = QLabel("잘못된 비밀번호입니다.")
        check_btn = QPushButton("확인")
        
        check_btn.clicked.connect(self.check_btn_clicked)
        
        main_layout.addWidget(no)
        main_layout.addWidget(check_btn)
        
        self.setLayout(main_layout)
        self.setWindowTitle("안내")
        
    def check_btn_clicked(self):
        self.close()    
        self.second = loginpage()
        self.second.show()
        
class nomem (QDialog,QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        self.show()
    
    def initui(self):
        main_layout = QHBoxLayout()
        
        no = QLabel("존재하지 않는 회원 정보입니다.")
        check_btn = QPushButton("확인")
        
        check_btn.clicked.connect(self.check_btn_clicked)
        
        main_layout.addWidget(no)
        main_layout.addWidget(check_btn)
        
        self.setLayout(main_layout)
        self.setWindowTitle("안내")
        
    def check_btn_clicked(self):
        self.close()    
        self.second = loginpage()
        self.second.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=loginpage()
    sys.exit(app.exec_())
