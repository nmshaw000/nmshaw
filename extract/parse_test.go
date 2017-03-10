package nmshaw

import (
	"os"
	"testing"
)

func TestParse(t *testing.T) {
	path := "honor.html"
	f, err := os.Open(path)
	if err != nil {
		t.Error(err)
		return
	}
	defer f.Close()

	result, err := ParseFromReader(f)
	if err != nil {
		t.Error(err)
		return
	}
	println(result)
}
