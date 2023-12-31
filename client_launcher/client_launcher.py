import sys
import time

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase, QFont


from class_client.class_client import ClientApp
from main_code.front.client_controller import ClientController

def main():
    app = QApplication(sys.argv)

    # 폰트
    fontDB = QFontDatabase()
    fontDB.addApplicationFont("../main_code/front/font/NanumSquareNeo-aLt.ttf")
    fontDB.addApplicationFont("../main_code/front/font/NanumSquareNeo-bRg.ttf")
    fontDB.addApplicationFont("../main_code/front/font/NanumSquareNeo-cBd.ttf")
    fontDB.addApplicationFont("../main_code/front/font/NanumSquareNeo-dEb.ttf")
    fontDB.addApplicationFont("../main_code/front/font/NanumSquareNeo-eHv.ttf")
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False


    client_object = ClientApp()
    client_controller = ClientController(client_object)
    client_controller.run()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



