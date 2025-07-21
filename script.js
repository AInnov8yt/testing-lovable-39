document.getElementById("fetchData").addEventListener("click", function() {
  fetch("/api/data")
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").textContent = data.message;
    })
    .catch(error => {
      document.getElementById("result").textContent = "Error fetching data!";
      console.error("Error:", error);
    });
});