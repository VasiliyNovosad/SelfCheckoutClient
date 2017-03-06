# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
import selfcheckout_ui
import scanedform_ui
import requests
import os
import cv2

style = os.path.join(os.path.dirname(__file__), 'style.css')

class MyDialog(QWidget, scanedform_ui.Ui_Dialog):
    def __init__(self, parent_object):
        super(MyDialog, self).__init__(parent_object)
        self.scannedGood = None
        self.setupUi(self)
        self.cancelPushButton.clicked.connect(self.closeDialog)
        self.verifyPushButton.clicked.connect(self.verifyGood)
        self.cancelPushButton2.clicked.connect(self.closeDialog)
        self.verifyPushButton2.clicked.connect(self.verifyGood)
        self.cancelPushButton3.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.hide()

    def verifyGood(self):
        if self.scannedGood == None:
            return
        barcode = self.scannedGood['barcode']
        if self.verifiedGood(barcode):
            self.buttonsStackedWidget.setCurrentIndex(2)

            self.parent().add_good_to_cart(self.scannedGood)

        else:
            self.buttonsStackedWidget.setCurrentIndex(1)

    def verifiedGood(self, barcode):
        # TODO: add OpenCV frame check
        # return True
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        cv2.imwrite('images/tmp_frame.jpg', frame)
        # url = 'http://40.68.188.63:10002/upload2/' + str(barcode)
        url = 'http://localhost:10002/upload2/' + str(barcode)
        files = {'file': open('images/tmp_frame.jpg', 'rb')}
        r = requests.post(url, files=files)
        if r.status_code == 200:
            return True
        else:
            return False


class MyMainWindow(QMainWindow, selfcheckout_ui.Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.goods = []
        self.foundedGoods = []
        self.discountGoods = [
            {
                'image': 'images/991.jpg',
                'name': 'Bread',
                'description': "Calories, kcal: 242 Proteins: 8.1 Fats: 1.0 Carbohydrates: 48.8",
                'expiration': '2 days',
                'price': 1.29,
                'barcode': '1111'
            },
            {
                'image': 'images/9402-bananas.jpg',
                'name': 'Banana',
                'description': 'Proteins - 0.9g Fats - 0.1g Carbohydrates - 4.9g (including mono - and bioses - 3g) Food fibers (cellulose) - 1.3g',
                'expiration': '2 weeks',
                'price': 2.19,
                'barcode': '2222'
            },
            {
                'image': 'images/salami.jpg',
                'name': 'Salami',
                'description': "Proteins: 13g Fats: 57g Carbohydrates: 0.2",
                'expiration': '3 months',
                'price': 10.69,
                'barcode': '3333'
            },
            {
                'image': 'images/FrenchBaguette.jpg',
                'name': 'French Baguette',
                'description': "Calories, kcal: 242 Proteins: 8.1 Fats: 1.0 Carbohydrates: 48.8",
                'expiration': '2 days',
                'price': 1.29,
                'barcode': '4444'
            },
            {
                'image': 'images/img-fiche-silver-sardine-huile-vegetale.png',
                'name': 'Fish Sardine',
                'description': 'Calories, kcal: 242 Carbohydrates - 4.9g Fats: 1.0 Carbohydrates: 48.8',
                'expiration': '1 year',
                'price': 3.79,
                'barcode': '5555'
            },
            {
                'image': 'images/Lemon_easter_biscuits_hero_1d74c01d.jpg',
                'name': 'Lemon',
                'description': "Proteins - 0.9g Fats - 0.1g Carbohydrates - 4.9g (including mono - and bioses - 3g) Food fibers (cellulose) - 1.3g Pectin - 0.5g Organic acids - 5.7g Ashes - 0.5g",
                'expiration': '3 months',
                'price': 2.89,
                'barcode': '6666'
            },
            {
                'image': 'images/liquor-bottle-IARzFh-clipart.jpg',
                'name': 'Alcohol',
                'description': "Caloric content: 299 kcal Degree 40 Proteins: 0g Fats: 0g Carbohydrates: 40g",
                'expiration': '1 year',
                'price': 27.99,
                'barcode': '7777'
            },
            {
                'image': 'images/marinated-tomatoes-with-garlic.jpg',
                'name': 'Tomatoes',
                'description': 'Caloric content: 18 kcal Carbohydrates - 3.9g Sugars - 2.6g Dietary fiber - 1.2g Fat - 0.2g Protein - 0.9g',
                'expiration': '2 months',
                'price': 8.99,
                'barcode': '8888'
            },
            {
                'image': 'images/Swiss_Cheese_Garden_of_Eden_jpg.jpg',
                'name': 'Cheese',
                'description': "Water - 29.16g Proteins - 35.75g Fats - 25.83g Carbohydrates - 3.22g Ashes - 6.04g",
                'expiration': '2 months',
                'price': 19.99,
                'barcode': '9999'
            }
        ]
        self.setupUi(self)
        # self.barcodeLineEdit.keyboard_type = 'numeric'
        self.setStyleSheet(open(style).read())
        self.stackedWidget.setCurrentIndex(0)
        self.scannedDialog = MyDialog(self)
        self.scannedDialog.hide()

        self.startButton.clicked.connect(self.clickStartButton)
        self.findPushButton.clicked.connect(self.clickFindButton)
        self.delPushButton.clicked.connect(self.clickDelButton)
        self.barcodeLineEdit.editingFinished.connect(self.changeBarcode)
        # self.barcodeLineEdit.focusInEvent()
        self.shopingCartListWidget.itemClicked.connect(self.showProductInfo)
        self.foundedListWidget.itemClicked.connect(self.showFoundedProductInfo)
        self.discountPushButton1.clicked.connect(self.clickDiscountButton1)
        self.discountPushButton2.clicked.connect(self.clickDiscountButton2)
        self.discountPushButton3.clicked.connect(self.clickDiscountButton3)
        self.discountPushButton4.clicked.connect(self.clickDiscountButton4)
        self.discountPushButton5.clicked.connect(self.clickDiscountButton5)
        self.discountPushButton6.clicked.connect(self.clickDiscountButton6)
        self.discountPushButton7.clicked.connect(self.clickDiscountButton7)
        self.discountPushButton8.clicked.connect(self.clickDiscountButton8)
        self.discountPushButton9.clicked.connect(self.clickDiscountButton9)
        self.favoritesPushButton.clicked.connect(self.openScannedDialog)
        self.proceedPushButton.clicked.connect(self.clickProceedButton)
        self.cartPushButton.clicked.connect(self.clickCartButton)
        self.findLineEdit.textChanged.connect(self.foundLineTextEdited)
        self.goToPushButton.clicked.connect(self.clickGoTo)
        self.getGoods()
        self.discountImageLabel1.setPixmap(
            QPixmap(self.discountGoods[0]['image']).scaled(self.discountImageLabel1.width(), self.discountImageLabel1.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel2.setPixmap(
            QPixmap(self.discountGoods[1]['image']).scaled(self.discountImageLabel2.width(), self.discountImageLabel2.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel3.setPixmap(
            QPixmap(self.discountGoods[2]['image']).scaled(self.discountImageLabel3.width(), self.discountImageLabel3.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel4.setPixmap(
            QPixmap(self.discountGoods[3]['image']).scaled(self.discountImageLabel4.width(), self.discountImageLabel4.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel5.setPixmap(
            QPixmap(self.discountGoods[4]['image']).scaled(self.discountImageLabel5.width(), self.discountImageLabel5.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel6.setPixmap(
            QPixmap(self.discountGoods[5]['image']).scaled(self.discountImageLabel6.width(), self.discountImageLabel6.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel7.setPixmap(
            QPixmap(self.discountGoods[6]['image']).scaled(self.discountImageLabel7.width(), self.discountImageLabel7.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel8.setPixmap(
            QPixmap(self.discountGoods[7]['image']).scaled(self.discountImageLabel8.width(), self.discountImageLabel8.height(),
                                                           Qt.KeepAspectRatio))
        self.discountImageLabel9.setPixmap(
            QPixmap(self.discountGoods[8]['image']).scaled(self.discountImageLabel9.width(), self.discountImageLabel9.height(),
                                                           Qt.KeepAspectRatio))
        self.centralwidget.showFullScreen()
        # self.showFullScreen()

    def openScannedDialog(self):
        self.scannedDialog = MyDialog(self)
        self.scannedDialog.exec_()

    def clickStartButton(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.barcodeLineEdit.setFocus()

    def clickProceedButton(self):
        self.stackedWidget.setCurrentIndex(0)
        self.shopingCartListWidget.clear()
        self.goods = []
        self.updateTotal()

    def clickCartButton(self):
        self.stackedWidget_3.setCurrentIndex(1)

    def clickFindButton(self):
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
        self.updateTotal()

    def updateTotal(self):
        total = 0
        for good in self.goods:
            total += good['price'] * good['count']
        self.shopingCartTotalSumLabel.setText(str(total) + u"€")

    def showProductInfo(self):
        selected_index = self.shopingCartListWidget.currentRow()
        if selected_index >= 0:
            selected_item = self.goods[selected_index]
            self.nameGoodLabel.setText(selected_item['name'])
            self.descriptionGoodLabel.setText(selected_item['description'])
            self.expirationGoodLabel.setText('Until ' + selected_item['expiration'])
            img = QPixmap(selected_item['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio)
            self.imageGoodLabel.setPixmap(img)

    def showFoundedProductInfo(self):
        selected_index = self.foundedListWidget.currentRow()
        if selected_index >= 0:
            selected_item = self.foundedGoods[selected_index]
            self.nameGoodLabel.setText(selected_item['name'])
            self.descriptionGoodLabel.setText(selected_item['description'])
            self.expirationGoodLabel.setText('Until ' + selected_item['expiration'])
            img = QPixmap(selected_item['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(),
                                                         Qt.KeepAspectRatio)
            self.imageGoodLabel.setPixmap(img)

    def clickDiscountButton1(self):
        self.nameGoodLabel.setText(self.discountGoods[0]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[0]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[0]['expiration'])
        self.imageGoodLabel.setScaledContents(False)
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[0]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                                  self.mapGraphicsView.height(),
                                                                                  Qt.KeepAspectRatio))

    def clickDiscountButton2(self):
        self.nameGoodLabel.setText(self.discountGoods[1]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[1]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[1]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[1]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def clickDiscountButton3(self):
        self.nameGoodLabel.setText(self.discountGoods[2]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[2]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[2]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[2]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def clickDiscountButton4(self):
        self.nameGoodLabel.setText(self.discountGoods[3]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[3]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[3]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[3]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def clickDiscountButton5(self):
        self.nameGoodLabel.setText(self.discountGoods[4]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[4]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[4]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[4]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def clickDiscountButton6(self):
        self.nameGoodLabel.setText(self.discountGoods[5]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[5]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[5]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[5]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def clickDiscountButton7(self):
        self.nameGoodLabel.setText(self.discountGoods[6]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[6]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[6]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[6]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def clickDiscountButton8(self):
        self.nameGoodLabel.setText(self.discountGoods[7]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[7]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[7]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[7]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def clickDiscountButton9(self):
        self.nameGoodLabel.setText(self.discountGoods[8]['name'])
        self.descriptionGoodLabel.setText(self.discountGoods[8]['description'])
        self.expirationGoodLabel.setText(self.discountGoods[8]['expiration'])
        self.imageGoodLabel.setPixmap(QPixmap(self.discountGoods[8]['image']).scaled(self.imageGoodLabel.width(), self.imageGoodLabel.height(), Qt.KeepAspectRatio))
        self.mapGraphicsView.setMovie(None)
        self.mapGraphicsView.setPixmap(
            QPixmap("images/Plan Superm 3.00_00_00_00.Still001.png").scaled(self.mapGraphicsView.width(),
                                                                            self.mapGraphicsView.height(),
                                                                            Qt.KeepAspectRatio))

    def getGoods(self):
        # response = requests.get('http://40.68.188.63:10002/wares')
        # self.all_goods = response.json()['wares']
        response = requests.get('http://localhost:10002/goods')
        self.all_goods = response.json()['goods']
        # self.all_goods = [t for t in self.discountGoods if True]
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
            scanedGood = selected[0]
            self.scannedDialog.scannedGood = scanedGood
            self.scannedDialog.scanedGoodNameLabel.setText(scanedGood['name'])
            self.scannedDialog.scanedGoodPriceLabel.setText(str(scanedGood['price']) + u"€")
            self.scannedDialog.scanedGoodDescriptionLabel.setText(scanedGood['description'])
            self.scannedDialog.scanedGoodExpirationLabel.setText(scanedGood['expiration'])
            self.scannedDialog.scanedGoodImageLabel.setPixmap(
                QPixmap(scanedGood['image']).scaled(self.scannedDialog.scanedGoodImageLabel.width(),
                                                               self.scannedDialog.scanedGoodImageLabel.height(),
                                                               Qt.KeepAspectRatio))
            self.scannedDialog.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.scannedDialog.move(400, 400)
            self.scannedDialog.buttonsStackedWidget.setCurrentIndex(0)
            self.scannedDialog.show()

            # self.goods.append(selected[0])
            # self.shopingCartListWidget.addItem(selected[0]['name'])
        # print self.goods

    def add_good_to_cart(self, scannedGood):
        ind = 0
        flag = False
        founded = 0
        for good in self.goods:
            if good['barcode'] == scannedGood['barcode']:
                flag = True
                founded = ind
            ind += 1
        if flag:
            self.goods[founded]['count'] += 1
            self.shopingCartListWidget.clear()
            for good in self.goods:
                self.shopingCartListWidget.addItem(good['name'] + ': ' + str(good['price']) + u"€" + ' x ' + str(good['count']) + ' = ' + str(good['count'] * good['price']) + u"€")
        else:
            self.goods.append(scannedGood)
            self.goods[-1]['count'] = 1
            self.shopingCartListWidget.addItem(scannedGood['name'] + ': ' + str(scannedGood['price']) + u"€" + ' x 1 = ' + str(scannedGood['price']) + u"€")
        self.updateTotal()

    def foundLineTextEdited(self):
        self.found_goods(self.findLineEdit.text())

    def clickGoTo(self):
        movie = QMovie("images/Plan Superm_1.gif")
        self.mapGraphicsView.setMovie(movie)
        movie.start()

    def found_goods(self, found_filter):
        if found_filter == '':
            self.foundedGoods = []
            self.foundedListWidget.clear()
        else:
            self.foundedGoods = [t for t in self.all_goods if t['name'].lower().find(found_filter.lower()) >= 0]
            self.foundedListWidget.clear()
            for good in self.foundedGoods:
                itm = QListWidgetItem(good['name'] + '    ' + str(good['price']) + u"€")
                itm.setIcon(QIcon(good['image']))
                self.foundedListWidget.addItem(itm)


if __name__ == '__main__':
    app = QApplication([])
    w = MyMainWindow()

    w.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    w.show()
    # w.showFullScreen()
    app.exec_()