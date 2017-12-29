from PyQt4.QtGui import *
import sys
import os

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        lblName1 = QLabel()
        lblName1.setText("<b>Formula (ex.C6H6)</b>")
        self.editName1 = QLineEdit()

        lblName2 = QLabel()
        lblName2.setText("<b>Output file name (ex.C6H6.sdf)</b>")
        self.editName2 = QLineEdit()

        lblName_r = QLabel()
        lblName_r.setText("<b>****Substructure Options****</b>")

        lblName3 = QLabel("o=o (ex.<b> n</b> or <b>n-m</b>)")
        self.editName3 = QLineEdit()
        lblName4 = QLabel("o-o-o")
        self.editName4 = QLineEdit()
        lblName5 = QLabel("o=o=o")
        self.editName5 = QLineEdit()
        lblName6 = QLabel("n-o")
        self.editName6 = QLineEdit()

        btnOk = QPushButton("SUBMIT")

        layout = QVBoxLayout()
        layout.addWidget(lblName1)
        layout.addWidget(self.editName1)
        layout.addWidget(lblName2)
        layout.addWidget(self.editName2)
        layout.addWidget(lblName_r)
        layout.addWidget(lblName3)
        layout.addWidget(self.editName3)
        layout.addWidget(lblName4)
        layout.addWidget(self.editName4)
        layout.addWidget(lblName5)
        layout.addWidget(self.editName5)
        layout.addWidget(btnOk)
        self.setLayout(layout)
        btnOk.clicked.connect(self.btnOkClicked)
    def btnOkClicked(self):
        formulaname = self.editName1.text()
        outputfilename = self.editName2.text()
        name ='mgen '+formulaname+' -o '+outputfilename+' -l2d'+' -badlist '+'__BAD.sdf'
        op1 = self.editName3.text()
      	if op1 != "" :
            name = name +' -substr indeced '+op1+' subfilename'

        op2 = self.editName4.text()
        if op2 != "" :
            name = name + ' -substr indeced '+op2+' subfilename'

        op3 = self.editName5.text()
        if op3 != "" :
            name = name + ' -substr indeced '+op3+' subfilename'

        print (name)
	f = open('_%s'%(outputfilename),'w')
	f.write(name)
	f.close()
        dodo= '__Runb _%s'%(outputfilename)
        os.system(dodo)

        QMessageBox.information(self, "Submit", 'Submit to n100')



# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()

