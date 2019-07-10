class Position:
    def __init__(self,row,column):
        self.row = row
        self.column = column

    def __str__(self):
        return "Position row="+str(self.row)+", column="+str(self.column)

