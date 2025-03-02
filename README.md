# 🚀  AI-Powered JIRA Sprint Goal Generator




![Sprint Goal Generator](https://img.shields.io/badge/Sprint%20Goal%20Generator-AI%20Powered-blueviolet?style=for-the-badge&logo=ai)
![Version](https://img.shields.io/badge/version-1.0.0-orange?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.1.6-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Jira API](https://img.shields.io/badge/Jira%20API-Integration-blue?style=for-the-badge&logo=jira)
![OpenAI](https://img.shields.io/badge/OpenAI-ChatGPT%20API-black?style=for-the-badge&logo=openai)

![AI Magic](https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif)

> 🚀 **Say goodbye to boring sprint planning!** 🎯
> Let AI analyze your Jira issues and generate **meaningful, smart sprint goals** so you can focus on **delivering impact instead of wasting time!** ⏳💡
>
Welcome to the **Sprint Goal Generator**, an AI-driven tool that revolutionizes sprint planning by integrating **Jira API** with **OpenAI's language models**! 🎯

---

## 🎯 **What Does This Do?**
- **Step 1:** Connect to your **Jira Account** using an API Token 🔑.
- **Step 2:** Fetch **all the boards** you have access to 📋.
- **Step 3:** Select a **board and sprint**, and fetch all its issues 🏗️.
- **Step 4:** AI processes the issues and **generates clear, actionable sprint goals** using OpenAI! 🤖✨
- **Step 5:** Display sprint goals in a clean, **dashboard-style format** 📊.

---

## 🧐 **Why This Approach? (And What Else I Could've Done!)**
There are **many** ways to build this sprint goal generator, but i chose the **best balance of automation, flexibility, and power**.

### ✅ **Method Chosen: Python Django + Jira API + OpenAI API**
- Pros: **Quick, scalable, customizable, and works with minimal setup**.
- Cons: **Requires API tokens, might have Jira permission issues**.

### 🔄 **Other Ways I Could’ve Done This!**
| Method | Pros | Cons |
|--------|------|------|
| **OAuth 2.0 (Jira Cloud)** | More secure, no API token leaks 🔐 | Complex setup, requires admin permissions ⚙️ |
| **Jira Automation Rules** | Built-in, no coding required 🤖 | Limited customization, no AI intelligence 🧠 |
| **Custom Jira Scripts (Groovy, Script-runner)** | Runs inside Jira, full control | Only works in Jira Server, steep learning curve 📜 |
| **Manual Sprint Planning** | No setup required 🤷 | Slow, repetitive, boring 😩 |

👉 **Why did I choose the API Token method?**
- **Fastest way to get started** 🚀.
- **No need for admin permissions** (if API access is enabled).
- **Works for both Jira Cloud & Jira Server**.

---

## 🔧 **Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/sachinarora/sprint-goal-generator.git
cd sprint-goal-generator
```

### **2️⃣ Create a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Setup Environment Variables (`.env` file)**
Create a `.env` file inside the project folder with the following details:
```ini
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
JIRA_BASE_URL=https://your-jira-instance.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-jira-api-token
OPENAI_API_KEY=your-openai-api-key
```

### **5️⃣ Run Migrations & Start the Server**
```sh
python manage.py migrate
python manage.py runserver
```

🚀 Open `http://127.0.0.1:8000/` in your browser and start generating **AI-powered sprint goals**! 🎉

---

## ⚡ **How the App Works (Step-by-Step)**

1. **Configuration on Left-Side Panel:**
   - Enter Jira Base URL, Email, and API Token.
   - Click **"Connect to Jira"** to fetch available boards.
   - Select a board, fetch sprints, and choose a sprint.
   - Enter OpenAI API Key and click **"Show Me The Magic"**.

2. **Sprint Goal Generation (Right-Side Panel):**
   - Displays **selected Board ID & Sprint Name**.
   - Fetches **Jira Issues** related to the sprint.
   - Uses **AI (OpenAI API)** to **generate meaningful sprint goals**.
   - Displays **AI-Generated Goals** in an easy-to-read format.

---

## 🚀 **Features & Tech Stack**
| Feature | Technology Used |
|---------|----------------|
| **Backend** | Django, Django REST Framework |
| **Frontend** | Bootstrap, Vanilla JavaScript |
| **Database** | SQLite (default) |
| **Jira Integration** | Jira REST API |
| **AI Processing** | OpenAI API |

---

## 🔥 **Possible Issues & Fixes**

### **1️⃣ Getting "403 Forbidden" Error?**
🔹 **Possible Causes:**
- **Your Jira admin disabled API token authentication.**
- **Your API token lacks permissions to access Jira boards.**

✅ **Fix:**
- Try logging into Jira manually using the API token.
- Contact Jira admin to **enable API authentication**.

### **2️⃣ Django API Not Responding?**
🔹 **Possible Causes:**
- Server not running or CORS issues.

✅ **Fix:**
```sh
python manage.py runserver
```

---

## 🤝 **Contributing**
Want to improve this app? Feel free to fork and submit a PR!

1. **Fork the repo**
2. **Create a new branch** (`feature-awesome-thing`)
3. **Commit changes** and push (`git push origin feature-awesome-thing`)
4. **Create a Pull Request** 🚀

---

## 📜 **License**
Ah, licenses. Who even reads them? 🤷‍♂️

This project is **MIT Licensed**—but let’s be honest, **licenses in open source are just fancy decorations**. If you think you can **modify it, improve it, and make the universe a better place**, **DO IT.** 🚀✨

Worried about the license? **Don’t be.** Just look at Threads—it’s Twitter’s long-lost sibling, BlueSky is Twitter’s reflection in the multiverse, and, let’s face it, everything is just a remix! **So fork it, tweak it, and unleash your genius.** 🔥😎
---

## 🚀 **Final Words**
If sprint planning ever felt like **a chore**, let AI handle it for you! 😉
Instead of manually writing sprint goals, let **OpenAI + Jira** do the heavy lifting!

## 🚀 **DIR-Structure**

```
├── sprint_goal_generator/
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── ci-cd.yml
│   ├── db.sqlite3
│   ├── README.md
│   ├── .env
│   ├── docker-compose.yml
│   ├── manage.py
│   └── config/
│   ├── sprint_goal_generator/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── script.js
│   ├── sprint_app/
│   │   ├── ai_processing.py
│   │   ├── jira_api.py
│   │   ├── models.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── utils.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │   ├── templates/
│   │   │   ├── index.html
│   │   │   └── sprint_result.html

```

## 📩 Contact

| Name              | Details                             |
|-------------------|-------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                      |
| **📧 Email**       | [sachnaror@gmail.com](mailto:sachnaror@gmail.com) |
| **📍 Location**    | Noida, India                       |
| **📂 GitHub**      | [github.com/sachnaror](https://github.com/sachnaror) |
| **🌐 Website**     | [https://about.me/sachin-arora](https://about.me/sachin-arora) |
| **📱 Phone**       | [+91 9560330483](tel:+919560330483) |



Happy coding! 🎯🔥





![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/homesachin/Desktop/Screenshot%202025-03-03%20at%203.38.31%E2%80%AFAM.png?version%3D1740957576324)
