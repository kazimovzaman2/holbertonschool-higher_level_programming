document.addEventListener("DOMContentLoaded", function() {
  const addItem = document.getElementById("add_item");
  addItem.addEventListener("click", function() {
    const ul = document.querySelector("ul.my_list");
    const li = document.createElement("li");
    li.textContent = "Item";
    ul.appendChild(li);
  });
});
