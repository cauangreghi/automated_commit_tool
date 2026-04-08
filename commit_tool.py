import anthropic
import os
from dotenv import load_dotenv
from validators.staged_commit import CommitSummary
from utils.read_key import read_single_key
import subprocess


def handler():
    load_dotenv()

    client = anthropic.Anthropic(
        api_key=os.getenv("CLAUDE_API")
    )

    differences_changes = subprocess.run(
        ["git", "status", "-v"],
        capture_output=True,
        text=True
    )
    clear_staged_changes = differences_changes.stdout

    tools = [
        {
            "name": "commit_summary",
            "description": "Generate a conventional commit message and list of modified files",
            "input_schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "One-line conventional commit message"
                    },
                    "files": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of modified files"
                    }
                },
                "required": ["message", "files"]
            }
        }
    ]
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": (
                    "Analyze the following staged git changes and generate a commit summary.\n\n"
                    f"{clear_staged_changes}"
                )
            }
        ],
        tools=tools,
        tool_choice={"type": "tool", "name": "commit_summary"}
    )

    tool_output = response.content[0].input
    summary = CommitSummary(**tool_output)

    print("\n✅ Commit message:")
    print(summary.message)

    print("\n📁 Files:")
    for f in summary.files:
        print(f"- {f}")

    print("\n🤖 Press (Y) to commit or (N) to cancel")

    while True:
        make_commit = read_single_key()
        if make_commit in ("y", "n"):
            print(make_commit.upper())
            break

    if make_commit == "y":
        subprocess.run(["git", "commit", "-m", summary.message])


if __name__ == "__main__":
    handler()