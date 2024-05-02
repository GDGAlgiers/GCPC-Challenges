import sys

class Node:
   def __init__(self, sequence):
      self.children = []
      self.sequence = sequence


def insert(tree,sequence):
    child = Node(sequence)
    tree.children.append(child)
    return child
def smallestMotifIndex(motifs):
    smallestMotif = motifs[0]
    index = 0
    for i in range(len(motifs)):
        if(len(motifs[i]) < len(smallestMotif)):
            smallestMotif = motifs[i]
            index = i
    return index




def checkSubSequenceInMotifs(sequence, motifs, index):
    k = 0
    for i in range(len(motifs)): 
      k=0
      if (i == index) :
        continue
      
      j = 0
      while (j < len(motifs[i]) and k < len(sequence)):
        if (motifs[i][j] == sequence[k]):
          k=k+1
        j=j+1
        if (k == len(sequence)):
            break
      if (k< len(sequence)) :
        return False
  
    return True


def checkCommonSequenceExistenceInMotifs(sequence, motifs, index) :
	k = 0
	for i in range(len(motifs)):
		if (i != index ):
			k = 0
			for j in range(len(motifs[i])):
				for l in range(len(sequence)):
					if( motifs[i][j] == sequence[l] ):
						k = k + 1
						break
			if( k == 0 ):
				return False
			
	return True
def bfs(tree, motifs, index):
    longuest = 0
    open = [tree]
    motif =""
    closed = []
    solutions = []
    if (checkSubSequenceInMotifs(motifs[index], motifs, index)):
        solutions = [motifs[index]]
        return solutions
    while (len(open) > 0 ):
        longuestLocal = longuest
        motif = open[0]
        open=open[1:]
        for i in range(len(motif.sequence)):
            if(len(motif.sequence) > 1 ):
                subMotif = motif.sequence[:i] + motif.sequence[i+1:]
                if subMotif not in closed:
                    if (checkSubSequenceInMotifs(subMotif, motifs, index)):
                        longuestLocal = len(subMotif)
                        if (longuestLocal < longuest ):
                            break
                        longuest = longuestLocal
                        solutions.append(subMotif)
                    open.append(insert(motif,subMotif))
                    closed.append(subMotif)
                else:
                    continue
            if (longuestLocal < longuest):
                break
    return solutions

def calculateCodage(str, base):
    codage = 0
    for i, char in enumerate(str):
        char_code = ord(char) 
        codage += char_code * (base ** i) 

    return codage




lineIndex = 0
limit = 6
base =256
motifs = []
for line in sys.stdin:
    if lineIndex == 0:
        base = int(line)
    else:
        motifs.append(line.split('\n')[0])
    lineIndex += 1
    if lineIndex == limit:
        break
smallestIndex = smallestMotifIndex(motifs)
solutions = []
check = checkCommonSequenceExistenceInMotifs(motifs[smallestIndex], motifs, smallestIndex)
if (not check):
    print(0)
else:
    tree = Node(motifs[smallestIndex])
    solutions = bfs(tree, motifs, smallestIndex)      
    if(len(solutions)==0):
          print(0)
    else:
        maxCodage = calculateCodage(solutions[0], base)
        if (len(solutions) > 1) :
          motifsCoding = []
          biggerIndex = 0
          for j in range(1, len(solutions)):
                codage = calculateCodage(solutions[j], base)
                motifsCoding.append(codage)
                if (codage > maxCodage):
                  maxCodage = codage
                  biggerIndex = j
          motifsCoding = [value for value, index in enumerate(motifsCoding) if value == maxCodage]
          if(len(motifsCoding ) > 1):
                  maxCodage =maxCodage* len(motifsCoding)
          print(maxCodage)
        else:
          print(maxCodage)