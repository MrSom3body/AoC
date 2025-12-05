package main

import (
	"strconv"
	"strings"

	"github.com/MrSom3body/AoC/aoclib"
)

func task1(lines []string) int {
	output_joltage := 0
	for _, line := range lines {
		string_joltages := strings.Split(line, "")
		joltages := make([]int, len(string_joltages))
		for i, j := range string_joltages {
			joltage, _ := strconv.Atoi(j)
			joltages[i] = joltage
		}

		jj := 0
		for i, j1 := range joltages {
			js1 := strconv.Itoa(j1)
			for _, j2 := range joltages[i+1:] {
				js2 := strconv.Itoa(j2)
				jj_str := js1 + js2
				new_jj, _ := strconv.ParseInt(jj_str, 10, 64)
				if int(new_jj) > jj {
					jj = int(new_jj)
				}
			}
		}

		output_joltage += int(jj)
	}
	return output_joltage
}

func sliceToInt(s []int) int {
	res := 0
	op := 1
	for i := len(s) - 1; i >= 0; i-- {
		res += s[i] * op
		op *= 10
	}
	return res
}

func findBiggestNumbers(numbers []int) int {
	var result []int

	start := 0
	itemsToPick := 12
	total := len(numbers)

	for i := range itemsToPick {
		remaining := itemsToPick - 1 - i
		end := (total - 1) - remaining

		bestDigit := -1
		bestIndex := -1

		for j := start; j <= end; j++ {
			val := numbers[j]
			if val > bestDigit {
				bestDigit = val
				bestIndex = j
			}
		}

		result = append(result, bestDigit)
		start = bestIndex + 1
	}

	return sliceToInt(result)
}

func task2(lines []string) int {
	joltage := 0
	for _, line := range lines {
		n := make([]int, len(line))
		for i, ch := range line {
			n[i], _ = strconv.Atoi(string(ch))
		}
		big := findBiggestNumbers(n)
		joltage += big
	}
	return joltage
}

func main() {
	// test input
	input := aoclib.ReadInput("./2025/03/x.in")
	aoclib.Output(task1(input))

	// normal input
	input = aoclib.ReadInput("./2025/03/i.in")
	aoclib.Output(task1(input))

	// test input
	input = aoclib.ReadInput("./2025/03/x.in")
	aoclib.Output(task2(input))

	// normal input
	input = aoclib.ReadInput("./2025/03/i.in")
	aoclib.Output(task2(input))
}
