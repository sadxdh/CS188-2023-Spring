# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from searchAgents import PositionSearchProblem
    from pacman import GameState
    # from searchAgents import SearchAgent
    # wall location, startState, cost
    position = PositionSearchProblem(problem, GameState)
    state = position.getStartState

    visiteddict = position._visited  # dict status is visited
    # visitedlist = position._visitedlist  # dict status is visited list
    # isexpand = position._expanded  # the num of expended status

    import util
    stack = util.Stack

    successor = position.getSuccessors(state=state)


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from searchAgents import PositionSearchProblem
    from searchAgents import SearchAgent
    from pacman import GameState
    from game import Grid
    from game import Configuration
    from game import AgentState
    from game import Agent
    import util

    position = PositionSearchProblem(problem, gameState=GameState)
    start = position.getStartState  # start position
    state = start
    goal = position.goal
    curstate = GameState.getPacmanState()
    pos, direct = curstate[0], curstate[1]
    lockStack = util.Stack
    lockStack.push(state)
    while (pos != goal):
        su = GameState.generateSuccessor(pos, direct)
        for i in su:
            if (i not in lockStack):  # 不在表中
                .
                .
                .

        # 关键步骤　找出min G(n)表示的是从起始节点到gooal节点的距离代价。
        su.sort(key=getKeyforSort)
        state = su.pop(0)  # get min node
        lockStack.append(state)
    result = []                      # 准备输出结果
    while (state.father != None):    # 当父节点不为空时
        result.append(state.father)  # 追加父节点
        state = state.father               # 当前节点改为父节点
    result.append(state)   # 最后添加初始节点
    return result           # 返回路径列表


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
