package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

type Node struct {
	sequence string
	Children []*Node
}

func (tree *Node) insert(motif string) *Node {
	node := &Node{sequence: motif}
	tree.Children = append(tree.Children, node)
	return node
}

func smallestMotifIndex(motifs []string) int {
	smallestMotif := motifs[0]
	index := 0
	for i, motif := range motifs {
		if len(motif) < len(smallestMotif) {
			smallestMotif = motif
			index = i
		}
	}
	return index
}

func checkMotifInList(motif string, closed []string) bool {
	for _, s := range closed {
		if s == motif {
			return true
		}
	}
	return false
}

func checkSubSequenceInMotifs(sequence string, motifs []string, index int) bool {
	k := 0
	for i := 0; i < len(motifs); i++ {
		if i != index {
			k = 0
			for j := 0; j < len(motifs[i]); j++ {

				if motifs[i][j] == sequence[k] {
					k = k + 1
				}
				if k == len(sequence) {
					break
				}
			}
			if k < len(sequence) {
				return false
			}
		}
	}
	return true
}

func checkCommonSequenceExistenceInMotifs(sequence string, motifs []string, index int) bool {
	k := 0
	for i := 0; i < len(motifs); i++ {
		if i != index {
			k = 0
			for j := 0; j < len(motifs[i]); j++ {
				for l := 0; l < len(sequence); l++ {
					if motifs[i][j] == sequence[l] {
						k = k + 1
						break
					}
				}
				if k > 0 {
					break
				}
			}
			if k == 0 {
				return false
			}
		}
	}
	return true
}
func bfs(tree *Node, motifs []string, index int) []string {
	longuest := 0
	open := []*Node{}
	open = append(open, tree)
	closed := []string{}
	solutions := []string{}
	find := false
	find = checkSubSequenceInMotifs(motifs[index], motifs, index)
	if find {
		solutions = append(solutions, motifs[index])
		return solutions
	}
	for len(open) > 0 {
		longuestLocal := longuest
		motif := open[0]
		open = open[1:]
		for i := 0; i < len(motif.sequence); i++ {
			if len(motif.sequence) > 1 {
				subMotif := motif.sequence[:i] + motif.sequence[i+1:]
				if !checkMotifInList(subMotif, closed) {
					if checkSubSequenceInMotifs(subMotif, motifs, index) {
						longuestLocal = len(subMotif)
						if longuestLocal < longuest {
							break
						}
						longuest = longuestLocal
						solutions = append(solutions, subMotif)
					}
					open = append(open, tree.insert(subMotif))
					closed = append(closed, subMotif)
				} else {
					continue
				}
			}
		}
		if longuestLocal < longuest {
			break
		}
	}
	return solutions
}
func calculateCodage(str string, base int) int {
	codage := 0
	for i, char := range str {
		codage += int(char) * int(math.Pow(float64(base), float64(i)))
	}
	return codage
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var lineIndex int
	limit := 6
	var base int
	fmt.Scanf("%d\n", &base)
	fmt.Scanf("%d\n", &limit)
	base = int(base)
	lineIndex = 1
	var motifs []string
	for scanner.Scan() {
		motifs = append(motifs, scanner.Text())
		lineIndex++
		if lineIndex == limit+1 {
			break
		}
	}
	index := smallestMotifIndex(motifs)

	solutions := []string{}
	check := checkCommonSequenceExistenceInMotifs(motifs[index], motifs, index)
	if !check {
		fmt.Println(0)
		return
	} else {
		tree := &Node{sequence: motifs[index]}
		solutions = bfs(tree, motifs, index)
	}
	if len(solutions) == 0 {
		fmt.Println(0)
		return
	}
	maxCodage := calculateCodage(solutions[0], base)
	if len(solutions) > 1 {
		motifsCoding := []int{}

		for j := 1; j < len(solutions); j++ {
			codage := calculateCodage(solutions[j], base)
			motifsCoding = append(motifsCoding, codage)
			if codage > maxCodage {
				maxCodage = codage
			}
		}
		if len(motifsCoding) > 0 {
			maxMotifs := []int{}
			for _, s := range motifsCoding {
				if s == maxCodage {
					maxMotifs = append(maxMotifs, s)
				}
			}
			maxCodage = maxCodage * len(maxMotifs)
		}
		fmt.Println(maxCodage)
		return
	} else {
		fmt.Println(maxCodage)
		return
	}

}
