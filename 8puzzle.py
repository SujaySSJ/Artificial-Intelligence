import itertools
number=0
sol=[]
#moves=[1,-1,2,-2]
'''
left=1
right=-1
up=2
down=-2
'''
def makeMove(current_node,move):
    data=current_node.state
    index=[[row,sublist.index(0)] for row,sublist in enumerate(data) if 0 in sublist]
    #print(index)
    row,col=0,0
    for sublist in index:
        row=sublist[0]
        col=sublist[1]
    #print(data[row][col])    
    if move is 1 and col>0:
        data[row][col],data[row][col-1]=data[row][col-1],data[row][col]
        return data
    elif move is -1 and col<2:
        data[row][col],data[row][col+1]=data[row][col+1],data[row][col]
        return data
    elif move is 2 and row>0:
        data[row][col],data[row-1][col]=data[row-1][col],data[row][col]
        return data
    elif move is -2 and row<0:
        data[row][col],data[row+1][col]=data[row+1][col],data[row][col]
        return data
    return    




class TreeNode():
    def __init__(self,data,depth=0,child_type=0):
        global number
        self.state=data
        self.children=[]
        self.weight=self.setWeight()
        self.depth=depth
        self.id=number
        number=number+1
        self.type=child_type
    def addChild(self,c):
        self.children.append(c)
    def setWeight(self):
        global goal_state
        c=0
        for i,j in itertools.product([0,1,2],repeat=2):
            if(goal_state[i][j]!=self.state[i][j] and goal_state[i][j]!=0):
                c=c+1
        return c        
    def printChildren(self):
        for child in self.children:
            print(child.weight)
    def printNodeData(self):
        for i in [0,1,2]:
            for j in [0,1,2]:
                print(str(self.state[i][j])+" "),
            print("")
        print("Weight :"+str(self.weight))
        print("Depth :"+str(self.depth))
    def getBestChild(self):
        if self.children:
            pos=0
            min_weight=20
            for i in range(len(self.children)):
                if self.children[i].weight<=min_weight:
                    pos=i
            return self.children[pos]

                
def search(current_node,goal_node,depth,prev_move=0):
    #node=TreeNode(current_state,depth)
    if current_node.weight is 0:
        current_node.printNodeData()
        print("Solution found")
        return
    available_moves=[1,-1,2,-2]
    if prev_move is not 0:
        available_moves.remove(-prev_move)
    for move in available_moves:
        res=makeMove(current_node,move)
        if res:
            current_node.addChild(TreeNode(res,depth+1,move))
    next_node=current_node.getBestChild()
    global sol
    sol.append(next_node)
    if next_node:
        search(next_node,goal_node,depth+1,next_node.type)        

def test(current_node):
    print(current_node.weight)

goal_state=[[1,2,3],[8,0,4],[7,6,5]]
initial_state=[[1,2,3],[0,8,4],[7,6,5]]
goal_node=TreeNode(goal_state,0,0)
initial_node=TreeNode(initial_state,0,0)
search(initial_node,goal_node,0,0)
# node.addChild(TreeNode(20))
# node.addChild(TreeNode(20))
# node.addChild(TreeNode(20))

# node.printChildren()
#print(node)
#test(initial_node)
#node.printNodeData
for state in sol:
    print(state.state)