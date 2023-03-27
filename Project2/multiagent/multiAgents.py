# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.
        反射体通过检查在每个选择点上选择一个动作 通过状态评估函数来确定备选方案。

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
        下面的代码是作为指南提供的。欢迎你来改变 用任何你认为合适的方式，只要你不碰我们的方法 头。
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.
            您不需要更改此方法，但欢迎您更改。
        getAction chooses among the best options according to the evaluation function.
            Get行动根据评价函数在最佳选项中进行选择。
        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
            就像在前面的项目中一样，get操作获取一个游戏状态并返回 一些方向。对于集合中的某个X {n or th, so u th, w e s t, ea s t, s t o p}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.
            设计一个更好的评价函数。
        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.
            评估函数采用当前和建议的后继函数 游戏状态(pacman.py)并返回一个数字，其中数字越大越好。
        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
            下面的代码从状态中提取了一些有用的信息，比如 剩余食物(新食物)和移动后的吃豆人位置(新姿势)。 新的恐惧时间包含每个鬼魂将保持的移动次数 害怕是因为吃豆人吃了能量球。
        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
            打印出这些变量，看看你得到了什么，然后把它们组合起来 创建一个熟练的评估函数。
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.
        这个默认的评估函数只返回状态的分数。 分数是相同的一个显示在吃豆人g u i。
    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
        该评估函数用于对抗性搜索代理 (不是反射剂)。
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.
        这个类为您的所有应用程序提供了一些通用元素 多代理搜索器。这里定义的任何方法都是可用的 到minimmax pacman agent, alpha beta pacman agent和expectimax pacman agent。
    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.
        您“不”需要在这里做任何更改，但如果您愿意，可以这样做 为所有对抗性搜索代理添加功能。请不要 但是，移除任何东西。
    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
        注意:这是一个抽象类:不应该被实例化。这是 只是部分指定，并且设计为扩展。代理(game.py) 是另一个抽象类。
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
        你的极大极小代理(问题2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.
            使用self.depth从当前游戏状态返回极大极小动作 和自我。评价函数。
        Here are some method calls that might be useful when implementing minimax.
            下面是一些在实现minimmax时可能有用的方法调用。
        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1
            游戏状态。获得法律诉讼(代理索引): 返回代理的法律操作列表 Agent index=0表示吃豆人，ghosts = >= 1
        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action
            游戏状态。生成继承人(代理索引、动作): 返回代理执行操作后的后续游戏状态
        gameState.getNumAgents():
        Returns the total number of agents in the game
            游戏状态。获取num agents(): 返回游戏中代理的总数
        gameState.isWin():
        Returns whether or not the game state is a winning state
            游戏状态。是赢得(): 返回游戏状态是否是获胜状态
        gameState.isLose():
        Returns whether or not the game state is a losing state
            游戏状态。失去(): 返回游戏状态是否为失败状态
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
        你的带修剪的极大极小代理(问题3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
            返回使用self.depth和self的极大极小操作。评价函数
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
        你的expectimax代理(问题4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
            使用self.depth和self. max返回expectimax操作。评价函数
        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
            所有幽灵都应该被建模为从它们的幽灵中随机选择 法律行动。
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).
        你的极限捉鬼，抓球，吃东西，势不可挡 评价函数(问题5)。
    DESCRIPTION: <write something here so we know what you did>
        D e s c r I p t o n: <在这里写点什么，让我们知道你做了什么>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
