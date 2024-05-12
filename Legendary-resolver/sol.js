const readline = require('readline').createInterface({
    input: process.stdin,
  })
class Node{
    constructor(value){
        this.sequence = value
        this.children = []
    }
    insert(sequence,tree){
        let node = new Node(sequence)
        tree.children.push(node)
        return node
    }
}

function smallestMotifIndex(motif){
    let smallestMotif = motif[0]
    let index = 0
    for(let i = 1; i < motif.length; i++){
        if(motif[i].length < smallestMotif.length){
            smallestMotif = motif[i]
            index = i
        }
    }
    return index

}


function checkSubSequenceInMotifs(sequence, motifs, index) {
    let k = 0;
  
    for (let i = 0; i < motifs.length; i++) {
        k=0
      if (i === index) {
        continue;
      }
      let j = 0
      while (j < motifs[i].length && k < sequence.length) {
        if (motifs[i][j] === sequence[k]) {
          k++;
        }
        j++;
        if (k === sequence.length) {
        break
        }
      }
      if (k<sequence.length) {
        return false;
      }
    }
  
    return true;
  }

function checkCommonSequenceExistenceInMotifs(sequence, motifs, index)  {
	k = 0
	for( i = 0; i < motifs.length; i++) {
		if (i != index ){
			k = 0
			for (j= 0; j < motifs[i].length; j++ ){
				for( l = 0; l < sequence.length; l++ ){
					if( motifs[i][j] == sequence[l] ){
						k = k + 1
						break
					}
				}
			}
			if( k == 0 ){
				return false
			}
		}
	}
	return true
}
function bfs(tree, motifs, index) {
	longuest = 0
	open = [tree]
    motif =""
	closed = []
	solutions = []
	find = false
	find = checkSubSequenceInMotifs(motifs[index], motifs, index)
	if (find ){
		solutions = [motifs[index]]
		return solutions
	}
	while (open.length > 0 ){
		longuestLocal = longuest
		motif = open[0]
		open.splice(0, 1);
		for(i= 0; i < motif.sequence.length; i++){
			if (motif.sequence.length > 1 ){
				const subMotif = motif.sequence.slice(0, i) + motif.sequence.slice(i + 1);
				if (!closed.includes(subMotif)){
					if (checkSubSequenceInMotifs(subMotif, motifs, index)) {
						longuestLocal = subMotif.length
						if (longuestLocal < longuest ){
							break
						}
						longuest = longuestLocal
						solutions = [...solutions, subMotif];
					}
					open =[...open,tree.insert(subMotif,motif)] 
					closed =  [...closed,subMotif] 
				} else {
					continue
				}
			}
		}
		if (longuestLocal < longuest) {
			break
		}
	}
	return solutions
}

function calculateCodage(str, base) {
    let codage = 0;
    for (let i = 0; i < str.length; i++) {
      const charCode = str.charCodeAt(i);
      codage += charCode * Math.pow(base, i); 
    }
    return codage;
  }
const inputs = []
let index = 0
let limit = 6
let base = 256
let motifs =[]
readline.on('line', (line) => {
    if(index == 0){
        base = parseInt(line)
    }else if(index ==1){
      limit = parseInt(line) + 2
    }else{
        inputs.push(line)
    }
    if(index ==1){
      limit = parseInt(line) + 2
    }
    index++
    if (index == limit) {
      readline.close()
      motifs = inputs
      smallestIndex = smallestMotifIndex(motifs)
      solutions = []
      check = checkCommonSequenceExistenceInMotifs(motifs[smallestIndex], motifs, smallestIndex)
      if (!check) {
          console.log(0)
          return
      } else {
          tree = new Node(motifs[smallestIndex])
          solutions = bfs(tree, motifs, smallestIndex)
      }
      if(!solutions.length){
          console.log(0)
          return
      }
      maxCodage = calculateCodage(solutions[0], base)
      if (solutions.length > 1) {
          motifsCoding = []
          biggerIndex = 0
  
          for( j = 1; j < solutions.length; j++ ){
              codage = calculateCodage(solutions[j], base)
              motifsCoding = [...motifsCoding, codage]
              if (codage > maxCodage) {
                  maxCodage = codage
                  biggerIndex = j
              }
          }
              motifsCoding = motifsCoding.filter((value, index) => value === maxCodage)
              if(motifsCoding.length > 1){
                  maxCodage =maxCodage* motifsCoding.length
              }
              console.log(solutions)
          console.log(maxCodage)
      } else {
        console.log(solutions)
          console.log(maxCodage)
      }
  
    }
  })

