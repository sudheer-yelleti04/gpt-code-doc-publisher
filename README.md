# 🧠 Automated Python Code Documentation → Confluence Integration

### 🚀 End-to-End AI-Powered Code Documentation System

This project automates the process of generating **detailed technical documentation** for Python scripts using **GPT (via OpenRouter API)** and publishes it automatically to **Confluence**.

After successful publishing, each processed script is **archived automatically**, ensuring a clean and maintainable workflow — all with **zero manual effort**.


## 📘 **Overview**

This project solves the time-consuming challenge of writing and managing documentation for Python scripts in enterprise environments.

With a single run:

1. All Python scripts from your designated folder are analyzed using GPT.
2. Each script’s explanation is automatically formatted as **rich HTML documentation**.
3. The content is directly published to **Confluence**.
4. The script is moved to the **archive folder** after successful upload.

✅ No manual writing
✅ No platform dependencies like Dataiku or Airflow
✅ Uses OpenRouter (GPT) + Confluence APIs directly


## 🏗️ **Architecture**

```
Python Scripts Folder (Input)
        ↓
   OpenRouter GPT API
        ↓
  AI-Generated HTML Documentation
        ↓
     Confluence Page Creation
        ↓
   Archive Folder (Processed Scripts)
```


## ⚙️ **Features**

| Feature                         | Description                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- |
| 🤖 **AI-Powered Documentation** | Uses GPT (via OpenRouter API) to analyze Python code and generate human-readable documentation. |
| 🌐 **Confluence Integration**   | Publishes generated docs automatically as Confluence pages using REST API.                      |
| 🗂️ **Auto-Archiving**          | Moves processed `.py` files to an archive folder after successful documentation.                |
| 🔐 **Secure Configuration**     | Sensitive data (API keys, credentials, paths) managed via `config.yaml`.                        |
| ⚡ **Lightweight & Portable**    | Pure Python implementation – no Dataiku or heavy tools required.                                |


## 📁 **Project Structure**

```
Project_3_GPT/
│
├── main.py                # Main automation script
├── config.yaml            # Configuration file for API keys & paths
│
├── scripts/               # Folder containing Python scripts to document
│   ├── etl_load.py
│   ├── transform_sales.py
│   └── cdc_script.py
│
└── archive/               # Successfully processed scripts are moved here
```


## 🧩 **Configuration (`config.yaml`)**

```yaml
openrouter:
  api_key: "sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  model: "openai/gpt-4o-mini"

confluence:
  email: "your_email@example.com"
  api_token: "your_confluence_api_token"
  site: "your-domain.atlassian.net"
  space_id: 123456

paths:
  input_folder: "C:\\Path\\To\\scripts"
  archive_folder: "C:\\Path\\To\\archive"
```

> 🛡️ **Security Tip:**
> Never commit your real API keys or tokens to GitHub.
> Add `config.yaml` to your `.gitignore` file.


## 🛠️ **Installation & Setup**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/automated-code-docs.git
   cd automated-code-docs
   ```

2. **Install Dependencies**

   ```bash
   pip install requests pyyaml
   ```

3. **Set Up Configuration**

   * Update `config.yaml` with your actual:

     * OpenRouter API key
     * Confluence credentials
     * Folder paths

4. **Prepare Input Scripts**

   * Place your `.py` files in the `scripts/` directory.

5. **Run the Automation**

   ```bash
   python main.py
   ```


## 📊 **Sample Workflow**

| Step | Action                             | Result                           |
| ---- | ---------------------------------- | -------------------------------- |
| 1️⃣  | Place Python scripts in `scripts/` | Ready for documentation          |
| 2️⃣  | Run `main.py`                      | GPT analyzes code & creates HTML |
| 3️⃣  | Confluence API triggered           | Page created automatically       |
| 4️⃣  | Script archived                    | File moved to `archive/`         |


## 🧱 **Example Script**

Sample script (`etl_load.py`) for testing:

```python
import pandas as pd
import sqlite3
from datetime import datetime

def load_customer_data():
    df = pd.read_csv("data/customers.csv")
    df["load_timestamp"] = datetime.now()
    conn = sqlite3.connect("datawarehouse.db")
    df.to_sql("customers", conn, if_exists="append", index=False)
    conn.close()
```


## 📄 **Example Confluence Output**

**Page Title:** `etl_load.py`
**Content Preview:**

> <h2>Script Purpose</h2>  
> <p>This Python script automates the ETL process for loading customer data into a SQLite database.</p>  
> <h3>Steps</h3>  
> <ul>  
>   <li>Extracts data from CSV</li>  
>   <li>Transforms and adds timestamps</li>  
>   <li>Loads data into target database</li>  
> </ul>  
> <p><i>Generated automatically using GPT 🤖</i></p>


## 🔁 **Automation Behavior**

| Condition           | Action                       |
| ------------------- | ---------------------------- |
| ✅ Upload Successful | File moved to archive        |
| ❌ Upload Failed     | File remains in input folder |
| 🚫 No Scripts Found | Script exits gracefully      |


## 🧠 **Tech Stack**

| Component                 | Technology             |
| ------------------------- | ---------------------- |
| **Language**              | Python 3.10+           |
| **AI Model**              | GPT via OpenRouter API |
| **Documentation Storage** | Atlassian Confluence   |
| **Config Format**         | YAML                   |
| **Auth**                  | HTTP Basic Auth        |


## 🧩 **Future Enhancements**

* Add logging & retry mechanism
* Integrate Slack/email notifications after successful uploads
* Add multi-space Confluence support
* Support for `.ipynb` (Jupyter) documentation generation


## 🧑‍💻 **Author**

**Yelleti Sudheer Kumar**
💼 Data Engineer | AI Enthusiast | Automation Developer
📧 sudheeryelleti@gmail.com
