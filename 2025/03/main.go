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

func task2(lines []string) int {
	return 0
}

func main() {
	// test input
	input := aoclib.ReadInput("./2025/03/x.in")
	aoclib.Output(task1(input))

	// normal input
	input = aoclib.ReadInput("./2025/03/i.in")
	aoclib.Output(task1(input))

	// // test input
	// input = aoclib.ReadInput("./2025/03/x.in")
	// aoclib.Output(task2(input))

	// // normal input
	// input = aoclib.ReadInput("./2025/03/i.in")
	// aoclib.Output(task2(input))
}
