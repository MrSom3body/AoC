package main

import (
	"log"

	"github.com/MrSom3body/AoC/aoclib"
)

func task1(nums [][]int) int {
	count := 0
DOG:
	for _, row := range nums {
		asc := false
		desc := false
		last_col := row[0]
		for i, col := range row {
			if i != 0 {
				if aoclib.Diff(last_col, col) < 1 || aoclib.Diff(last_col, col) > 3 {
					continue DOG
				}

				if last_col < col {
					asc = true
				} else {
					desc = true
				}

				if asc == true && desc == true {
					continue DOG
				}
			}
			last_col = col
		}
		count += 1
	}
	return count
}

func task2(nums [][]int) int {
	count := 0

	for _, row := range nums {
		rCount := task1([][]int{row})
		if rCount == 0 {
			for i := range row {
				temp := make([]int, len(row))
				copy(temp, row)
				temp = append(temp[:i], temp[i+1:]...)
				rCount = task1([][]int{temp})
				if rCount == 1 {
					break
				}
			}
		}
		count += rCount
	}

	return count
}

func main() {
	// test input
	input, err := aoclib.StringsToInts2D(aoclib.LinesTo2D(aoclib.ReadInput("./x.in")))
	if err != nil {
		log.Fatal(err)
	}
	aoclib.Output(task2(input))

	// normal input
	input, err = aoclib.StringsToInts2D(aoclib.LinesTo2D(aoclib.ReadInput("./i.in")))
	if err != nil {
		log.Fatal(err)
	}
	aoclib.Output(task2(input))
}
