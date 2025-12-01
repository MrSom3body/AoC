package main

import (
	"github.com/MrSom3body/AoC/aoclib"
)

func task1(grid [][]string) int {
	count := 0
	for _, row := range grid {
		for _, col := range row {
		}
	}
	return count
}

func main() {
	aoclib.Output(task1(aoclib.LinesTo2D(aoclib.ReadInput("./x.in"), "")))
}
