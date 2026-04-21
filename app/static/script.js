let datasetSummary = null;

document.getElementById("uploadForm").onsubmit = async (e) => {
  e.preventDefault();

  const form = new FormData(e.target);
  document.getElementById("loading").classList.remove("hidden");

  const res = await fetch("/upload", {
    method: "POST",
    body: form
  });

  const data = await res.json();

  document.getElementById("loading").classList.add("hidden");

  // store summary for chatbot
  datasetSummary = data.summary;

  // dataset summary 
  document.getElementById("summary").textContent =
`
DATASET SUMMARY

Rows: ${data.summary.rows}

Columns:
${data.summary.columns.join(", ")}

Missing Values:
${JSON.stringify(data.summary.missing_values, null, 2)}

Numeric Summary:
${JSON.stringify(data.summary.numeric_summary, null, 2)}

Categorical Summary:
${JSON.stringify(data.summary.categorical_summary, null, 2)}

Date Range:
${JSON.stringify(data.summary.date_range, null, 2)}
`;

  // AI Insights 
  document.getElementById("insights").textContent = data.insights;
};


// Chat toggle
document.getElementById("chatIcon").onclick = () => {
  document.getElementById("chatPanel").classList.toggle("hidden");
};


async function ask() {

  let q = document.getElementById("question").value;
  if (!q || !datasetSummary) return;

  let chat = document.getElementById("chatWindow");

  chat.innerHTML += `<div class="user">${q}</div>`;

  let res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ summary: datasetSummary, question: q })
  });

  let data = await res.json();

  chat.innerHTML += `<div class="bot">${data.answer}</div>`;
  chat.scrollTop = chat.scrollHeight;

  document.getElementById("question").value = "";
}


// Press Enter to send message
const questionInput = document.getElementById("question");

questionInput.addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    ask();
  }
});
