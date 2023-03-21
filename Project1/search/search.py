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
    nowstates = util.Stack()                                                #now states
    everstates = []                                                                   #ever states
    nowstates.push((problem.getStartState(), []))  #insert start state
    while not nowstates.isEmpty():                               #if not none continue
        nownode, actions = nowstates.pop()              
        if problem.isGoalState(nownode):                    #if already in goal state return actions
            return actions
        if nownode not in everstates:                               #if now node not in ever node,continue
            successors = problem.getSuccessors(nownode) #goal states successors
            everstates.append(nownode)                          #ever states insert into now node
            for successor, action, stepCost in successors:    #push successors to
                if successor not in everstates:                       #if successor not in ever states,contiue
                    nowstates.push((successor, actions + [action]))#now states insert 
 
    # util.raiseNotDefined()



def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    st =problem.getStartState()             # huo qu chu shi zhuan tai 

    readystates=[]                   #yi jing sou suo guo de jie dian 

    states=util.Queue()           #jian li sou suo shu
    states.push((st,[]))

    while not states.isEmpty():    #bian li sou suo shu 
        state,action = states.pop()

        if problem.isGoalState(state):      #zhao dao mu biao zhuang tai fan hui xing dong 
                    return action            
        if state not in readystates:                
            readystates.append(state)
            for nextstate,nextaction,costlen in problem.getSuccessors(state):  # xin jie dian         zhuang tai ,xing dong ,chang du     zeng jia 
                if nextstate not in readystates:
                    nexaction = action + [nextaction]       #xia yi zhaung tai bu zai    yizhi zhaung tai li ,xinwen   juli  zeng  jia
                    states.push((nextstate,nexaction))

    return action
    
    # util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startNode = problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    
    myCostQueue = util.PriorityQueue()
    visitedNode = []
    myCostQueue.push((startNode, []), 0)
    
    while not myCostQueue.isEmpty():
        currentNode, action = myCostQueue.pop()
        if not (currentNode in visitedNode):
            visitedNode.append(currentNode)
            
            if problem.isGoalState(currentNode):
                return action
        
            for nextNode, nextAction, cost in problem.getSuccessors(currentNode):
                newAction = action + [nextAction]
                newCost = problem.getCostOfActions(newAction)
                myCostQueue.push((nextNode, newAction), newCost)  

    # util.raiseNotDefined()



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startNode = problem.getStartState() # 获取当前状态
    startPriority = heuristic(startNode, problem) + 0   # 计算距离函数
    if problem.isGoalState(startNode):          # 判断是否终点就是起点
        return []
    
    myQueue = util.PriorityQueue()          # 优先队列
    visitedNode = []                        # 记录已经访问过的位置
    myQueue.push((startNode, [], 0), startPriority)  # 添加开始位置和距离
    
    while not myQueue.isEmpty():        # 如果优先队列不为空
        currentNode, action, preCost = myQueue.pop()    # 记录当前位置，行为，cost
        if not (currentNode in visitedNode):    # 如果当前节点未访问过
            visitedNode.append(currentNode)         # 将当前节点添加到已访问节点列表
            
            if problem.isGoalState(currentNode):        # 如果是终点，返回行为
                return action
        
            for nextNode, nextAction, nextCost in problem.getSuccessors(currentNode):   # 遍历当前节点的后继函数
                newAction = action + [nextAction]                       # 
                newCost = problem.getCostOfActions(newAction)               # 获取新的节点的距离
                newPriority = newCost + heuristic(nextNode, problem)    # 获取后继节点中的优先级
                myQueue.push((nextNode, newAction, newCost), newPriority)  # 将后继节点添加到优先队列

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
