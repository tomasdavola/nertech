class WorkPackage():
    def __init__(self, name, startWeek, duration):
        self.name=name
        self.startWeek=startWeek
        self.duration=duration

    def getEndWeek(self):
        return self.startWeek+self.duration

class Project():
    def __init__(self, name, workPackages):
        self.name=name
        self.workPackages=workPackages

    def getStartWeek(self):
        earliestPackage=None
        startWeek=9999999999
        for workPackage in self.workPackages:
            if workPackage.startWeek<startWeek:
                startWeek=workPackage.startWeek
                earliestPackage=workPackage
        return startWeek, earliestPackage

    def getEndWeek(self):
        sortedPackages = sorted(self.workPackages, key=lambda x: x.startWeek)
        #Greedy approach, do the first available project
        currentTime=self.getStartWeek()[0]
        for package in sortedPackages:
            if currentTime>=package.startWeek:
                currentTime+=package.duration
            else:
                currentTime=package.startWeek+package.duration
        return currentTime

#Testing
a=WorkPackage("a", 1,2)
b=WorkPackage("a", 0,2)
c=WorkPackage("a", 8,2)
p=Project("a", [a,b,c])
print(p.getEndWeek())
