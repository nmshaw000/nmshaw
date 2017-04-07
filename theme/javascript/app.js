'use strict';

var speed = 60;

function Playing(elements, elementIndex, textIndex) {
  if (elementIndex == elements.length) {
    return;
  }
  var element = elements[elementIndex];
  if (textIndex == element.dataset.typedtext.length) {
    setTimeout(Playing, speed, elements, elementIndex + 1, 0);
  } else {
    element.textContent += element.dataset.typedtext[textIndex];
    setTimeout(Playing, speed, elements, elementIndex, textIndex + 1);
  }
}

function PlaySequential() {
  var spans = document.querySelectorAll("span[data-typedtext]");
  Playing(spans, 0, 0);
}

document.addEventListener("DOMContentLoaded", function(event) {
  PlaySequential();
});
