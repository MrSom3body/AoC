package aoclib

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
)

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