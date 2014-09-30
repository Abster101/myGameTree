#!/usr/bin/env python
#Filename: alphaBeta.py
#Description: alphaBeta in Python
#Source:
def alphaBeta(node, depth, alpha, beta, maxmizingPlayer):
    move_list= board.generateMoves(node, maxmizingPlayer)
    if depth == 0:
        #return value of node
        return self.postionEvaluation(board,rules,player)
    if maxmizingPlayer:
        for move in move_list:
            board.makeMove(node)
            evaluation= -self.alphaBeta(child, depth-1, alpha, beta, false) 
            if evaluation >= beta:
                return beta
            else:
                alpha = evaluation
        return alpha
    else:
        for move in move_list:
            board.makeMove(node)
            evulation= self.alphaBeta(child, depth-1, alpha, beta, true)
            if evaluation >= beta:
                return beta
            else:
                beta = evaluation
        return beta 
