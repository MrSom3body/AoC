package main

import (
	"fmt"
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

func task2(lines []string) int {
	var modLines []string
	p := regexp.MustCompile(".*?do()")
	line := "do()" + strings.Join(lines, " ")
	splitted := strings.Split(line, "don't()")
	for _, splittedLine := range splitted {
		fmt.Println(splittedLine)
		if strings.Contains(splittedLine, "do()") {
			loc := p.FindStringIndex(splittedLine)[1]
			modLines = append(modLines, splittedLine[loc:])
		}
	}
	fmt.Println(modLines)
	return task1(modLines)
}

func main() {
	// test input
	input := aoclib.ReadInput("./x.in")
	aoclib.Output(task2(input))

	// normal input
	input = aoclib.ReadInput("./i.in")
	aoclib.Output(task2(input))
}
