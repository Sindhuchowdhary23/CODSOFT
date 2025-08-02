<p align="center">
  <img src="https://raw.githubusercontent.com/Sindhuchowdhary23/todo-cli-app/main/docs/logo.png" alt="To-Do CLI Logo" width="200"/>
</p>

<h1 align="center">📝 To-Do List Application</h1>

<p align="center">
  <strong>A versatile task management solution with both Command-Line and Web interfaces - Choose your preferred way to manage tasks!</strong>
  <br />
  <br />
  <a href="#-getting-started"><strong>🚀 Get Started</strong></a>
  ·
  <a href="https://github.com/Sindhuchowdhary23/todo-cli-app/issues"><strong>🐛 Report a Bug</strong></a>
  ·
  <a href="https://github.com/Sindhuchowdhary23/todo-cli-app/issues"><strong>✨ Request a Feature</strong></a>
</p>

<p align="center">
  <a href="https://github.com/Sindhuchowdhary23/todo-cli-app/stargazers"><img src="https://img.shields.io/github/stars/Sindhuchowdhary23/todo-cli-app?style=for-the-badge&logo=github&color=FFDD00" alt="Stars"></a>
  <a href="https://github.com/Sindhuchowdhary23/todo-cli-app/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Sindhuchowdhary23/todo-cli-app?style=for-the-badge&color=00BFFF" alt="License"></a>
  <a href="https://github.com/Sindhuchowdhary23/todo-cli-app/network/members"><img src="https://img.shields.io/github/forks/Sindhuchowdhary23/todo-cli-app?style=for-the-badge&logo=github&color=90EE90" alt="Forks"></a>
</p>

---

## 📌 Table of Contents

- [🌟 About the Project](#-about-the-project)
- [🔥 Core Features](#-core-features)
- [🎬 Interface Previews](#-interface-previews)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [💡 Usage Guide](#-usage-guide)
- [🤝 Contributing](#-contributing)
- [🌟 Contributors](#-contributors)
- [📜 Code of Conduct](#-code-of-conduct)
- [📜 License](#-license)
- [🙌 Credits](#-credits)

---

## 🌟 About the Project

This project provides **two different interfaces** for managing your to-do tasks - giving you the flexibility to choose based on your preference and workflow:

- **📟 Command-Line Interface (CLI):** Perfect for terminal enthusiasts and developers who prefer keyboard-driven interfaces
- **🌐 Web Interface:** Modern, clean Streamlit-based web application for users who prefer graphical interfaces

Both versions offer the same core functionality with their own unique advantages, making task management accessible to everyone regardless of their preferred working environment.

### 🔥 Core Features

*   **✅ Complete Task Management:** Add, view, mark complete, and delete tasks
*   **🎯 Status Tracking:** Clear visual distinction between pending and completed tasks  
*   **🚀 Dual Interface Options:** Choose between CLI or Web interface
*   **💻 Zero External Dependencies:** CLI version uses only Python standard library
*   **🎨 Clean User Experience:** Intuitive interfaces in both versions
*   **⚡ Lightweight & Fast:** Minimal resource usage for maximum efficiency

---

## 🎬 Interface Previews

### Command-Line Interface (task1.py)
```bash
--- To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
Choose an option (1-5): 2

1. Complete GSSoC Registration - Not Done
2. Review Pull Requests - Done
3. Buy groceries - Not Done
```

### Web Interface (todoUI.py)
- Modern Streamlit interface with interactive buttons
- Real-time task status updates
- Clean card-based task display
- One-click task completion and deletion

---

## 🛠️ Tech Stack

| Component           | CLI Version              | Web Version                |
| ------------------- | ------------------------ | -------------------------- |
| **Core Language**   | Python 3.x               | Python 3.x                 |
| **Interface**       | Terminal/Command Line     | Streamlit Web Framework    |
| **Dependencies**    | None (Standard Library)   | Streamlit                  |
| **Storage**         | In-memory (session-based) | Streamlit session state    |

<details>
  <summary><strong>Project Structure</strong></summary>

  ```
  todo-cli-app/
  ├── task1.py              # CLI version - Terminal interface
  ├── todoUI.py             # Web version - Streamlit interface  
  ├── README.md             # Project documentation
  ├── LICENSE               # MIT License
  └── CODE_OF_CONDUCT.md    # Community guidelines
  ```
</details>

---

## 🚀 Getting Started

### Prerequisites

**For CLI Version:**
- Python 3.x installed on your system

**For Web Version:**
- Python 3.x installed on your system
- Streamlit library

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sindhuchowdhary23/todo-cli-app.git
   cd todo-cli-app
   ```

2. **Choose Your Interface:**

   **Option A: Command-Line Interface**
   ```bash
   python task1.py
   ```

   **Option B: Web Interface**
   ```bash
   # Install Streamlit (one-time setup)
   pip install streamlit
   
   # Run the web app
   streamlit run todoUI.py
   ```

3. **🎉 Start Managing Your Tasks!**
   - CLI: Follow the numbered menu options
   - Web: Access via your browser (typically http://localhost:8501)

---

## 💡 Usage Guide

### CLI Version Features
- **Menu-driven interface:** Simple numbered options for all operations
- **Keyboard-only operation:** Perfect for terminal workflows
- **Immediate feedback:** Instant confirmation of all actions
- **Session-based:** Tasks persist during the program session

### Web Version Features  
- **Interactive buttons:** Click-based task management
- **Real-time updates:** Immediate visual feedback
- **Session persistence:** Tasks saved during browser session
- **Modern UI:** Clean, card-based task display

### Common Operations
1. **Adding Tasks:** Enter descriptive task names
2. **Viewing Tasks:** See all tasks with their current status
3. **Completing Tasks:** Mark tasks as done when finished
4. **Deleting Tasks:** Remove tasks you no longer need

---

## 🤝 Contributing

We welcome contributions from developers of all skill levels! Whether you prefer working with CLI applications or web interfaces, there's something for everyone.

### 🌟 How to Contribute

1. **🍴 Fork the Repository**
2. **🌿 Create a Feature Branch:** `git checkout -b feature/amazing-feature`
3. **✨ Make Your Changes**
4. **✅ Test Both Interfaces**
5. **📝 Commit Your Changes:** `git commit -m 'Add amazing feature'`
6. **🚀 Push to Branch:** `git push origin feature/amazing-feature`
7. **🎯 Open a Pull Request**

### 📋 Contribution Ideas

- **🎨 Enhanced CLI:** Add colors and better formatting to terminal interface
- **💾 Persistent Storage:** Implement file-based task storage for both versions
- **🔍 Search Functionality:** Add task search and filtering
- **📅 Due Dates:** Implement deadline tracking
- **🏷️ Categories:** Add task categorization
- **📱 Mobile Optimization:** Improve Streamlit mobile experience
- **🔄 Data Import/Export:** Support for various file formats

### 🧾 Development Guidelines

- Follow **PEP 8** Python style guidelines
- Test changes in **both CLI and web versions**
- Write **clear commit messages**
- Add **comments** for complex logic
- Update **documentation** as needed
- Be **respectful and collaborative**

---

## 🌟 Contributors

Thanks to these amazing people who have contributed to this project:

<a href="https://github.com/Sindhuchowdhary23/todo-cli-app/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Sindhuchowdhary23/todo-cli-app" />
</a>

---

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand our community standards.

In short: **Be respectful, be kind, and be collaborative.**

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Credits

**Developed by [Sindhu Chowdhary](https://github.com/Sindhuchowdhary23)**

> Thank you to all open-source contributors for making this project better! 🚀  
> We welcome developers of all skill levels to contribute and learn together.

---

<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">
  
  <p><strong>⭐ If you found this helpful, please consider giving it a star on GitHub!</strong></p>
  <p>Every star motivates us to keep building and improving. 😊</p>
  
  <img src="https://komarev.com/ghpvc/?username=Sindhuchowdhary23-todo-cli-app&label=Project%20Views&color=00BFFF&style=flat" alt="Project views" />
</div>