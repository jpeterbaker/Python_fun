#Creates the board as an object
#This class is in used in conjection 
# with the main file of the Tic_Tac_Toe folder

class TicTac:

    def __init__(self):
        self.data=[0,1,2,3,4,5,6,7,8]
        self.entries=[]

    #replaces board with x, checks if entry has been used
    def turn(self,p,x):

        if p>8 or p<0:
            print "No such entry"
            return 0

        elif(self.data[p] != "X" and  self.data[p] !="O"):
            self.data[p] = x
            return 1
        else:
            print "Entry in use!"
            return 0

    #check if there is a win
    def win(self,p):
        #Checks for wins across
        Xcount=0
        Ocount=0   
        for k in range(0,3):
            for j in range(0,3):
                if (self.data[k*3+j]=='X'):
                    Xcount=Xcount+1;
                elif (self.data[k*3+j]=='O'):
                    Ocount=Ocount+1;

                if (p==1 and Xcount==3):
                    print "Tic-Tac-Toe! Player " + '1' +" wins across!"
                    return 0
                
                if (p==2 and Ocount==3):
                    print "Tic-Tac-Toe! Player " + '2' +" wins across!"
                    return 0

            Xcount=0;
            Ocount=0;
            
            
        #Checks for vertical wins
        #j and k have been switched
        Xcount=0;
        Ocount=0;
        for j in range(0,3):
            for k in range(0,3):
                if (self.data[k*3+j]=='X'):
                    Xcount=Xcount+1;
                elif (self.data[k*3+j]=='O'):
                    Ocount=Ocount+1;

                if (p==1 and Xcount==3):
                    print "Tic-Tac-Toe! Player " + '1' +" vertical win!"
                    return 0
                
                if (p==2 and Ocount==3):
                    print "Tic-Tac-Toe! Player " + '2' +" vertical win!"
                    return 0

            Xcount=0;
            Ocount=0;

        #Check for left-top -> bottom right win
        Xcount=0;
        Ocount=0;
        for k in range(0,3):
            if (self.data[k*3+k]=='X'):
                Xcount=Xcount+1;
            elif (self.data[k*3+k]=='O'):
                Ocount=Ocount+1;
                
        if (p==1 and Xcount==3):
            print "Tic-Tac-Toe! Player " + '1' +" left to right diagonal win!"
            return 0
            
        if (p==2 and Ocount==3):
            print "Tic-Tac-Toe! Player " + '2' +" left to right diagonal win!"
            return 0


        
        #Check for right-top -> left-bottom win 
        T=[2,4,6]
        Xcount=0;
        Ocount=0;
        for t in range(0,3):
            if (self.data[T[t]]=='X'):
                Xcount=Xcount+1;
            elif (self.data[T[t]]=='O'):
                Ocount=Ocount+1;
                
        if (p==1 and Xcount==3):
            print "Tic-Tac-Toe! Player " + '1' +" right to left diagonal win!"
            return 0
        
        if (p==2 and Ocount==3):
            print "Tic-Tac-Toe! Player " + '2' +" right to left diagonal win!"
            return 0



    #displays to screen
    def show(self):
        for x in range(0,3):
            for y in range(0,3):
                print "|" + str(self.data[3*x+y]) + "|" ,
            print ""
