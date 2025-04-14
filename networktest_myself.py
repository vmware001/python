import subprocess
import re
import statistics
import datetime
import time
import os
from pathlib import Path

#config

domain="119.29.29.29"
interval=1.000
pingsPerRound=10
outputDict="./log/"
overtimeMaxTime=3.000

#end_config

class program:
    def __init__(self):
        self.logDir = Path(outputDict)
        self.logDir.mkdir(parents=True, exist_ok=True)
        self.resetStats()
        self.currentLog = None

    def resetStats(self):
        self.pingCount=0
        self.delays=[]
        self.pkgLost=0
        self.maxDelay=0
        self.startTime=datetime.datetime.now()
        self.avgDelay=0
        self.stdevDelay=0
        self.writeContent = ""

    def writeToFile(self):
        logName = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        logPath = self.logDir / logName
        with open(logPath, "w") as f:
            f.write(self.writeContent)
        self.currentLog = None  # 因为用了 with，不需要手动管理

    def pingOnce(self):
        commandLine=["ping","-c","1",domain]
        result = subprocess.run(commandLine, capture_output=True, text=True, timeout=overtimeMaxTime) #exec command and catch results
        if match := re.search(r"time=(\d+\.?\d*)\s?ms", result.stdout): #match regex
            delay = float(match.group(1))
            self.maxDelay = max(self.maxDelay, delay)
            return delay
        return -1 #output is not match regex -> ping overtime

    def runInRound(self):
        while self.pingCount < pingsPerRound:
            delay=self.pingOnce()
            time.sleep(interval)
            self.pingCount+=1
            if delay!=-1:
                self.delays.append(delay) #add to delays array
                consoleOutput="["+datetime.datetime.now().strftime("%H:%M:%S")+"] delay:"+str(delay)+" ms"
            else:
                self.delays.append(overtimeMaxTime) #add $overtieMax time to array, to ensure average delay time is accurate
                self.pkgLost+=1
                consoleOutput="["+datetime.datetime.now().strftime("%H:%M:%S")+"] Overtime!!!"
            print(consoleOutput)
        self.getStatInfo()
        self.writeToFile()
        self.resetStats()

    def getStatInfo(self):
        self.avgDelay=statistics.mean(self.delays)
        self.stdevDelay=statistics.stdev(self.delays)
        self.writeContent=("["+datetime.datetime.now().strftime("%H:%M:%S")+"]\n"+
                           "Average Delay:"+str(self.avgDelay)+"ms\n"+
                           "Standard dev delay:"+str(self.stdevDelay)+"ms\n"+
                           "Max Delay:"+str(self.maxDelay)+"ms\n"+
                           "Package Lost Rate:"+str(self.pkgLost/pingsPerRound)
        )

def main():
    monitor = program() 
    try:
        while True:
            monitor.runInRound()
            print("Finished one round test, "+str(pingsPerRound)+" ping\n")
    except KeyboardInterrupt:
        print("\nTerminating...")
        if monitor.currentLog:
            monitor.currentLog.close()

main()



