async function searchKeyword() {
      const input = document.getElementById("keyword").value;
      const resultDiv = document.getElementById("result");
      const errorText = document.getElementById("error");
      const def = document.getElementById("definition");
      const src = document.getElementById("source");

      resultDiv.style.display = "none";
      errorText.textContent = "";

      if (!input) {
        errorText.textContent = "Please enter a term to search.";
        return;
      }

      try {
        
        const response = await fetch(`https://50k5abucs9.execute-api.ap-south-1.amazonaws.com/prod/search?text=${encodeURIComponent(input)}`);
        
        if (!response.ok) {
          const errData = await response.json();
          errorText.textContent = errData.message || "Something went wrong.";
          return;
        }

        const data = await response.json();

        def.textContent = data.definition;
        src.textContent = data.source;
        resultDiv.style.display = "block";
      } catch (error) {
        errorText.textContent = "Failed to fetch definition. Please try again.";
      }
    }