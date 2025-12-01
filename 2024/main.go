package main

import "fmt"

func dog(s []string) {
	s[0] = "dog"
}

func main() {
	a := []string{"as", "asd"}
	fmt.Println(a)
	dog(a)
	fmt.Println(a)
}
