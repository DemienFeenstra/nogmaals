from RobotArm import RobotArm

# robotArm = RobotArm('exercise 13')
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

teller = 2
while True:
    Grab = robotArm.grab()
    if not Grab:
        break
    for i in range(1,teller):
        robotArm.moveRight()
    robotArm.drop()
    teller += 1
    for i in range(1,10):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()