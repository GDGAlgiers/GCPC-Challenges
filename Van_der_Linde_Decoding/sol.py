match=1
mismatch=-1
Indel=-2 # Add
L ="""ARTHURT AHURT 
TITA TATI
ARE ASE 
NON ONO 
YES YOS 
NI NAGG"""
Translate=  {
1 : 'I',
3 : 'D',
0: ' ',
10: 'E',
-7: 'L',
-2 :'L',
-4: 'N'
}


def GetPairs(Message):
  lines=Message.split('\n')
  pairs=[]
  for line in lines:
    seq1, seq2 = line.split()  # Split each line into seq1 and seq2
    pairs.append([seq1, seq2]) 
  return pairs
pairs=GetPairs(L)

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