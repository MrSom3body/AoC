package main

import (
	"log"
	"strconv"

	"github.com/MrSom3body/AoC/aoclib"
)

func task1(lines []string) int {
	zeroes := 0
	dial := 50
	limit := 100

	for _, line := range lines {
		direction := line[:1]
		val, err := strconv.Atoi(line[1:])
		if err != nil {
			log.Fatal(err)
		}

		remainder := val % limit

		delta := remainder
		if direction == "L" {
			delta = -remainder
		}

		target := dial + delta

		dial = ((target % limit) + limit) % limit

		if dial == 0 {
			zeroes++
		}
	}

	return zeroes
}

func task2(lines []string) int {
	zeroes := 0
	dial := 50
	limit := 100

	for _, line := range lines {
		direction := line[:1]
		val, err := strconv.Atoi(line[1:])
		if err != nil {
			log.Fatal(err)
		}

		zeroes += val / limit

		remainder := val % limit

		delta := remainder
		if direction == "L" {
			delta = -remainder
		}

		target := dial + delta

		if dial > 0 && (target <= 0 || target >= limit) {
			zeroes++
		}

		dial = ((target % limit) + limit) % limit
	}

	return zeroes
}

func main() {
	// test input
	input := aoclib.ReadInput("./x.in")
	aoclib.Output(task2(input))

	// normal input
	input = aoclib.ReadInput("./i.in")
	aoclib.Output(task2(input))
}
