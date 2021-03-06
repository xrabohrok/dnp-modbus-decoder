'''struct to contain nested info about message'''
class Report:
    def __init__(self):
        self.Next = []
        self.title = ""
        self.description = ""
        self.data = ""
        self.raw = ""

    def __init__(self, Title, Description, Data, Raw=""):
        self.Next = []
        self.title = Title
        self.description = Description
        self.data = Data
        self.raw = Raw
        
    def AddNext(self, ob):
        self.Next.append(ob)
      
'''displays report contents in console, debug purposes only
always start with depth of zero

Feel free to ape the basic implementation, though'''      
def printReport(report, depth = 0):
    space = ""
    for i in range(0, depth):
        space += "  "
        
    if not report == None:
        print ((space + "Title: {}\n" + space + "Description: {}\n" + space + "Data: {}\n").format(report.title, report.description, report.data))
        
        for i in report.Next:
            printReport(i, depth + 1)