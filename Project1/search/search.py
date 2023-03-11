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
import game
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):        #获取初始位置
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):   #目标状态:能否继续当前行进方向
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.

        状态：搜索状态
        当且仅当状态是有效的目标状态时，返回True。
        """
        util.raiseNotDefined()

    def getSuccessors(self, state): #返回（当前状态，动作，路径大小）
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.

        状态：搜索状态
        对于给定的状态，这应该返回一个三元组列表，action，stepCost），其中“继任者”是当
        前的继任者state，“action”是到达目的地所需的操作，“stepCost”是扩大到继任者的增量成本。
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):    #所有行进路线
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
    return  [s, s, w, s, w, w, s, w]

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

    start_states = problem.getStartState()  #获取初始状态
    end_states = []                         #收集走过节点
    states = util.Stack()                   #调用栈方法设置搜索树
    states.push((start_states,[]))          #将当前状态和下一状态集合收集
    while states.isEmpty() == 0 and problem.isGoalState(start_states) == False:   #判断当前状态是否处于目标状态或不可执行状态
        state,actions = states.pop()        #删除末状态并传递给state和actions
        end_states.append(state)            #动作列表中添加当前状态
        Successors = problem.getSuccessors(state)   #实例化当前的状态、动作、路径
        for stated in Successors:
            x = stated[0]                   #获取当前状态
            y = stated[1]                   #获取当前动作
            if x not in end_states:         #判断当前状态是否已经搜索过
                states.push((x,actions + [y]))  #将当前状态以及下一步搜索方向传递到搜索树
            start_states = x                #当前状态作为下一次循环的初始状态
    return actions + [y]
    util.raiseNotDefined()



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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
