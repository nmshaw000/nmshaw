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

function RemoveColgroup() {
  var colgroups = document.querySelectorAll("colgroup");
  for (var i = 0; i < colgroups.length; ++i) {
    colgroups[i].remove();
  }
}

document.addEventListener("DOMContentLoaded", function(event) {
  PlaySequential();
  RemoveColgroup();
});
