document.getElementById("settingsForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const data = {
        jira_email: document.getElementById("jira_email").value,
        jira_base_url: document.getElementById("jira_base_url").value,
        jira_api_token: document.getElementById("jira_api_token").value,
        board_id: document.getElementById("board_id").value,
        sprint_name: document.getElementById("sprint_name").value,
        openai_api_key: document.getElementById("openai_api_key").value
    };

    fetch("/save-settings/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error("Error:", error));
});
