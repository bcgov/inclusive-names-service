package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"strconv"
	"strings"
	"unicode/utf8"

	"github.com/clipperhouse/uax29/graphemes"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	readFile, err := os.Open("../utf8.txt")
	check(err)

	f, err := os.Create("./output.txt")
	check(err)

	defer f.Close()

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line := fileScanner.Text()
		fmt.Printf("String: %s\n", line)
		_, err := f.WriteString("String: " + line + "\n")
		check(err)

		fmt.Printf("String type: %s\n", reflect.TypeOf(line))
		_, err = f.WriteString("String type: " + reflect.TypeOf(line).Name() + "\n")
		check(err)

		splitList := strings.Split(line, "")
		fmt.Printf("List: %s\n", strings.Join(splitList, ", "))
		_, err = f.WriteString("List: " + strings.Join(splitList, ", ") + "\n")
		check(err)

		//note the use of []rune here as is in incorrect without it
		fmt.Printf("Length: %d\n", len([]rune(line)))
		_, err = f.WriteString("Length: " + strconv.Itoa(len([]rune(line))) + "\n")
		check(err)

		//and here
		fmt.Printf("Seventh character: %s\n", string([]rune(line)[6]))
		_, err = f.WriteString("Seventh character: " + string([]rune(line)[6]) + "\n")
		check(err)

		segments := graphemes.NewSegmenter([]byte(line))

		graphLine := ""
		graphSlice := []rune("")
		for segments.Next() {
			graphLine = graphLine + string(segments.Bytes()) + ", "
			r, _ := utf8.DecodeRune(segments.Bytes())
			graphSlice = append(graphSlice, r)
		}
		graphLine = graphLine[:len(graphLine)-2]
		fmt.Printf("Graphemes: %s\n", graphLine)
		_, err = f.WriteString("Graphemes: " + graphLine + "\n")

		fmt.Printf("Graphemes Length: %d\n", len(graphSlice))
		_, err = f.WriteString("Graphemes Length: " + string(len(graphSlice)) + "\n")

		fmt.Printf("\n")
		_, err = f.WriteString("\n")
		check(err)
	}

	f.Sync()

}
