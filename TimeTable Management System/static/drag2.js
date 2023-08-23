function droppoint(event) {
  var data = event.dataTransfer.getData("Text");
  var draggedElement = document.getElementById(data);
  var clonedElement = draggedElement.cloneNode(true); // Clone the dragged element
  clonedElement.id = "cloned-" + data; // Set a new ID for the cloned element
  event.target.appendChild(clonedElement); // Append the cloned element to the drop target
  event.preventDefault();
}

function allowDropOption(event) {
  event.preventDefault();
}

function dragpoint(event) {
  event.dataTransfer.setData("Text", event.target.id);
}
