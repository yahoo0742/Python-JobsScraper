from Utilities import XStr

CSVDelimiter = ','

class Job:
    '''
    Id = ""
    Title = ""
    WorkType = ""
    Salary = ""
    Location = ""
    ListingDate = ""
    ExpiryDate = ""
    Keywords = ""
    '''
    '''def __init__(self, d):
        self.__dict__ = d
        print(self.ToString())
        
    def ToString(self):
        return str(self.__dict__)'''

    def __init__(self, Id, title, workType, salary, location, listingDate, expiryDate, keywords):
        self.Id = Id
        self.Title = title.replace(CSVDelimiter,'_')
        self.WorkType = XStr(workType).replace(CSVDelimiter,'_')
        self.Salary = XStr(salary).replace(CSVDelimiter,'_')
        self.Location = XStr(location).replace(CSVDelimiter,'_')
        self.ListingDate = XStr(listingDate).replace(CSVDelimiter,'_')
        self.ExpiryDate = XStr(expiryDate).replace(CSVDelimiter,'_')
        self.Keywords = keywords.replace(CSVDelimiter,'_')
        #print(self.ToString())

    def ToString(self):
        return self.Id+CSVDelimiter+self.Title+CSVDelimiter+self.WorkType+CSVDelimiter+self.Salary+CSVDelimiter+self.Location+CSVDelimiter+self.ListingDate+CSVDelimiter+self.ExpiryDate+CSVDelimiter+self.Keywords

    @staticmethod
    def Fields():
        return "ID"+CSVDelimiter+"Title"+CSVDelimiter+"WorkType"+CSVDelimiter+"Salary"+CSVDelimiter+"Location"+CSVDelimiter+"Listing Date"+CSVDelimiter+"ExpiryDate"+CSVDelimiter+"Keywords"
