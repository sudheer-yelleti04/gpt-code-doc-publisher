import os
import json
import shutil
import requests
import yaml
from requests.auth import HTTPBasicAuth

# ========= Load Config =========
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

OPENROUTER_KEY = config["openrouter"]["api_key"]
MODEL = config["openrouter"]["model"]
EMAIL = config["confluence"]["email"]
API_TOKEN = config["confluence"]["api_token"]
SITE = config["confluence"]["site"]
SPACE_ID = config["confluence"]["space_id"]

INPUT_FOLDER = config["paths"]["input_folder"]
ARCHIVE_FOLDER = config["paths"]["archive_folder"]
os.makedirs(ARCHIVE_FOLDER, exist_ok=True)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


# ========= Helper Functions =========

def read_python_scripts(folder):
    """Read all .py files from a folder."""
    scripts = []
    for file in os.listdir(folder):
        if file.endswith(".py"):
            path = os.path.join(folder, file)
            with open(path, "r", encoding="utf-8") as f:
                scripts.append((file, f.read(), path))
    return scripts


def generate_doc(script_name, code):
    """Send Python script to GPT (OpenRouter) and get documentation."""
    prompt = f"""
You are a senior Data Engineer writing internal documentation.

Analyze this Python script and describe:
1️⃣ Overall purpose
2️⃣ Key logic and data flow
3️⃣ Functions and libraries used
4️⃣ Inputs / Outputs
5️⃣ A 2-line summary for documentation.

Return the answer in HTML format with attravite fonts style, ready for Confluence.
Avoid balckquotes or markdown formatting.
Example:```html
Note: Don't include any following text like below in Confluence page:
Example:Here's the structured HTML documentation for the provided Python script, complete with styling suited for Confluence. 


Script name: {script_name}
Code:
{code}
"""

    response = requests.post(
        url=OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}]
        })
    )

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    else:
        print(f"❌ GPT Error {response.status_code}: {response.text}")
        return None


def publish_to_confluence(script_name, html_doc):
    """Create a Confluence page with GPT-generated documentation."""
    url = f"https://{SITE}/wiki/api/v2/pages"

    payload = {
        "spaceId": SPACE_ID,
        "title": script_name,
        "body": {
            "representation": "storage",
            "value": html_doc
        }
    }

    response = requests.post(
        url,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(EMAIL, API_TOKEN)
    )

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Uploaded: {data['title']}")
        return True
    else:
        print(f"❌ Confluence Error {response.status_code}: {response.text}")
        return False


def archive_file(file_path):
    """Move successfully processed file to archive."""
    try:
        file_name = os.path.basename(file_path)
        dest = os.path.join(ARCHIVE_FOLDER, file_name)
        shutil.move(file_path, dest)
        print(f"📦 Archived: {file_name}")
    except Exception as e:
        print(f"⚠️ Could not archive {file_path}: {e}")


# ========= Main Flow =========

def main():
    print("🚀 Starting GPT → Confluence Automation\n")

    scripts = read_python_scripts(INPUT_FOLDER)
    if not scripts:
        print("⚠️ No Python scripts found in input folder.")
        return

    for name, code, path in scripts:
        print(f"🧠 Processing: {name}")

        # Step 1: Generate documentation
        doc = generate_doc(name, code)
        if not doc:
            print(f"❌ Skipped {name} due to GPT error\n")
            continue

        # Step 2: Upload to Confluence
        success = publish_to_confluence(name, doc)

        # Step 3: Archive the script
        if success:
            archive_file(path)

        print("-" * 60)

    print("\n✅ All scripts processed successfully!")


if __name__ == "__main__":
    main()
