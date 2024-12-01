package main

import (
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func diff(a, b int) int {
	if a < b {
		return b - a
	}
	return a - b
}

func occurs(elem int, list []int) int {
	occurences := 0
	for _, current := range list {
		if current == elem {
			occurences += 1
		}
	}
	return occurences
}

func task1(data string) int {
	var d1, d2 []int
	difference := 0
	data = strings.TrimSpace(data)
	lines := strings.Split(data, "\n")

	for _, line := range lines {
		parts := strings.Fields(line)
		n1, _ := strconv.ParseInt(parts[0], 10, 32)
		n2, _ := strconv.ParseInt(parts[1], 10, 32)
		d1 = append(d1, int(n1))
		d2 = append(d2, int(n2))
	}

	sort.Sort(sort.IntSlice(d1))
	sort.Sort(sort.IntSlice(d2))

	for i, n1 := range d1 {
		difference += diff(n1, d2[i])
	}

	return difference
}

func task2(data string) int {
	s := 0
	var d1, d2 []int
	data = strings.TrimSpace(data)
	lines := strings.Split(data, "\n")

	for _, line := range lines {
		parts := strings.Fields(line)
		n1, _ := strconv.ParseInt(parts[0], 10, 32)
		n2, _ := strconv.ParseInt(parts[1], 10, 32)
		d1 = append(d1, int(n1))
		d2 = append(d2, int(n2))
	}

	for _, elem := range d1 {
		s += elem * occurs(elem, d2)
	}

	return s
}

func main() {
	content, err := os.ReadFile("./i.in")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Print(task2(string(content)))
}
