    "*** YOUR CODE HERE ***"
    # 获得当前pacman的初始状态
    startNode = problem.getStartState()
    # 检测初始状态是否正好为目标状态
    if problem.isGoalState(startNode):
        return []

    # 构造搜索树
    myStack = util.Stack()
    visitedNode = []
    # 搜索树的节点结构为（当前状态，[actions]从初始状态到达当前状态经过的动作集合）
    myStack.push((startNode, []))

    # 对搜索树进行遍历，如果遍历结束仍未找到解即返回无解
    while not myStack.isEmpty():
        currentNode, action = myStack.pop()
        if not (currentNode in visitedNode):
            visitedNode.append(currentNode)

            if problem.isGoalState(currentNode):
                return action

            # 扩展搜索树
            for nextNode, nextAction, cost in problem.getSuccessors(currentNode):
                newAction = action + [nextAction]
                myStack.push((nextNode, newAction))

    util.raiseNotDefined()
