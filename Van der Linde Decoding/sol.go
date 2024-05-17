package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func initiateMatrix(Seq1 string, Seq2 string, Indel int) [][]string {
	var LengthSeq1 = len(Seq1)
	var LengthSeq2 = len(Seq2)

	Matrix := make([][]string, LengthSeq1+2)
	for i := range Matrix {
		Matrix[i] = make([]string, LengthSeq2+2)
	}
	for i := 0; i < len(Matrix); i++ {
		for j := 0; j < len(Matrix[0]); j++ {
			Matrix[i][j] = "0"
		}
	}
	Matrix[0][0] = "/"
	Matrix[0][1] = "i"
	Matrix[1][0] = "j"

	for i := 0; i < LengthSeq1; i++ {
		Matrix[i+2][0] = string(Seq1[i])
	}
	for i := 0; i < LengthSeq2; i++ {
		Matrix[0][i+2] = string(Seq2[i])
	}
	for i := 0; i < len(Matrix)-2; i++ {
		Value, _ := strconv.Atoi(Matrix[i+1][1])
		Mat_Value := Indel + Value
		Matrix[i+2][1] = strconv.Itoa(Mat_Value)
	}
	for j := 0; j < LengthSeq2; j++ {
		Value, _ := strconv.Atoi(Matrix[1][j+1])
		Mat_Value := Indel + Value
		Matrix[1][j+2] = strconv.Itoa(Mat_Value)
	}

	return Matrix
}

func get_Params() ([][]string, map[string]string, int, int, int, int) {
	pairs := make([][]string, 100)
	for i := range pairs {
		pairs[i] = make([]string, 100) // Initializing each row with a slice of 3 integers
	}
	translate := make(map[string]string)
	nbrline := 0
	match := 0
	mismatch := 0
	indel := 0
	scanner := bufio.NewScanner(os.Stdin)
	n := 0
	m := 0
	index := 0

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		if nbrline == 0 {
			n, _ = strconv.Atoi(line)
		}
		if nbrline == 1 {
			m, _ = strconv.Atoi(line)
		}
		if nbrline > 1 {
			if nbrline <= n+1 {
				seq1 := strings.Split(line, " ")[0]
				seq2 := strings.Split(line, " ")[1]
				pairs[index] = []string{seq1, seq2}
				index++
			}
			if nbrline > n+1 && nbrline < n+m+2 {
				key := strings.Split(line, ":")[0]
				value := strings.Split(line, ":")[1]
				translate[key] = value
			}
			if nbrline == n+m+2 {
				match, _ = strconv.Atoi(line)
			}
			if nbrline == n+m+3 {
				mismatch, _ = strconv.Atoi(line)
			}
			if nbrline == n+m+4 {
				indel, _ = strconv.Atoi(line)
			}
		}
		nbrline = nbrline + 1
	}

	return pairs, translate, match, mismatch, indel, n
}

func FillMatrix(Matrix [][]string, Indel int, match int, mismatch int) [][]string {
	for i := 2; i < len(Matrix); i++ {
		for j := 2; j < len(Matrix[0]); j++ {
			diag, _ := strconv.Atoi(Matrix[i-1][j-1])
			left, _ := strconv.Atoi(Matrix[i][j-1])
			right, _ := strconv.Atoi(Matrix[i-1][j])
			if Matrix[i][0] == Matrix[0][j] {
				Max := max(diag+match, left+Indel, right+Indel)
				Matrix[i][j] = strconv.Itoa(Max)
			} else {
				Matrix[i][j] = strconv.Itoa(max(diag+mismatch, left+Indel, right+Indel))
			}
		}
	}
	return Matrix
}

func dehashMessage(pairs [][]string, n int, Indel int, match int, mismatch int, Translate map[string]string) string {
	RealMessage := ""
	for index := 0; index < n; index++ {
		Matrix := initiateMatrix(pairs[index][0], pairs[index][1], Indel)
		Matrix = FillMatrix(Matrix, Indel, match, mismatch)
		score := Matrix[len(Matrix)-1][len(Matrix[0])-1]
		value, exists := Translate[score]
		if exists {
			RealMessage = RealMessage + value
		}
	}
	return RealMessage
}

func main() {
	Pairs, translate, match, mismatch, indel, n := get_Params()
	RealMessage := dehashMessage(Pairs, n, indel, match, mismatch, translate)
	fmt.Println(RealMessage)
}
