import sys

def get_Params():
    pairs = []
    translate = {}
    nbrline = 0
    match = 0
    mismatch = 0
    indel = 0
    
    for line in sys.stdin:
        line = line.strip()  # Remove leading/trailing whitespace
        
        if nbrline == 0:
            n = int(line)
            nbrline = 1
        elif nbrline == 1:
            m = int(line)
            nbrline = 2
        elif nbrline > 1:
            if nbrline <= n + 1:
                seq1, seq2 = line.split()
                pairs.append([seq1, seq2])
            elif nbrline > n + 1 and nbrline < n + m + 2:
                key, value = line.split(':')
                translate.setdefault(int(key), value)
            elif nbrline == n + m + 2:
                match = int(line)
            elif nbrline == n + m + 3:
                mismatch = int(line)
            elif nbrline == n + m + 4:
                indel = int(line)
                break
            nbrline=nbrline+1 
    return pairs, translate, match, mismatch, indel

pairs,Translate,match,mismatch,Indel=get_Params()
def FillMatrix(Matrix):
 for i in range(2,len(Matrix)):
  for j in range(2,len(Matrix[0])):
     if(Matrix[i][0] == Matrix[0][j] ) :
      Matrix[i][j]=max(Matrix[i-1][j-1]+ match,Matrix[i][j-1]+Indel,Matrix[i-1][j]+Indel)
     else : 
      Matrix[i][j]=max(Matrix[i-1][j-1]+ mismatch,Matrix[i][j-1]+Indel,Matrix[i-1][j]+Indel)
       
 return Matrix

def initiateMatrix(seq1,seq2):
  Matrix=[[0]*(len(seq1) + 2) for _ in range(len(seq2) + 2)]
  Matrix[0][0]='/'
  Matrix[0][1]='i'
  Matrix[1][0]='j'
  Matrix[1][1]=0
  j=2
  for i in seq1:
    Matrix[0][j]=i
    j=j+1
  j=2
  for i in seq2:
    Matrix[j][0]=i
    j=j+1  

  for i in range(2,len(Matrix[0])):
   Matrix[1][i]=Matrix[1][i-1] + Indel 
  for j in range(2,len(Matrix)):
    Matrix[j][1]=Matrix[j-1][1] + Indel 
  return Matrix

def dehashMessage(pairs):
  RealMessage=''
  for seqs in pairs :
   Matrix=[]
   Matrix=initiateMatrix(seqs[0],seqs[1])
   Matrix=FillMatrix(Matrix)
   score=Matrix[len(Matrix) -1 ][len(Matrix[0]) -1 ]
   if score in Translate : 
     RealMessage=RealMessage+Translate[score]
  return RealMessage 
   
RealMessage=dehashMessage(pairs)
print(RealMessage)