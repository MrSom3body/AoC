package aoclib

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"strconv"
	"strings"
)

func Diff(a, b int) int {
	if a < b {
		return b - a
	}
	return a - b
}

func ReadInput(filePath string) []string {
	rawContent, err := os.ReadFile(filePath)
	if err != nil {
		log.Fatal(err)
	}

	content := string(rawContent)
	content = strings.TrimSpace(content)

	lines := strings.Split(content, "\n")

	return lines
}

func Output[Outputtable int | float32 | string](o Outputtable) {
	fmt.Println(o)
	cmd := exec.Command("wl-copy", fmt.Sprint(o))
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
	}
}

func LinesTo2D(lines []string, sep string) [][]string {
	var a [][]string
	for _, line := range lines {
		a = append(a, strings.Split(line, sep))
	}
	return a
}

func StringsToInts2D(strings [][]string) ([][]int, error) {
	var ints [][]int
	for _, row := range strings {
		var intRow []int
		for _, str := range row {
			num, err := strconv.Atoi(str)
			if err != nil {
				return nil, fmt.Errorf("error converting %q to int: %w", str, err)
			}
			intRow = append(intRow, num)
		}
		ints = append(ints, intRow)
	}
	return ints, nil
}
