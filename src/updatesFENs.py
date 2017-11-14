"""This module takes the FENs with two moves from chess.com
and 'plays' the first move, updating the FEN"""
import chess

#fenDocument = open('..\\data\\fork.csv','r') Windows version
#writeToDocument = open('..\\data\\updatedFENs.csv', 'r+')
fenDocument = open('../data/fork.csv','r')   #Mac version
writeToDocument = open('../data/updatedFENs.csv', 'r+')
i = 0
for line in fenDocument.read().split('\n'):
    if i != 0:  
        # read one line of fen document
        # read moves, separate them into two positions
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

        board.push_san(fen[1])
        newFen = board.fen()
        writeToDocument.write(newFen + ',')
        board.push_san(fen[2])
        newFen = board.fen()
        writeToDocument.write(newFen + '\n')
    i += 1
writeToDocument.close()
