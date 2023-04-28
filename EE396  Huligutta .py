#!/usr/bin/env python
# coding: utf-8

# In[21]:


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

position = {                            'b0': '0' , 
                'a1': 'g' , 'b1': 'g' , 'c1': 't' , 'd1': '0' , 'e1': 'g' , 'f1': 't' , 
                'a2': '0' , 'b2': '0' , 'c2': '0' , 'd2': 'g' , 'e2': '0' , 'f2': '0' ,
                'a3': 't' , 'b3': 'g' , 'c3': '0' , 'd3': '0' , 'e3': 'g' , 'f3': 't' ,
                            'b4': '0' , 'c4': 'g' , 'd4': '0' , 'e4': '0' ,               }
move = ('b1','b2','m')
#move = ('0','c1','p')
factor = -1

undoMove(position, move, factor)
# Undo movement
#    move[0] = 'g' or 't'
#    move[1] = '0'
# Undo placement
#    move[0] = 'g' or 't'
#    move[1] = '0'
# Undo capture
#    move[0] = 't'
#    move[1] = '0'
#    move[1] - move[0] = 'g'


# In[5]:


def undoMove2(boardPosition, move, factor):
    holdMove = []
    
    for position in boardPosition.keys():
        if move[0] == position:
            if boardPosition[position] == '0':
                holdMove.append(position)
            
    for piecePosition in boardPosition.keys():
        if move[1] == piecePosition:
            if boardPosition[piecePosition] != '0':
                holdMove.append(boardPosition[piecePosition])
                holdMove.append(piecePosition)
    
    boardPosition.update({holdMove[0]:holdMove[1]})
    boardPosition.update({holdMove[2]:'0'})
    
    return boardPosition

position = {                            'b0': '0' , 
                'a1': 'g' , 'b1': 'g' , 'c1': 't' , 'd1': '0' , 'e1': 'g' , 'f1': 't' , 
                'a2': '0' , 'b2': '0' , 'c2': '0' , 'd2': 'g' , 'e2': '0' , 'f2': '0' ,
                'a3': 't' , 'b3': 'g' , 'c3': '0' , 'd3': '0' , 'e3': 'g' , 'f3': 't' ,
                            'b4': '0' , 'c4': 'g' , 'd4': '0' , 'e4': '0' ,
           }
move = ('e4','e3','m')
factor = -1

undoMove2(position, move, factor)
# move[0] = 'g' or 't'
# move[1] = '0'


# In[39]:


def undoMove3(boardPosition, move, factor):
    holdMove = []
    
    if factor == -1:
        if move[2] == 'p':
            boardPosition.update({move[1]:'0'})
        else:
            for position in boardPosition.keys():
                if move[0] == position:
                    if boardPosition[position] == '0':
                        holdMove.append(position)
        
            for piecePosition in boardPosition.keys():
                if move[1] == piecePosition:
                    if boardPosition[piecePosition] != '0':
                        holdMove.append(boardPosition[piecePosition])
                        holdMove.append(piecePosition)
            
            if move[2] == 'm':
                boardPosition.update({move[0]:boardPosition[move[1]]})
                boardPosition.update({move[1]:'0'})
            else:
                boardPosition.update({holdMove[0]:holdMove[1]})
                boardPosition.update({holdMove[2]:'0'})
            
        print(holdMove)

    return boardPosition

position = {                            'b0': '0' , 
                'a1': 'g' , 'b1': 'g' , 'c1': 't' , 'd1': '0' , 'e1': 'g' , 'f1': 't' , 
                'a2': '0' , 'b2': '0' , 'c2': '0' , 'd2': 'g' , 'e2': '0' , 'f2': '0' ,
                'a3': 't' , 'b3': 'g' , 'c3': '0' , 'd3': '0' , 'e3': 'g' , 'f3': 't' ,
                            'b4': '0' , 'c4': 'g' , 'd4': '0' , 'e4': '0' ,
           }
move = ('e2','e1','m')
#move = ('0','f1','p')
#move = ('c3','c1','c')
factor = -1

undoMove3(position, move, factor)
# Undo placement
#    move[1] = '0'
# Undo movement
#    move[0] = 'g' or 't'
#    move[1] = '0'
# Undo capture
#    move[0] = 't'
#    move[1] = '0'
#    move[1] - move[0] = 'g'


# In[11]:


def undoMove4(boardPosition, move, factor):
    holdMove = []
    
    for position in boardPosition.keys():
        if position == move[0]:
            if boardPosition[position] == '0':
                break
            if boardPosition[position] == '0':
                break
            if move[2] == 'p':
                boardPosition.update({move[1]:'0'})
            elif move[2] == 'm':
                boardPosition.update({move[0]:boardPosition[move[1]]})
                boardPosition.update({move[1]:'0'})
            else:
                print('c')
    
    return boardPosition

position = {                            'b0': '0' , 
                'a1': 'g' , 'b1': 'g' , 'c1': 't' , 'd1': '0' , 'e1': 'g' , 'f1': 't' , 
                'a2': '0' , 'b2': '0' , 'c2': '0' , 'd2': 'g' , 'e2': '0' , 'f2': '0' ,
                'a3': 't' , 'b3': 'g' , 'c3': '0' , 'd3': '0' , 'e3': 'g' , 'f3': 't' ,
                            'b4': '0' , 'c4': 'g' , 'd4': '0' , 'e4': '0' ,               }
move = ('e4','e3','m')
factor = -1

undoMove4(position, move, factor)


# In[ ]:




