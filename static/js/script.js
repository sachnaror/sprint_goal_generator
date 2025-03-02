// static/js/script.js

document.addEventListener("DOMContentLoaded", function () {
    const jiraEmail = document.getElementById("jira_email");
    const jiraApiToken = document.getElementById("jira_api_token");
    const jiraBaseUrl = document.getElementById("jira_base_url");
    const openaiApiKey = document.getElementById("openai_api_key");
    const boardDropdown = document.getElementById("board_id");
    const sprintDropdown = document.getElementById("sprint_id");
    const generateButton = document.getElementById("generate_goals");

    // Load saved session data
    function loadSessionData() {
        jiraEmail.value = localStorage.getItem("jira_email") || "";
        jiraApiToken.value = localStorage.getItem("jira_api_token") || "";
        jiraBaseUrl.value = localStorage.getItem("jira_base_url") || "";
        openaiApiKey.value = localStorage.getItem("openai_api_key") || "";
    }

    // Save session data
    function saveSessionData() {
        localStorage.setItem("jira_email", jiraEmail.value);
        localStorage.setItem("jira_api_token", jiraApiToken.value);
        localStorage.setItem("jira_base_url", jiraBaseUrl.value);
        localStorage.setItem("openai_api_key", openaiApiKey.value);
    }

    function fetchBoards() {
        saveSessionData();
        fetch(`/jira_connect?jira_email=${jiraEmail.value}&jira_api_token=${jiraApiToken.value}&jira_base_url=${jiraBaseUrl.value}`)
            .then(response => response.json())
            .then(data => {
                if (data.status === "success") {
                    boardDropdown.innerHTML = '<option value="">Select Board</option>';
                    data.boards.forEach(board => {
                        boardDropdown.innerHTML += `<option value="${board.id}">${board.name}</option>`;
                    });
                    document.getElementById("board_status").innerText = "✅ All boards fetched";
                    localStorage.setItem("boards", JSON.stringify(data.boards));
                } else {
                    alert("Failed to fetch boards. Check Jira credentials.");
                }
            });
    }

    function fetchSprints() {
        saveSessionData();
        fetch(`/fetch_sprints?jira_email=${jiraEmail.value}&jira_api_token=${jiraApiToken.value}&jira_base_url=${jiraBaseUrl.value}&board_id=${boardDropdown.value}`)
            .then(response => response.json())
            .then(data => {
                if (data.status === "success") {
                    sprintDropdown.innerHTML = '<option value="">Select Sprint</option>';
                    data.sprints.forEach(sprint => {
                        sprintDropdown.innerHTML += `<option value="${sprint.id}">${sprint.name}</option>`;
                    });
                    document.getElementById("sprint_status").innerText = "✅ All sprints fetched";
                    localStorage.setItem("sprints", JSON.stringify(data.sprints));
                } else {
                    alert("Failed to fetch sprints.");
                }
            });
    }

    function fetchIssues() {
        saveSessionData();
        fetch(`/fetch_issues?jira_email=${jiraEmail.value}&jira_api_token=${jiraApiToken.value}&jira_base_url=${jiraBaseUrl.value}&sprint_id=${sprintDropdown.value}`)
            .then(response => response.json())
            .then(data => {
                if (data.status === "success") {
                    document.getElementById("issues_status").innerText = "✅ All issues fetched";
                    generateButton.disabled = false;
                    localStorage.setItem("issues", JSON.stringify(data.issues));
                } else {
                    alert("Failed to fetch issues.");
                }
            });
    }

    function generateSprintGoals() {
        saveSessionData();
        fetch(`/generate_sprint_goals?openai_api_key=${openaiApiKey.value}&issues=${sprintDropdown.value}`)
            .then(response => response.json())
            .then(data => {
                if (data.status === "success") {
                    document.getElementById("sprint_goals_output").innerText = data.sprint_goals;
                } else {
                    alert("Failed to generate sprint goals.");
                }
            });
    }

    document.getElementById("connect_jira").addEventListener("click", fetchBoards);
    boardDropdown.addEventListener("change", fetchSprints);
    sprintDropdown.addEventListener("change", fetchIssues);
    generateButton.addEventListener("click", generateSprintGoals);

    loadSessionData(); // Load session data on page load
});


function fetchBoards() {
    let jiraEmail = document.getElementById("jira_email").value;
    let jiraApiToken = document.getElementById("jira_api_token").value;
    let jiraBaseUrl = document.getElementById("jira_base_url").value;

    fetch(`/jira_connect?jira_email=${jiraEmail}&jira_api_token=${jiraApiToken}&jira_base_url=${jiraBaseUrl}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                let boardDropdown = document.getElementById("board_id");
                boardDropdown.innerHTML = '<option value="">Select Board</option>';
                data.boards.forEach(board => {
                    boardDropdown.innerHTML += `<option value="${board.id}">${board.name}</option>`;
                });
                document.getElementById("board_status").innerText = "✅ All boards fetched";
            } else {
                alert("Failed to fetch boards. Check Jira credentials.");
            }
        });
}

document.getElementById("connect_jira").addEventListener("click", fetchBoards);
