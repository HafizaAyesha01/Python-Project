
'''The following code is made by taking help for variuos github codes and youtube tutorials.
But some of the code is original and mine'''


import graphics
import random

#Functions to play and draw the game
def playGame(): #Game Start Point
    '''Constructor to choose and select the background and diffculty 
    for gameplay'''
    youWin = graphics.GraphWin("Connect Four Game", 1000, 650)
    youWin.setCoords(0, 0, 1000, 650)
    back = graphics.color_rgb(255,255,224)
    youWin.setBackground(back)
    locationDifficulty =opening(youWin)
    location=locationDifficulty[0]
    difficulty=locationDifficulty[1]
    strategy = ComputerStrategy(difficulty)
    gameBoard = Board()
    gamePlay(youWin,location, gameBoard, difficulty,strategy)
    tryAgain(youWin,gameBoard)

def opening(youWin):
    '''Makes the initial grouping to the game where players pick 

a trouble setting and foundation for playing 

Boundary: 

youWin - window the graphic is brought into'''
    welcome = graphics.Text(graphics.Point(500, 550), 
                            'WELCOME TO CONNECT FOUR!!!')
    welcome.setStyle('bold')
    welcome.setFace('arial')
    welcome.setSize(36)
    welcome.setTextColor('Midnight Blue')
    welcome.draw(youWin)
    choice1 = graphics.Text(graphics.Point(500, 450), 
                            'Select Where You Would Like To Play!')
    choice1.setFace('arial')
    choice1.setSize(20)
    choice1.setTextColor('Midnight Blue')
    choice1.draw(youWin)

    #chooses a place screen
    saylesBack = graphics.Rectangle(graphics.Point(675,100), 
                                    graphics.Point(970, 325))
    saylesBack.setFill('black')
    saylesBack.draw(youWin)
    saylesBox=graphics.Image(graphics.Point(822.5,212.5),"saylesTN.gif")
    saylesBox.draw(youWin)
    saylesText = graphics.Text(graphics.Point(822.5,212.5), 'Sayles')
    saylesText.setFace('arial')
    saylesText.setSize(30)
    saylesText.setStyle("bold")
    saylesText.setTextColor("white")
    saylesText.draw(youWin)

    cmcBack = graphics.Rectangle(graphics.Point(30,100), 
                                 graphics.Point(325, 325))
    cmcBack.setFill('black')
    cmcBack.draw(youWin)
    cmcBox=graphics.Image(graphics.Point(177.5,212.5),"cmcTN.gif")
    cmcBox.draw(youWin)
    cmcText = graphics.Text(graphics.Point(177.5,212.5), 'CMC')
    cmcText.setFace('arial')
    cmcText.setSize(30)
    cmcText.setStyle("bold")
    cmcText.setTextColor("white")
    cmcText.draw(youWin)

    bsBack = graphics.Rectangle(graphics.Point(347.5,100), 
                                graphics.Point(652.5, 325))
    bsBack.setFill('black')
    bsBack.draw(youWin)
    baldBox=graphics.Image(graphics.Point(500,212.5),"baldTN.gif")
    baldBox.draw(youWin)
    baldText = graphics.Text(graphics.Point(500,212.5), 'Bald Spot')
    baldText.setFace('arial')
    baldText.setSize(30)
    baldText.setStyle("bold")
    baldText.setTextColor("white")
    baldText.draw(youWin)

    location=getBackground(youWin)

    baldText.undraw()
    baldBox.undraw()
    bsBack.undraw()
    cmcText.undraw()
    cmcBox.undraw()
    cmcBack.undraw()
    saylesText.undraw()
    saylesBox.undraw()
    saylesBack.undraw()
    choice1.undraw()

    #Chooses a difficulty screen
    choice2 = graphics.Text(graphics.Point(500, 450), 
                            'Select A Difficulty Level! \n \n  Human Player Will Play First')
    choice2.setFace('arial')
    choice2.setSize(18)
    choice2.setTextColor('Midnight Blue')
    choice2.draw(youWin)

    easy = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    easy.setFill('green')
    easyText = graphics.Text(graphics.Point(370,300),"EASY")
    easyText.setFace('arial')
    easyText.setSize(24)
    easyText.setTextColor("White")
    easy.draw(youWin)
    easyText.draw(youWin)

    medium = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    medium.setFill('gold')
    mediumText = graphics.Text(graphics.Point(630,300),"MEDIUM")
    mediumText.setFace('arial')
    mediumText.setSize(24)
    mediumText.setTextColor("White")
    medium.draw(youWin)
    mediumText.draw(youWin)

    advanced = graphics.Rectangle(graphics.Point(510,265),graphics.Point(750,215))
    advanced.setFill('black')
    advancedText = graphics.Text(graphics.Point(630,240),"ADVANCED")
    advancedText.setFace('arial')
    advancedText.setSize(24)
    advancedText.setTextColor("White")
    advanced.draw(youWin)
    advancedText.draw(youWin)

    hard = graphics.Rectangle(graphics.Point(250,265),graphics.Point(490,215))
    hard.setFill('red')
    hardText = graphics.Text(graphics.Point(370,240),"HARD")
    hardText.setFace('arial')
    hardText.setSize(24)
    hardText.setTextColor("White")
    hard.draw(youWin)
    hardText.draw(youWin)

    difficulty = getDifficulty(youWin)
    return [location,difficulty]

def gamePlay(youWin,location, gameBoard, difficulty,strategy):
    '''Draws the gameBoard for Connect Four the area picked by the player 

Boundary: 

youWin - window the graphic is brought into 

area - picture record of the area picked by the player 

gameBoard - rundown of records containing pieces 

trouble - the snap of the client used to pick procedure 

procedure - the PC's method of picking where to put a piece
    '''
    gamePlace = graphics.Image(graphics.Point(500,325), location)
    gamePlace.draw(youWin)
    grid=graphics.Image(graphics.Point(500,300),"CFBoard.gif")
    grid.draw(youWin)
    getFour=False
    turnCount=0
    while getFour==False:
        if turnCount%2==0:
            playerColor="maize"
            setColumn = getHumanColumn(youWin)
        else:
            playerColor="blue"
            if strategy.strategyReturn() == "easy":
                setColumn = strategy.easy()
            if strategy.strategyReturn() == "medium":
                setColumn = strategy.medium(gameBoard)
            if strategy.strategyReturn() == "hard":
                setColumn = strategy.hard(gameBoard)
            if strategy.strategyReturn() == "advanced":
                setColumn = strategy.advanced(gameBoard)
        filledSpot=gameBoard.getTileCoordinate(setColumn,playerColor)
        gameBoard.playTile(filledSpot,playerColor)
        tileFall(youWin,filledSpot,playerColor)
        end=gameBoard.checkForWin()
        if end=="win":
            drawWin(youWin)
            getFour=True  
        elif end =="loss":
            drawLoss(youWin)
            getFour=True
        elif end == "tie":
            drawTie(youWin)
            getFour = True
        else:
            turnCount+=1
    youWin.getMouse()

def getBackground(youWin):
    """Decides wanted background for game dependent on clicks by client 

Boundary
    youWin - window the graphic is drawn into"""
    back = False
    while back ==False:
        userClick=youWin.getMouse()
        if int(userClick.getX()) in range(675,970) and int(userClick.getY()) in range(100,325):
            image = "sayles.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(30,325) and int(userClick.getY()) in range(100,325):
            image= "cmc.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(348,653) and int(userClick.getY()) in range(100,325):
            image = "bald.gif"
            back=True
            return image      
        
def getDifficulty(youWin):  #Sets the game difficulty
    """Decides wanted difficulty level (hard, easy, medium or advanced) of game, given graphical client input 

Boundary:
    youWin - window the graphic is drawn into
    """
    userClick=youWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        difficulty = 1 #makes easy
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        difficulty = 2 #makes medium
    elif int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(215,265):
        difficulty = 3 #makes hard
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(215,265):
        difficulty = 4 #make advanced 
    else:
        difficulty=getDifficulty(youWin)
    return difficulty
        
def getHumanColumn(youWin): # This functions returns the segment chose by the human player through clicks
    
    userClick = youWin.getMouse()
    if int(userClick.getX()) in range(190,265):
        setColumn = 0
    elif int(userClick.getX()) in range(275,355):
        setColumn = 1
    elif int(userClick.getX()) in range(370,445):
        setColumn=2
    elif int(userClick.getX()) in range(455,535):
        setColumn=3
    elif int(userClick.getX()) in range(555,625):
        setColumn=4
    elif int(userClick.getX()) in range(635,715):
        setColumn=5
    elif int(userClick.getX()) in range(725,805):
        setColumn=6
    else:
        setColumn=getHumanColumn(youWin)
    return setColumn

def tileFall(youWin, coordinate, playerColor): # This functions animates/shows the tile fall through the gameBoard

    if int(coordinate[0])==0:
        xCoord=224
    if int(coordinate[0])==1:
        xCoord=314
    if int(coordinate[0])==2:
        xCoord=404
    if int(coordinate[0])==3:
        xCoord=494
    if int(coordinate[0])==4:
        xCoord=586
    if int(coordinate[0])==5:
        xCoord=675
    if int(coordinate[0])==6:
        xCoord=766
    if coordinate[1]==5:
        yCoord=80
    if coordinate[1]==4:
        yCoord=170
    if coordinate[1]==3:
        yCoord=260
    if coordinate[1]==2:
        yCoord=350
    if coordinate[1]==1:
        yCoord=440
    if coordinate[1]==0:
        yCoord=530
    if playerColor=="maize":
        color="gold"
    elif playerColor=="blue":
        color="blue"
    playerPiece = graphics.Circle(graphics.Point(xCoord,600),38)
    i=0
    #makes sure piece begins animating at the top of the gameBoard
    if yCoord < 500: 
        while (600-i) > yCoord +100:
            i += 20 #animates piece
            #playerPiece.undraw()
            playerPiece=graphics.Circle(graphics.Point(xCoord,600-i),38)
            playerPiece.setFill(color)
            playerPiece.draw(youWin)
            playerPiece.undraw()
    playerPiece = graphics.Circle(graphics.Point(xCoord,yCoord),38)
    playerPiece.setFill(color)
    playerPiece.draw(youWin)

def drawWin(youWin): #This function draws stars all over screen if user wins the game
    
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            winStar = graphics.Image(graphics.Point(i, j),"goldstar.gif")
            winStar.draw(youWin)
    finalStar = graphics.Image(graphics.Point(500,325),"goldstar.gif")
    finalStar.draw(youWin)
    winText = graphics.Text(graphics.Point(500, 325), "YOU WIN!")
    winText.setFace("arial")
    winText.setStyle('bold')
    winText.setSize(36)
    winText.draw(youWin)
def drawLoss(youWin): # This function draws sad faces all over screen if human user loses 
    
    for i in range (0, 1200, 100):
         for j in range(0, 800, 100):
            loseFace = graphics.Image(graphics.Point(i, j),"lose.gif")
            loseFace.draw(youWin)
    finalLose = graphics.Circle(graphics.Point(500,325),150)
    finalLose.setFill("blue")
    finalLose.draw(youWin)
    loseText = graphics.Text(graphics.Point(500, 325), "Computer Wins")
    loseText.setFace("arial")
    loseText.setStyle('bold')
    loseText.setSize(36)
    loseText.draw(youWin)

def drawTie(youWin):#This function draws tiles over the screen to indicate a draw/tie game
   
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            tie = graphics.Image(graphics.Point(i, j),"tie.gif")
            tie.draw(youWin)
    finalTie = graphics.Image(graphics.Point(500,325),"finalTie.gif")
    finalTie.draw(youWin)
    tieText = graphics.Text(graphics.Point(500, 250), "It's a tie!")
    tieText.setFace("arial")
    tieText.setStyle('bold')
    tieText.setSize(36)
    tieText.draw(youWin)        

def tryAgain(youWin,gameBoard): # Ask user to startover again
    
    backColor = graphics.color_rgb(255,255,224)
    back = graphics.Rectangle(graphics.Point(0,0),graphics.Point(1000,650))
    back.setFill(backColor)
    back.draw(youWin)
    replay = graphics.Text(graphics.Point(500,550),"Would you like to play again?")
    replay.setStyle('bold')
    replay.setFace('arial')
    replay.setSize(36)
    replay.setTextColor('Midnight Blue')
    replay.draw(youWin)
    yes = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    yes.setFill('green')
    yesText = graphics.Text(graphics.Point(370,300),"YES")
    yesText.setFace('arial')
    yesText.setSize(24)
    yesText.setTextColor("White")
    yes.draw(youWin)
    yesText.draw(youWin)
    no = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    no.setFill('gray')
    noText = graphics.Text(graphics.Point(630,300),"NO")
    noText.setFace('arial')
    noText.setSize(24)
    noText.setTextColor("White")
    no.draw(youWin)
    noText.draw(youWin)
    userClick=youWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        gameBoard.resetBoard()
        playGame()
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        return