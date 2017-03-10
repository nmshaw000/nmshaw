package nmshaw

import (
	"bytes"
	"github.com/PuerkitoBio/goquery"
	"io"
	"strings"
	"text/template"
)

type Event struct {
	Date  string
	Descr string
}

var rsttable = `
.. list-table::
{{range $event := .}}
   * - {{$event.Date}}
     - {{$event.Descr}}
{{end}}
`

func AnchorToRst(a *goquery.Selection) string {
	href, ok := a.Attr("href")
	if !ok {
		panic("a has no href")
	}
	return "`" + strings.TrimSpace(a.Text()) + " <" + href + ">`__"
}

func ParseTr(tr *goquery.Selection) (evt Event) {
	tr.Find("a").Each(func(i int, a *goquery.Selection) {
		if i == 0 {
			evt.Date = AnchorToRst(a)
		} else if i == 1 {
			evt.Descr = AnchorToRst(a)
		} else {
			panic("bad index")
		}
	})
	if evt.Date != "" {
		return
	}
	tr.Find("td").Each(func(i int, td *goquery.Selection) {
		if i == 0 {
			evt.Date = strings.TrimSpace(td.Text())
		} else if i == 1 {
			evt.Descr = strings.TrimSpace(td.Text())
		} else {
			panic("bad index")
		}
	})
	if evt.Date == "" {
		panic("strange tr")
	}
	return
}

func ParseFromReader(r io.Reader) (result string, err error) {
	doc, err := goquery.NewDocumentFromReader(r)
	if err != nil {
		return
	}

	var events []Event
	doc.Find("tr").Each(func(i int, tr *goquery.Selection) {
		events = append(events, ParseTr(tr))
	})

	var b bytes.Buffer
	t := template.Must(template.New("rst").Parse(rsttable))
	err = t.Execute(&b, events)
	if err != nil {
		return
	}
	result = b.String()

	return
}
