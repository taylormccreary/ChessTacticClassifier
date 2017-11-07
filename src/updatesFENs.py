"""This module takes the FENs with two moves from chess.com
and 'plays' the first move, updating the FEN"""
import chess

fenDocument = open('..\\data\\fork.csv','r')
writeToDocument = open('..\\data\\updatedFENs.csv', 'r+')
i = 0
movePiece = []
newLocation = []
attack = []
kingCheck = []
for line in fenDocument.read().split('\n'):
    if i != 0:  
        # read one line of fen document
        # read moves, seperate them into two positions
        # create board from position of first fen
        # input first move
        # output fen after first move and write it to updatedFENs
        # add comma
        # add next move to board
        # write new fen board to csv file
        fen = line.split(',')
        #print (fen[3])
        if fen[3] == "white":
            fen[0] = fen[0] + ' w' + " KQkq - 0 1"
        else:
            fen[0] = fen[0] + ' b' + " KQkq - 0 1"

        board = chess.Board(fen[0])
        # print (fen[1]+fen[2])
        # FirstMove = chess.Move.from_uci(fen[1]+fen[2])
        for char in ' ':
            fen[1] = fen[1].replace(char, '')
            fen[2] = fen[2].replace(char, '')
            
        
        #Find which piece moved, if it attacked, where it moved, and if king in check    
        if fen[2].isupper() == true:
            #seperate piece
            movePiece = fen[2][0]
            if fen[2][1] == 'x':
                #check for attacks
                attack = '1'
            else:
                attack = '0'
        else:
            #pawn moves
            movePiece = 'p'
            if fen[2][0] == 'x':
                #check for attacks
                attack = '1'
            else:
                attack = '0'
        if fen[2][fen[2].length()-1] == '+':
            kingCheck = '1'
            movestring = fen[2][fen[2].length()-3] + fen[2][fen[2].length()-2]
            newLocation = movestring
        else:
            kingCheck = '0'
            movestring = fen[2][fen[2].length()-2] + fen[2][fen[2].length()-1]
            newLocation = movestring
        
        
        board.push_san(fen[1])
        newFen = board.fen()
        writeToDocument.write(newFen + ',')
        board.push_san(fen[2])
        newFen = board.fen()
        writeToDocument.write(newFen + ',')
        writeToDocument.write(movePiece + ',')
        writeToDocument.write(attack + ',')
        writeToDocument.write(newLocation + ',')
        writeToDocument.write(kingCheck + '\n')
    i += 1
writeToDocument.close()
