import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog
)
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt

# Thermal conductivity values for materials (W/m·K)
materials = {
    "آجر": 0.72,
    "بتن": 1.75,
    "چوب": 0.15,
    "شیشه": 0.8,
    "پلی‌کربنات": 0.22
}

class HeatLossApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("محاسبه اتلاف حرارتی دیوار و پنجره")
        self.setGeometry(100, 100, 800, 600)

        self.items = []  # List of all sections
        self.setup_ui()

    def setup_ui(self):
        # Load custom Persian font (Vazir)
        font_id = QFontDatabase.addApplicationFont("Vazirmatn-Medium.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(font_family, 11)
        self.setFont(custom_font)

        self.setLayoutDirection(Qt.RightToLeft)  # Enable RTL direction

        layout = QVBoxLayout()

        # Temperature input
        temp_layout = QHBoxLayout()
        self.temp_label = QLabel("اختلاف دمای داخل و بیرون (درجه سانتی‌گراد):")
        self.temp_input = QLineEdit()
        self.temp_input.setText("20")
        temp_layout.addWidget(self.temp_label)
        temp_layout.addWidget(self.temp_input)
        layout.addLayout(temp_layout)

        # Section form: type, material, size, thickness
        form_layout = QHBoxLayout()
        self.section_type = QComboBox()
        self.section_type.addItems(["دیوار", "پنجره"])

        self.material_input = QComboBox()
        self.material_input.addItems(materials.keys())

        self.thickness_input = QLineEdit()
        self.thickness_input.setPlaceholderText("ضخامت (میلی‌متر)")
        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("طول (متر)")
        self.width_input = QLineEdit()
        self.width_input.setPlaceholderText("عرض (متر)")

        form_layout.addWidget(self.section_type)
        form_layout.addWidget(self.material_input)
        form_layout.addWidget(self.thickness_input)
        form_layout.addWidget(self.length_input)
        form_layout.addWidget(self.width_input)
        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_btn = QPushButton("➕ افزودن به لیست")
        self.add_btn.clicked.connect(self.add_item)

        self.total_btn = QPushButton("📊 محاسبه مجموع کل اتلاف")
        self.total_btn.clicked.connect(self.calculate_total)

        self.save_btn = QPushButton("💾 ذخیره به صورت فایل CSV")
        self.save_btn.clicked.connect(self.save_csv)

        self.chart_btn = QPushButton("📈 نمایش نمودار دایره‌ای")
        self.chart_btn.clicked.connect(self.show_chart)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.total_btn)
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.chart_btn)
        layout.addLayout(button_layout)

        # Table for displaying entries
        self.table = QTableWidget(0, 6)
        self.table.setLayoutDirection(Qt.RightToLeft)
        self.table.setHorizontalHeaderLabels(["نوع", "جنس", "ضخامت (mm)", "طول (m)", "عرض (m)", "اتلاف (W)"])
        layout.addWidget(self.table)

        self.setLayout(layout)

    def add_item(self):
        try:
            # Read and calculate values
            section = self.section_type.currentText()
            material = self.material_input.currentText()
            thickness_mm = float(self.thickness_input.text())
            length = float(self.length_input.text())
            width = float(self.width_input.text())
            delta_T = float(self.temp_input.text())

            thickness_m = thickness_mm / 1000
            area = length * width
            k = materials[material]
            U = k / thickness_m
            Q = U * area * delta_T

            self.items.append((section, material, thickness_mm, length, width, Q))

            row = self.table.rowCount()
            self.table.insertRow(row)
            for i, val in enumerate([section, material, thickness_mm, length, width, round(Q, 2)]):
                self.table.setItem(row, i, QTableWidgetItem(str(val)))

        except ValueError:
            QMessageBox.warning(self, "خطای ورودی", "لطفاً تمام مقادیر را به‌درستی وارد کنید.")

    def calculate_total(self):
        total_Q = sum(item[5] for item in self.items)
        QMessageBox.information(self, "اتلاف کل", f"🔻 مجموع کل اتلاف حرارتی: {total_Q:.2f} وات")

    def save_csv(self):
        if not self.items:
            QMessageBox.warning(self, "خطا", "لیست خالی است.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "ذخیره فایل", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["نوع", "جنس", "ضخامت (mm)", "طول (m)", "عرض (m)", "اتلاف حرارت (W)"])
                for row in self.items:
                    writer.writerow(row)
            QMessageBox.information(self, "ذخیره شد", f"فایل با موفقیت ذخیره شد:\n{file_path}")

    def show_chart(self):
        if not self.items:
            QMessageBox.warning(self, "خطا", "لیست خالی است.")
            return

        labels = [f"{i+1}-{row[0]}" for i, row in enumerate(self.items)]
        sizes = [row[5] for row in self.items]

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title("نمودار دایره‌ای سهم اتلاف حرارتی هر بخش")
        plt.axis("equal")
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HeatLossApp()
    window.show()
    sys.exit(app.exec_())
