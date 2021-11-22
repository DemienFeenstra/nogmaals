from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

for i in range(1,5):
    for j in range(0, i):
        robotArm.grab()
        for k in range(0, 5):
            robotArm.moveRight()
        robotArm.drop()
        for l in range(0, 5):
            robotArm.moveLeft()
    robotArm.moveRight()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()