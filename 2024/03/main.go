package main

import (
	"regexp"
	"strconv"
	"strings"

	"github.com/MrSom3body/AoC/aoclib"
)

func task1(lines []string) int {
	sum := 0
	p := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	for _, line := range lines {
		matches := p.FindAllStringSubmatch(line, -1)
		for _, lineMatches := range matches {
			n1, _ := strconv.Atoi(lineMatches[1])
			n2, _ := strconv.Atoi(lineMatches[2])
			sum += n1 * n2
		}
	}
	return sum
}

func main() {
	// test input
	input := aoclib.ReadInput("./x.in")
	aoclib.Output(task1(input))

	// normal input
	input = aoclib.ReadInput("./i.in")
	aoclib.Output(task1(input))
}
