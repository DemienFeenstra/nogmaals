from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

for i in range(9, 0, -2):
    robotArm.grab()
    for j in range(i):
        robotArm.moveRight()
    robotArm.drop()
    for k in range(i - 1):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()