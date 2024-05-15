const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});
// Indel=-2
// match=1
// mismatch=-1


process.stdin.setEncoding('utf8');

// let inputData = '';
// let inputArray=[]
// process.stdin.on('data', (chunk) => {
//     inputArray.push(chunk)
//     inputData += chunk;
// });
// process.stdin.on('end', () => {
//   // console.log(inputArray);
// });

const get_Params= async()=>{
 let pairs = []
 let translate = {}
 let nbrline = 0
 let match = 0
 let mismatch = 0
 let indel = 0
 const processComplete = new Promise((resolve) => {
  rl.on('line', (line) => {
    line = line.trim();
    if (nbrline == 0) {
       n = Number(line)   
      } 
    else if (nbrline == 1 ){
      m = Number(line)
  }
     if( nbrline > 1){
    if (nbrline <= n + 1){
        [seq1, seq2] = line.split(' ');
        pairs.push([seq1, seq2])
      }
    if( nbrline > n + 1 && nbrline < n + m + 2){
       [ key, value] = line.split(':')
        // translate.setdefault(Number(key), value)
        translate[Number(key)] = value;
      }
    if (nbrline == n + m + 2)
        match = Number(line)
    if (nbrline == n + m + 3)
        mismatch = Number(line)
    if (nbrline == n + m + 4)
        indel = Number(line)
  }
  nbrline++
  });

  rl.on('close', () => {
      resolve([pairs, translate, match, mismatch, indel]);
  });
});


 return await processComplete;
}

(async () => {
  const [pairs, translate, match, mismatch, indel] = await get_Params();
  RealMessage=dehashMessage(pairs,translate,indel,mismatch,match)
  console.log(RealMessage)
})();

const dehashMessage=(pairs,Translate,Indel,Mismatch,Match)=>{
  let RealMessage=''
  for(let i=0;i<pairs.length;i++){
    Matrix=[]
    Matrix=initiateMatrix(seq1=pairs[i][0],seq2=pairs[i][1],Indel)
    Matrix=FillMatrix(Matrix,Indel,Mismatch,Match)
    score=Matrix[Matrix.length -1 ][Matrix[0].length -1 ]
    if (Translate[score]) {
      RealMessage=RealMessage+Translate[score]
    }
  }

  return RealMessage 
}
   


const FillMatrix=(Matrix,Indel,Mismatch,Match)=>{
 for (i=2;i<Matrix.length ; i++) {
  for (j=2;j<Matrix[0].length ; j++) {
    if(Matrix[i][0] == Matrix[0][j] ) 
    Matrix[i][j]=Math.max(Matrix[i-1][j-1]+ Match,Matrix[i][j-1]+Indel,Matrix[i-1][j]+Indel)
   else 
    Matrix[i][j]=Math.max(Matrix[i-1][j-1]+ Mismatch,Matrix[i][j-1]+Indel,Matrix[i-1][j]+Indel)
  }
 }
 return Matrix
}

const initiateMatrix=(seq1,seq2,Indel)=> {
 let rows = seq2.length+2;
 let cols = seq1.length+2;
 let Matrix = new Array(rows);
 for (let i = 0; i < rows; i++) {
  Matrix[i] = new Array(cols).fill(0);
}
  Matrix[0][0]='/'
  Matrix[0][1]='i'
  Matrix[1][0]='j'
  Matrix[1][1]=0
  let j=2
  for (let i=0 ; i<seq1.length;i++){
    Matrix[0][j]=seq1[i]
    j++
  }
  j=2
  for (let i=0 ; i<seq2.length;i++){
    Matrix[j][0]=seq2[i]
    j++
  }
  for (let i=2 ; i<Matrix[0].length;i++){
    Matrix[1][i]=Matrix[1][i-1] + Indel 
  }
  for (let i=2 ; i<Matrix.length;i++){
    Matrix[i][1]=Matrix[i-1][1] + Indel 
  }
  return Matrix
}

const Show_Matrix=(Matrix)=>{
 for (let i=0 ; i<Matrix.length ; i++){
  for (let j=0; j<Matrix[0].length;j++){
    process.stdout.write(String(Matrix[i][j]) + "\t" )
  }
  console.log("\n")
 }
}
// let Matrix = initiateMatrix('SETIN','SETING',-2)
// Matrix=FillMatrix(Matrix,-2,-1,1)
// Show_Matrix(Matrix)


