from PyQt5 import uic,QtWidgets
import mysql.connector
from time import sleep

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pedrodev123",
    database="banco"
)

def create_account():
    initial.close()
    create_user.show()


def create_conta():
    name = create_user.lineEdit.text()
    user_email = create_user.lineEdit_2.text()
    password = create_user.lineEdit_3.text()

    cursor = banco.cursor()
    cursor.execute("SELECT email FROM sistemas WHERE email ='{}'".format(user_email))
    email_SQL = cursor.fetchall()

    if email_SQL != user_email:
        comando_SQL = "INSERT INTO sistemas (name,email,password) VALUES (%s,%s,%s)"
        dados_client = (str(name),str(user_email),str(password))
        cursor.execute(comando_SQL, dados_client)
        banco.commit()
        create_user.label_5.setText("Registared User!")
        create_user.lineEdit.setText("")
        create_user.lineEdit_2.setText("")
        create_user.lineEdit_3.setText("")
    else:
        banco.close()
        create_user.label_5.setText("email already exists")
        sleep(0.5)
        create_user.lineEdit.setText("")
        create_user.lineEdit_2.setText("")
        create_user.lineEdit_3.setText("")

    banco.reconnect()

def back_initial():
    create_user.close()
    initial.show()

def log_in():
    initial.close()
    login.show()

def logar():
    email_user = login.lineEdit.text()
    password_user = login.lineEdit_2.text()
    
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT password FROM sistemas WHERE email ='{}'".format(email_user))
        password_SQL = cursor.fetchall()
    except:
        login.label_4.setText("mistake! Incorrect email or password.")

   
    if password_user == password_SQL[0][0]:
        sleep(1)
        home.show()
    else:
        login.label_4.setText("email or password wrong!")

    
    login.lineEdit.setText("")
    login.lineEdit_2.setText("")

    

def back_initial2():
    login.close()
    initial.show()

def page_creator():
    creator.show()

app=QtWidgets.QApplication([])
initial = uic.loadUi('page_initial.ui')
create_user = uic.loadUi('page_create_user.ui')
login = uic.loadUi('page_login.ui')
creator = uic.loadUi('page_creator.ui')
home = uic.loadUi('home.ui')


initial.pushButton.clicked.connect(create_account)
initial.pushButton_2.clicked.connect(log_in)
initial.pushButton_3.clicked.connect(page_creator)

create_user.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
create_user.pushButton.clicked.connect(create_conta)
create_user.pushButton_2.clicked.connect(back_initial)

login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
login.pushButton.clicked.connect(logar)
login.pushButton_2.clicked.connect(back_initial2)

initial.show()
app.exec()




# create table sistemas(
#   id INT NOT NULL AUTO_INCREMENT,
#   name VARCHAR(15),
#   email VARCHAR(35),
#   password VARCHAR(20),
#   PRIMARY KEY (id)
#  );