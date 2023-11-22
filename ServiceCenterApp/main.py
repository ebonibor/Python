import sys
from db_logic import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сервисный Центр")
        self.setGeometry(100, 100, 600, 400)  # X, Y, Width, Height

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Файл")
        self.edit_menu = self.menu.addMenu("Редактировать")
        self.view_menu = self.menu.addMenu("Просмотреть")

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

        client_action_1 = QAction("Клиенты", self)
        client_action_1.triggered.connect(self.openClientForm)
        self.edit_menu.addAction(client_action_1)

        client_action_2 = QAction("Клиенты", self)
        client_action_2.triggered.connect(self.viewClients)
        self.view_menu.addAction(client_action_2)


    def openClientForm(self):
        self.client_form = ClientForm()
        self.client_form.show()

    def viewClients(self):
        self.client_view = ClientView()
        self.client_view.show()

class ClientForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Имя:")
        self.name_input = QLineEdit()
        self.surname_label = QLabel("Фамилия:")
        self.surname_input = QLineEdit()
        self.phone_label = QLabel("Телефон:")
        self.phone_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.submit_button = QPushButton("Добавить клиента")
        self.submit_button.clicked.connect(self.addClient)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.submit_button)

        # Установка layout для этого виджета
        self.setLayout(layout)

    def addClient(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        contact_number = self.phone_input.text()
        email = self.email_input.text()
        if name:
            try:
                add_client(name, surname, contact_number, email)
                QMessageBox.information(self, "Успех", "Клиент успешно добавлен")
                self.name_input.clear()
                self.surname_input.clear()
                self.phone_input.clear()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось добавить клиента: {str(e)}")
        else:
            QMessageBox.critical(self, "Ошибка", "Имя клиента не может быть пустым")

class ClientView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadClients()

    def initUI(self):
        layout = QVBoxLayout()

        self.clients_table = QTableWidget()
        self.clients_table.setColumnCount(5)
        self.clients_table.setHorizontalHeaderLabels(["ID", "Имя", "Фамилия", "Телефон", "Email"])
        layout.addWidget(self.clients_table)
        self.setLayout(layout)

    def loadClients(self):
        clients = get_clients()
        self.clients_table.setRowCount(len(clients))
        for i, client in enumerate(clients):
            self.clients_table.insertRow(i)
            for j, item in enumerate(client):
                self.clients_table.setItem(i, j, QTableWidgetItem(str(item)))

        self.clients_table.resizeColumnsToContents()

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
