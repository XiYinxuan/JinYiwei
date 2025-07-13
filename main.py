import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QMenuBar, QMenu, QAction
from PyQt5.QtCore import Qt
from system_monitor import SystemMonitor
from malware_scanner import MalwareScanner

class SecuritySoftware(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("锦衣卫安全软件")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu_bar()
        
        # 设置中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignTop)

        # 创建标签页控件
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget, 1)

        # 添加系统监控标签页
        self.system_monitor = SystemMonitor()
        self.tab_widget.addTab(self.system_monitor, "系统监控")

        # 添加恶意软件扫描标签页
        self.malware_scanner = MalwareScanner()
        self.tab_widget.addTab(self.malware_scanner, "恶意软件扫描")
        
    def create_menu_bar(self):
        # 创建菜单栏
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu('文件')
        
        # 退出动作
        exit_action = QAction('退出', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecuritySoftware()
    window.show()
    sys.exit(app.exec_())