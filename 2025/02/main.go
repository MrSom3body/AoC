package main

import (
	"strconv"

	"github.com/MrSom3body/AoC/aoclib"
	"github.com/dlclark/regexp2"
)

func regexp2FindAllString(re *regexp2.Regexp, s string) []*regexp2.Match {
	var matches []*regexp2.Match
	m, _ := re.FindStringMatch(s)
	for m != nil {
		matches = append(matches, m)
		m, _ = re.FindNextMatch(m)
	}
	return matches
}

func task1(lines []string) int {
	invalid := 0
	line := lines[0]
	idPattern := regexp2.MustCompile(`(\d+)\-(\d+),?`, regexp2.None)
	duplicatePattern := regexp2.MustCompile(`^(\d+)\1{1}$`, regexp2.None)
	for _, match := range regexp2FindAllString(idPattern, line) {
		start, _ := strconv.Atoi(match.GroupByNumber(1).String())
		end, _ := strconv.Atoi(match.GroupByNumber(2).String())
		for i := start; i <= end; i++ {
			iStr := strconv.Itoa(i)
			isDuplicate, _ := duplicatePattern.MatchString(iStr)
			if isDuplicate && len(iStr)%2 == 0 {
				invalid += i
			}
		}
	}
	return invalid
}
func task2(lines []string) int {
	invalid := 0
	line := lines[0]
	idPattern := regexp2.MustCompile(`(\d+)\-(\d+),?`, regexp2.None)
	duplicatePattern := regexp2.MustCompile(`^(\d+)\1+$`, regexp2.None)
	for _, match := range regexp2FindAllString(idPattern, line) {
		start, _ := strconv.Atoi(match.GroupByNumber(1).String())
		end, _ := strconv.Atoi(match.GroupByNumber(2).String())
		for i := start; i <= end; i++ {
			iStr := strconv.Itoa(i)
			isDuplicate, _ := duplicatePattern.MatchString(iStr)
			if isDuplicate {
				invalid += i
			}
		}
	}
	return invalid
}

func main() {
	// test input
	input := aoclib.ReadInput("./2025/02/x.in")
	aoclib.Output(task1(input))

	// normal input
	input = aoclib.ReadInput("./2025/02/i.in")
	aoclib.Output(task1(input))

	// test input
	input = aoclib.ReadInput("./2025/02/x.in")
	aoclib.Output(task2(input))

	// normal input
	input = aoclib.ReadInput("./2025/02/i.in")
	aoclib.Output(task2(input))
}
