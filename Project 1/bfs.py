"""
Author : one of the TAs, just after
submitting an important journal manuscript.
I am so tired that I might have screwed up the following DFS implementation.
My fellow TAs are expected to fix all the errors
while I'm taking a very long nap.
I trust them but you should also, student,
check the following code against a possible *unique* error.
"""

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import PriorityQueue,manhattanDistance


def key(state):
    """
    Returns a key that uniquely identifies a Pacman game state.
    Arguments:
    ----------
    - `state`: the current game state. See FAQ and class
               `pacman.GameState`.
    Return:
    -------
    - A hashable key object that uniquely identifies a Pacman game state.
    """
    return (state.getPacmanPosition(),state.getFood())

def h(currentState):
    """
    Returns the mananhattan Distance between a state and the nearest dot
    Arguments:
    ----------
    -`currentState`(GameState): the current game state.
    Return:
    -------
    - the integer zero.
    """
    
    return 0


class PacmanAgent(Agent):
    """
    A Pacman agent based on Depth-First-Search.
    """

    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.moves = []

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.
        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.
        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """

        if not self.moves:
            self.moves = self.astar(state)

        try:
            return self.moves.pop(0)

        except IndexError:
            return Directions.STOP

    def astar(self, state):
        """
        Given a pacman game state,
        returns a list of legal moves to solve the search layout.
        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.
        Return:
        -------
        - A list of legal moves as defined in `game.Directions`.
        """
        path = []
        cost = 0
        fringe = PriorityQueue()
        fringe.push((state, path,cost),0)
        closed = set()

        while True:
            if fringe.isEmpty():
                return []  # failure

            f, (current,path,cost) = fringe.pop()

            if current.isWin():
                return path

            current_key = key(current)

            if current_key not in closed:
                closed.add(current_key)

                for next_state, action in current.generatePacmanSuccessors():
                    
                    if not current.getFood().__eq__(next_state.getFood()):
                        stepCost = 0
                    else :
                        stepCost = 0
                    fringe.push((next_state, path + [action],cost + stepCost),cost + stepCost +h(next_state))

        return path