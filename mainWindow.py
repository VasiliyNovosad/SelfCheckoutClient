# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
import selfcheckout_ui
import requests
import os

style = os.path.join(os.path.dirname(__file__), 'style.css')

class myMainWindow(QMainWindow, selfcheckout_ui.Ui_MainWindow):
    def __init__(self):
        super(myMainWindow, self).__init__()
        self.goods = []
        self.discountGoods = [
            {
                'image': '',
                'name': 'Bread',
                'description': "Calories, kcal: 242\nProteins: 8.1\nFats: 1.0\nCarbohydrates: 48.8",
                'expiration': '2 days',
                'price': 1.29
            },
            {
                'image': '',
                'name': 'Banana',
                'description': 'Banana',
                'expiration': '2 weeks',
                'price': 2.19
            },
            {
                'image': '',
                'name': 'Salami',
                'description': "Proteins: 13 g\nFats: 57 g\nCarbohydrates: 0.2",
                'expiration': '3 months',
                'price': 10.69
            },
            {
                'image': '',
                'name': 'French bread',
                'description': "Calories, kcal: 242\nProteins: 8.1\nFats: 1.0\nCarbohydrates: 48.8",
                'expiration': '2 days',
                'price': 1.29
            },
            {
                'image': '',
                'name': 'Fish conserve',
                'description': 'Fish conserve',
                'expiration': '1 year',
                'price': 3.79
            },
            {
                'image': '',
                'name': 'Lemon',
                'description': "Proteins - 0.9 g\nFats - 0.1 g\nCarbohydrates - 4.9 g (including mono - and bioses – 3 g)\nFood fibers (cellulose) – 1.3 g\nPectin - 0.5 g\nOrganic acids - 5.7 g\nAshes - 0.5 g",
                'expiration': '3 months',
                'price': 2.89
            },
            {
                'image': '',
                'name': 'Alcohol',
                'description': "Caloric content: 299 kcal.\nDegree 40\nProteins: 0 g.\nFats: 0 g.\nCarbohydrates: 40 g.",
                'expiration': '1 year',
                'price': 27.99
            },
            {
                'image': '',
                'name': 'Tomatoes',
                'description': 'Tomatoes',
                'expiration': '2 months',
                'price': 8.99
            },
            {
                'image': '',
                'name': 'Cheese',
                'description': "Water - 29.16 g\nProteins - 35.75 g\nFats - 25.83 g\nCarbohydrates - 3.22 g\nAshes - 6.04 g",
                'expiration': '2 months',
                'price': 19.99
            }
        ]
        self.setupUi(self)
        self.setStyleSheet(open(style).read())
        self.stackedWidget.setCurrentIndex(0)
        self.startButton.clicked.connect(self.clickStartButton)
        self.findPushButton.clicked.connect(self.clickFindButton)
        self.delPushButton.clicked.connect(self.clickDelButton)
        self.barcodeLineEdit.editingFinished.connect(self.changeBarcode)
        self.shopingCartListWidget.itemClicked.connect(self.showProductInfo)
        self.discountPushButton1.clicked.connect(self.clickDiscountButton1)
        self.discountPushButton2.clicked.connect(self.clickDiscountButton2)
        self.discountPushButton3.clicked.connect(self.clickDiscountButton3)
        self.discountPushButton4.clicked.connect(self.clickDiscountButton4)
        self.discountPushButton5.clicked.connect(self.clickDiscountButton5)
        self.discountPushButton6.clicked.connect(self.clickDiscountButton6)
        self.discountPushButton7.clicked.connect(self.clickDiscountButton7)
        self.discountPushButton8.clicked.connect(self.clickDiscountButton8)
        self.discountPushButton9.clicked.connect(self.clickDiscountButton9)
        self.getGoods()

    def clickStartButton(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)

    def clickFindButton(self):
        self.setStyleSheet(open(style).read())
        if self.stackedWidget_2.currentIndex() == 0:
            self.stackedWidget_2.setCurrentIndex(1)
        else:
            self.stackedWidget_2.setCurrentIndex(0)

    def clickDelButton(self):
        selected_item = self.shopingCartListWidget.currentRow()
        if selected_item != -1 and len(self.goods) > 0:
            item = self.shopingCartListWidget.takeItem(selected_item)
            item = None
            self.goods.pop(selected_item)

    def showProductInfo(self):
        selected_index = self.shopingCartListWidget.currentRow()
        if selected_index >= 0:
            selected_item = self.goods[selected_index]
            self.nameGoodLabel.setText(selected_item['name'])
            # self.descriptionGoodLabel.setText(selected_item['description'])
            # self.expirationGoodLabel.setText(selected_item['expiration'])
            self.descriptionGoodLabel.setText(selected_item['name'])
            self.expirationGoodLabel.setText(selected_item['name'])
            self.imageGoodLabel.setPixmap(QPixmap('/home/tk/PycharmProjects/SelfCheckoutOnGo/app/static/upload/wares/1/1.jpg'))

    def clickDiscountButton1(self):
        self.nameGoodLabel.setText(self.discountGoods[0]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[0]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[0]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel1.pixmap())

    def clickDiscountButton2(self):
        self.nameGoodLabel.setText(self.discountGoods[1]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[1]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[1]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel2.pixmap())

    def clickDiscountButton3(self):
        self.nameGoodLabel.setText(self.discountGoods[2]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[2]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[2]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel3.pixmap())

    def clickDiscountButton4(self):
        self.nameGoodLabel.setText(self.discountGoods[3]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[3]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[3]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel4.pixmap())

    def clickDiscountButton5(self):
        self.nameGoodLabel.setText(self.discountGoods[4]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[4]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[4]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel5.pixmap())

    def clickDiscountButton6(self):
        self.nameGoodLabel.setText(self.discountGoods[5]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[5]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[5]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel6.pixmap())

    def clickDiscountButton7(self):
        self.nameGoodLabel.setText(self.discountGoods[6]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[6]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[6]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel7.pixmap())

    def clickDiscountButton8(self):
        self.nameGoodLabel.setText(self.discountGoods[7]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[7]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[7]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel8.pixmap())

    def clickDiscountButton9(self):
        self.nameGoodLabel.setText(self.discountGoods[8]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[8]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[8]['expiration'])
        self.imageGoodLabel.setPixmap(self.discountImageLabel9.pixmap())

    def getGoods(self):
        response = requests.get('http://40.68.188.63:10002/wares')
        self.all_goods = response.json()['wares']
        self.goods = []
        print(self.all_goods)

    def changeBarcode(self):
        barcode = self.barcodeLineEdit.text()
        self.barcodeLineEdit.setText('')
        if barcode == '':
            return
        self.addGood(barcode)

    def addGood(self, barcode):
        selected = [t for t in self.all_goods if t['barcode'] == barcode]
        if len(selected) > 0:
            self.goods.append(selected[0])
            self.shopingCartListWidget.addItem(selected[0]['name'])
        print self.goods


if __name__ == '__main__':
    app = QApplication([])
    w = myMainWindow()
    w.show()
    # w.showFullScreen()
    app.exec_()