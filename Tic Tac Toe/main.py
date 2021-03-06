#Arturo Vargas
#Simple tic-tac-toe game 
#Status:11-29-2013
#Win conditions complete
#This is a simple exercise 
#I did to become familiar with python syntax
#Feel free to play and build upon

from TicTac import TicTac #imports the board object

#Main code          
def main():

    print "Welcome to Tic tac toe"
    print ""
    print "==============Start============="
    print ""
    game=TicTac()
    game.show()

  #Game is in motion!
    turn=0;
    while turn <= 9:
        

        valid=0
        while (valid != 1):
            print "==============Player 1 !============="
            print ""
            try: 
                p1=int(raw_input("P1 choose a location: "))
                valid=game.turn(p1,"X")
            except ValueError:
                print "Not valid, enter a number: "

            game.show()
            if(game.win(1) == 0):
                return
                
            turn = turn+valid
            print "End of turn: " + str(turn)
        
        if turn ==9:
            break

        
        valid=0
        while (valid != 1):
            print "==============Player 2 !============="
            print ""
            try:
                p2=int(raw_input("P2 choose a location: "))
                valid =game.turn(p2,"O")

            except ValueError:
                print "Not valid, enter a number: "
            game.show()
            if(game.win(2) == 0):
                return
            turn = turn+valid
            print "End of turn: " + str(turn)
        
    print "Game over! Thanks for playing!"

main()
