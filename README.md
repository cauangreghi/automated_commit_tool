

# 🤖 Git Automated Commit Tool

Automatically generate high‑quality Git commit messages using **Claude API (Anthropic)** based on your **staged Git changes**.

This Python tool inspects staged files, asks Claude to generate a conventional commit message, shows a preview, and lets you confirm the commit with a single key press — no Enter required.

***

## ✨ Features

*   ✅ Reads **only staged changes** (`git status -v`)
*   ✅ Generates **conventional commit messages**
*   ✅ Uses **Claude API** for intelligent summaries
*   ✅ Returns **structured JSON** (no Markdown parsing)
*   ✅ Validates responses with **Pydantic**
*   ✅ Interactive **Y/N prompt** with color support
*   ✅ Cross‑platform (Linux, macOS, Windows)

***

## 🧠 How It Works

1.  You stage your files with `git add`
2.  The tool:
    *   Reads staged changes
    *   Sends them to Claude
    *   Receives a structured commit summary
3.  You review the message and file list
4.  Press:
    *   **Y** → commit is created automatically
    *   **N** → commit is canceled

***

## 📦 Requirements

*   Python **3.9+**
*   Git
*   Anthropic (Claude) API key

### Python dependencies

```bash
pip install anthropic python-dotenv pydantic
```

> Optional (for older Windows terminals):

```bash
pip install colorama
```

***

## 🔐 Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/githubautomated_commit_tool.git
cd githubautomated_commit_tool
```

### 2️⃣ Set your Claude API key

Create a `.env` file in the project root:

```env
CLAUDE_API=your_api_key_here
```

🚨 **Important:**  
Add `.env` to your `.gitignore` — never commit API keys.

***

## 🚀 Usage

1.  Stage your files:

```bash
git add .
```

2.  Run the tool:

```bash
python main.py
```

3.  Review the generated commit:

```text
✅ Commit message:
feat: initialize commit insight tool with Claude API integration

📁 Files:
- .gitignore
- commit_insight.py
- teste.py

🤖 Press Y to commit or N to cancel
```

✅ Press **Y** → commit is created  
❌ Press **N** → nothing happens

***

## 📁 Example Output (Structured)

```json
{
  "message": "feat: initialize commit insight tool with Claude API integration",
  "files": [
    ".gitignore",
    "commit_insight.py",
    "teste.py"
  ]
}
```

***

## 🏗️ Project Structure

```text
.
├── main.py              # Entry point
├── staged_commit.py     # Pydantic schema (CommitSummary)
├── .env                 # Claude API key (ignored by git)
├── README.md
└── .gitignore
```

***

## ✅ Design Principles

*   **No Markdown parsing** — uses Claude tool calling
*   **Schema‑first** — validated JSON via Pydantic
*   **Fail‑fast** — errors stop execution safely
*   **Human‑in‑the‑loop** — you always confirm before committing

***

## 🔮 Possible Improvements

*   ⏳ Auto‑timeout commit confirmation
*   🧪 Dry‑run mode
*   🧩 Git hook integration
*   ✏️ Interactive commit message edit
*   📦 PyPI package

Contributions are welcome!

***

## ⚠️ Security Notice

*   Never commit `.env` files
*   Revoke exposed API keys immediately
*   Use separate keys for local tooling

***

## 📄 License

MIT — feel free to use, modify, and distribute.

***

## 🙌 Acknowledgements

*   <https://www.anthropic.com/>
*   Git Conventional Commits specification

***

If you want, I can also:

*   Add badges (Python version, license, AI)
*   Write a **Git hook installation section**
*   Optimize the README for PyPI
*   Add screenshots / asciinema demo

Just tell me 👍
