from PyQt4 import QtGui, QtCore
import sys, calculator

class MyApp(QtGui.QMainWindow, calculator.Ui_MainWindow):
	def __init__(self):
		super(MyApp, self).__init__()
		self.setupUi(self)
		#self.sign = ''
		#self.first_operand = ''
		#self.second_operand = ''
		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.one)
		#QtCore.QObject.connect(QtCore.Qt.Key_E, QtCore.SIGNAL("clicked()"), self.one)
		#print(QtCore.Qt.grabKeyboard())
		#self.pushButton.clicked.connect(self.one)
		self.pushButton_2.clicked.connect(self.two)
		#print(self.pushButton.hasFocus())
		self.pushButton_3.clicked.connect(self.three)
		self.pushButton_4.clicked.connect(self.four)
		self.pushButton_5.clicked.connect(self.five)
		self.pushButton_6.clicked.connect(self.six)
		self.pushButton_7.clicked.connect(self.seven)
		self.pushButton_8.clicked.connect(self.eight)
		self.pushButton_9.clicked.connect(self.nine)
		self.pushButton_10.clicked.connect(self.zero)
		self.pushButton_11.clicked.connect(self.addition)
		self.pushButton_12.clicked.connect(self.substraction)
		self.pushButton_13.clicked.connect(self.multiplication)
		self.pushButton_14.clicked.connect(self.division)
		self.pushButton_15.clicked.connect(self.result)
		self.pushButton_16.clicked.connect(self.clear)

	def one(self): self.lineEdit.insert('1')
	def two(self): self.lineEdit.insert('2')
	def three(self): self.lineEdit.insert('3')
	def four(self): self.lineEdit.insert('4')
	def five(self): self.lineEdit.insert('5')
	def six(self): self.lineEdit.insert('6')
	def seven(self): self.lineEdit.insert('7')
	def eight(self): self.lineEdit.insert('8')
	def nine(self): self.lineEdit.insert('9')
	def zero(self): self.lineEdit.insert('0')
	def addition(self):	
		#self.first_operand = self.lineEdit.text()
		#self.sign = '+'
		self.lineEdit.insert('+')
	def substraction(self):
		#self.first_operand = self.lineEdit.text()
		#self.sign = '-'
		self.lineEdit.insert('-')
	def multiplication(self):
		#self.first_operand = self.lineEdit.text()
		#self.sign = '*'
		self.lineEdit.insert('*')
	def division(self):
		#self.first_operand = self.lineEdit.text()
		#self.sign = '/'
		self.lineEdit.insert('/')
	def result(self):
		try:
			self.lineEdit.setText(str(float(eval(str(self.lineEdit.text())))))
			"""self.second_operand = self.lineEdit.text()
			if self.sign == '+':
				self.lineEdit.setText(str(float(self.first_operand) + float(self.second_operand)))
			elif self.sign == '-':
				self.lineEdit.setText(str(float(self.first_operand) - float(self.second_operand)))
			elif self.sign == '*':
				self.lineEdit.setText(str(float(self.first_operand) * float(self.second_operand)))
			elif self.sign == '/':
				self.lineEdit.setText(str(float(self.first_operand) / float(self.second_operand)))"""
		except ZeroDivisionError:
			QtGui.QMessageBox.information(self, "Error", "an attempt to divide by zero", QtGui.QMessageBox.Ok)
			self.clear()
		except NameError:
			QtGui.QMessageBox.information(self, "Error", "Something wrong with operands", QtGui.QMessageBox.Ok)
			self.clear()
		except SyntaxError:
			QtGui.QMessageBox.information(self, "Error", "Something wrong with signs", QtGui.QMessageBox.Ok)
			self.clear()
	def clear(self):
		#self.sign, self.first_operand, self.second_operand = '', '', ''
		self.lineEdit.setText('')
	def keyPressEvent(self, event):
		if event.key() == 43:
			self.addition()
		elif event.key() == 45:
			self.substraction()
		elif event.key() == 42:
			self.multiplication()
		elif event.key() == 47:
			self.division()
		elif event.key() == 48:
			self.zero()
		elif event.key() == 49:
			self.one()
		elif event.key() == 50:
			self.two()
		elif event.key() == 51:
			self.three()
		elif event.key() == 52:
			self.four()
		elif event.key() == 53:
			self.five()
		elif event.key() == 54:
			self.six()
		elif event.key() == 55:
			self.seven()
		elif event.key() == 56:
			self.eight()
		elif event.key() == 57:
			self.nine()
		elif event.key() == 61 or event.key() == 16777221:
			self.result()
def main():
	app = QtGui.QApplication(sys.argv)
	form = MyApp()
	form.show()
	sys.exit(app.exec_())

if __name__ == '__main__':	
    main()