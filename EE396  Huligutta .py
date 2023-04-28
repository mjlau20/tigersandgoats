#!/usr/bin/env python
# coding: utf-8

def undoMove(boardPosition, move, factor):

    if factor == -1:
        if move[2] == 'p':
            if boardPosition[move[1]] != '0':
                boardPosition.update({move[1]:'0'})
        elif move[2] == 'm':
                if boardPosition[move[0]] == '0' and boardPosition[move[1]] != '0':
                    boardPosition.update({move[0]:boardPosition[move[1]]})
                    boardPosition.update({move[1]:'0'})
        else:
            # place holder for undo capture
            print('c')
            
    return boardPosition

factor = -1
position = {                            'b0': '0' , 
                'a1': 'g' , 'b1': 'g' , 'c1': 't' , 'd1': '0' , 'e1': 'g' , 'f1': 't' , 
                'a2': '0' , 'b2': '0' , 'c2': '0' , 'd2': 'g' , 'e2': '0' , 'f2': '0' ,
                'a3': 't' , 'b3': 'g' , 'c3': '0' , 'd3': '0' , 'e3': 'g' , 'f3': 't' ,
                            'b4': '0' , 'c4': 'g' , 'd4': '0' , 'e4': '0' ,               }
move = ('b1','b2','m')
#move = ('0','c1','p')

undoMove(position, move, factor)