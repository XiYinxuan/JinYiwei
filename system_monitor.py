import psutil
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.scan_processes()

    def init_ui(self):
        layout = QVBoxLayout()

        # 创建进程表格
        self.process_table = QTableWidget()
        self.process_table.setColumnCount(4)
        self.process_table.setHorizontalHeaderLabels(['PID', '进程名称', 'CPU使用率(%)', '内存使用(MB)'])
        layout.addWidget(self.process_table)

        # 刷新按钮
        refresh_btn = QPushButton('刷新进程列表')
        refresh_btn.clicked.connect(self.scan_processes)
        layout.addWidget(refresh_btn)

        self.setLayout(layout)

    def scan_processes(self):
        self.process_table.setRowCount(0)
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                row_position = self.process_table.rowCount()
                self.process_table.insertRow(row_position)
                
                # PID
                self.process_table.setItem(row_position, 0, QTableWidgetItem(str(proc.info['pid'])))
                # 进程名称
                self.process_table.setItem(row_position, 1, QTableWidgetItem(proc.info['name']))
                # CPU使用率
                self.process_table.setItem(row_position, 2, QTableWidgetItem(f"{proc.info['cpu_percent']:.1f}"))
                # 内存使用
                mem_mb = proc.info['memory_info'].rss / (1024 * 1024)
                self.process_table.setItem(row_position, 3, QTableWidgetItem(f"{mem_mb:.2f}"))
        except Exception as e:
            print(f"扫描进程时出错: {e}")

        # 调整列宽
        for column in range(4):
            self.process_table.resizeColumnToContents(column)