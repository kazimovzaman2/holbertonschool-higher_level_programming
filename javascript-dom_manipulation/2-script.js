document.addEventListener("DOMContentLoaded", function() {
  const redHeader = document.getElementById("red_header");
  redHeader.addEventListener("click", function() {
    const header = document.querySelector("header");
    header.classList.add("red");
  });
});
