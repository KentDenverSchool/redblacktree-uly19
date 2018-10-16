#Ulysses Atkeson, 10/15/18, Implement Some of a isRBTNode
import math
class Node:
    def __init__(self, keyIn, valueIn):
        self.key = keyIn
        self.value = valueIn
        self.left = None
        self.right = None
        self.black = False

    def __repr__(self):
        return "Node{ key : " + str(self.key) + ", value : " + str(self.value) + ", black : " + str(self.black) + "}"

    def getKey(self):
        return self.key
    def setKey(self, keyIn):
        self.key = keyIn
    def getValue(self):
        return self.value
    def setValue(self, valueIn):
        self.value = valueIn

    def getLeft(self):
        return self.left
    def setLeft(self, nodeIn):
        self.left = nodeIn
    def getRight(self):
        return self.right
    def setRight(self, nodeIn):
        self.right = nodeIn

    def blackHeightCheck(self, heightIn):
        if self.black:
            heightIn = heightIn - 1
        if self.getLeft() == None and heightIn!=0:
            return False
        if self.getRight() == None and heightIn!=0:
            return False
        if self.getLeft() != None and self.getLeft().blackHeightCheck(heightIn)==False:
            return False
        if self.getRight() != None and self.getRight().blackHeightCheck(heightIn)==False:
            return False
        return True

class Red_Black_Tree:
    def __init__(self):
        self.root = Node(None, None)
    def rotateRight(self, nodeIn):
        if nodeIn.getLeft() == None:
            return None
        else:
            nodeOut = nodeIn.getLeft()
            nodeIn.setLeft(nodeOut.getRight())
            nodeOut.setRight(nodeIn)
            return nodeOut
    def rotateLeft(self, nodeIn):
        if nodeIn.getRight() == None:
            return None
        else:
            nodeOut = nodeIn.getRight()
            nodeIn.setRight(nodeOut.getLeft())
            nodeOut.setLeft(nodeIn)
            return nodeOut
    def isGParrent(self, nodeIn):
        left = False
        right = False
        if nodeIn.getLeft() != None:
            left = (nodeIn.getLeft().getLeft() != None) or (nodeIn.getLeft().getRight() != None)
        if nodeIn.getRight() != None:
            right = (nodeIn.getRight().getLeft() != None) or (nodeIn.getRight().getRight() != None)
        return left or right

    def size(self):
        return self.__size(self.root)

    def __size(self, nodeIn):
        if nodeIn == None or nodeIn.getKey() == None:
            return 0
        left = nodeIn.getLeft() == None
        right = nodeIn.getRight() == None
        if left & right:
            return 1
        elif right:
            return 1 + self.__size(nodeIn.getLeft())
        elif left:
            return 1 + self.__size(nodeIn.getRight())
        else:
            return 1 + self.__size(nodeIn.getRight()) + self.__size(nodeIn.getLeft())

    def isEmpty(self):
        return self.size() == 0

    def put(self, keyIn, valueIn):
        if self.root.getKey() == None:
            self.root = Node(keyIn, valueIn)
        else:
            self.root = self.__put(self.root, keyIn, valueIn)

    def __put(self, nodeIn, keyIn, valueIn):
        if nodeIn == None or nodeIn.getKey() == None:
            return Node(keyIn, valueIn)
        else:
            if keyIn > nodeIn.getKey():
                nodeIn.setRight(self.__put(nodeIn.getRight(), keyIn, valueIn))
            else:
                nodeIn.setLeft(self.__put(nodeIn.getLeft(), keyIn, valueIn))
            return nodeIn

    def get(self, keyIn):
        return self.__get(self.root, keyIn)

    def __get(self, curNode, keyIn):
        if curNode == None:
            return None
        if curNode.getKey() == keyIn:
            return curNode.getValue()
        elif curNode.getKey() < keyIn:
            if curNode.getRight() == None:
                return None
            return self.__get(curNode.getRight(), keyIn)
        elif curNode.getKey() > keyIn:
            if curNode.getLeft() == None:
                return None
            return self.__get(curNode.getLeft(), keyIn)

    def contains(self, keyIn):
        return self.get(keyIn) != None

    def remove(self, keyIn):
        value = self.get(keyIn)
        self.root = self.__remove(self.root, keyIn)
        return value

    def __remove(self, nodeIn, keyIn):
        if nodeIn == None:
            return None
        if keyIn < nodeIn.getKey():
            nodeIn.setLeft(self.__remove(nodeIn.getLeft(), keyIn))
        elif keyIn > nodeIn.getKey():
            nodeIn.setRight(self.__remove(nodeIn.getRight(), keyIn))
        else:
            if nodeIn.getRight() == None:
                return nodeIn.getLeft()
            if nodeIn.getLeft() == None:
                return nodeIn.getRight()
            min = self.__min(nodeIn.getRight())
            min.setLeft(nodeIn.getLeft())
            nodeIn = nodeIn.getRight()
        return nodeIn

    def min(self):
        return self.__min(self.root).getKey()

    def __min(self, nodeIn):
        if nodeIn.getLeft() == None:
            return nodeIn
        else:
            return self.__min(nodeIn.getLeft())

    def max(self):
        return self.__max(self.root).getKey()

    def __max(self, nodeIn):
        if nodeIn.getRight() == None:
            return nodeIn
        else:
            return self.__max(nodeIn.getRight())

    def __repr__(self):
        return self.toString(self.root)

    def toString(self, nodeIn): #based on Grant
        if(nodeIn==None):
            return "x"
        left = self.toString(nodeIn.getLeft())
        right = self.toString(nodeIn.getRight())
        width = max(len(left.split("\n")[0]), len(right.split("\n")[0]))
        halfWidth = math.floor(width/2)

        stringOut = halfWidth * " " + "|" +(width-halfWidth-1) * "-" + str(nodeIn.key) + (width-halfWidth-1) * "-" + "|" + halfWidth * " "+"\n"
        
        leftArr=left.split('\n')
        rightArr=right.split("\n")

        for i in range(0,max(len(leftArr),len(rightArr))):
            if(len(leftArr)>i):
                smallSideWidth=math.floor((width-len(leftArr[i]))/2)
                stringOut+=smallSideWidth*" "
                stringOut+=leftArr[i]
                stringOut+=(width-len(leftArr[i])-smallSideWidth)*" "
            else:
                stringOut = stringOut + " "*(width)
            stringOut+=(( width + len(str(nodeIn.key)) + width)-width*2)*" "
            if(len(rightArr)>i):
                smallSideWidth=math.floor((width-len(rightArr[i]))/2)
                stringOut+=smallSideWidth*" "
                stringOut+=rightArr[i]
                stringOut+=(width-len(rightArr[i])-smallSideWidth)*" "
            else:
                stringOut = stringOut + " "*(width)
            stringOut = stringOut + "\n"
        return stringOut[:-1]

    def blackHeight(self):
        nodeIn = self.root
        blacNum = 1
        while(nodeIn.getLeft()!=None):
            nodeIn = nodeIn.getLeft()
            if nodeIn.black:
                blackNum = blacNum + 1
        return blackNum

def isRBT(rbt):
    if rbt.root.black == False:
        return False
    if rbt.root.blackHeightCheck(rbt.blackHeight()) == False:
        return False
    else:
        return isRBTNode(rbt.root)

def isRBTNode(nodeIn):
    if not nodeIn.black:
        if (nodeIn.getLeft() != None and (not nodeIn.getLeft().black)) or (nodeIn.getRight() != None and (not nodeIn.getRight().black)):
            return False
    if nodeIn.getLeft() != None and (not isRBTNode(nodeIn.getLeft())):
        return False
    if nodeIn.getRight() != None and (not isRBTNode(nodeIn.getRight())):
        return False
    return True

test = Red_Black_Tree() # from website
test.put(2,0)
test.put(1,0)
test.put(6,0)
test.put(4,0)
test.put(7,0)
test.put(3,0)
test.put(5,0)
test.put(8,0)
print(isRBT(test)) #false
test.root.getRight().black = True
print(isRBT(test)) #false
test.root.getRight().black = False
test.root.black = True
test.root.getLeft().black = True
test.root.getRight().getLeft().black = True
test.root.getRight().getRight().black = True
print(isRBT(test)) #true

test1 = Red_Black_Tree()
test1.put(10,1)
test1.put(5,2)
test1.put(15,3)
test1.put(4,4)
test1.put(6,5)
test1.put(14,6)
test1.put(16,7)
print(str(test1))
print()
print()
test1.root=test1.rotateRight(test1.root)
print(str(test1))
print()
print()
test1.root.setRight(test1.rotateLeft(test1.root.right))
print(str(test1))


