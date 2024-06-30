from PyQt6.QtWidgets import QFrame, QGridLayout, QLabel
from PyQt6.QtCore import Qt

class MapDisplayFrame(object):
    def __init__(self, dataframe):
        self.dataframe = dataframe

        self.frame = QFrame()

        layout = QGridLayout()

        for x in range(5):
            for y in range(5):
                newLabel = QLabel()
                cellData = self.dataframe.iat[x, y]
                if type(cellData) == type(None):
                    cellData = cellData
                else:
                    cellData = cellData.getRoomName()

                newLabel.setText(cellData)
                newLabel.setStyleSheet("""QLabel {
                                    background-color: beige;
                                    color: black;
                                    font-family: 'Georgia';
                                    font-size: 12pt; 
                                    border: 1px solid black;
                                    margin: 0px;
                                    min-height: 75px;
                                    min-width: 200px;}""")
                newLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                layout.addWidget(newLabel, x, y, 1, 1, Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(0)        

        self.frame.setLayout(layout)

    def getFrame(self):
        return self.frame