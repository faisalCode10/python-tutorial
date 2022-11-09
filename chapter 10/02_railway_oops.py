class RailwayForm:
    formType = "railwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")


faisalApplication = RailwayForm()
faisalApplication.name = "faisal"
faisalApplication.train = "rawalpindi Express"
faisalApplication.printData()