class Box:
    '''
    self.is_allowed used for finding not used boxes
    '''
    def __init__(self,is_allowed=False,symbol=None):
        self.is_allowed = is_allowed
        self.symbol = symbol

    def updateSymbol(self,symbol):
        self.symbol = symbol

    # checks if the box is allowed (used/not used box)
    def isBoxAllowed(self):
        if(self.is_allowed==True):
            return True
        else:
            return False

    # checks if the box is not already used by the user
    def isBoxAvailable(self):
        return True if self.symbol== None else False

    def updateisAllowed(self,is_allowed=True):
        self.is_allowed = is_allowed

