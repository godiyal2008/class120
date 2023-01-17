#name=input("enter ur name")
#print (name)
import time
#print(dir(time))
seconds = input("Enter the time in no. of seconds")
def timer(seconds):
    while seconds>0:
        
      mins=int(seconds/60)
      secs=int(seconds%60)
      timer=f'{mins}:{secs}'
      time.sleep(1)
      print(timer)
      seconds -=1
    print("timesup")
timer(int(seconds))