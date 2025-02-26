# Setting Up a Virtual Environment in Python

A virtual environment allows you to create an isolated Python environment with its own dependencies, ensuring that your project runs smoothly without conflicts.

## Step 1: Install Python (if not already installed)
Ensure you have **Python 3.7 or later** installed. You can check your Python version by running:

```bash
python --version
```

or (on some systems):

```bash
python3 --version
```

If Python is not installed, download and install it from the official website:  
🔗 https://www.python.org/downloads/

---

## Step 2: Create a Virtual Environment
Navigate to your project folder and run:

```bash
python -m venv myenv
```

or (if using Python 3):

```bash
python3 -m venv myenv
```

This will create a virtual environment named `myenv`.

---

## Step 3: Activate the Virtual Environment
### On **Windows** (Command Prompt or PowerShell):
```bash
myenv\Scripts\activate
```

### On **macOS/Linux**:
```bash
source myenv/bin/activate
```

After activation, you should see `(myenv)` appear before your terminal prompt.

---

## Step 4: Install Dependencies
Once the virtual environment is activated, install your required dependencies:

```bash
pip install -r requirements.txt
```

or install individual packages as needed:

```bash
pip install requests beautifulsoup4
```

To save installed packages to a `requirements.txt` file for future use:

```bash
pip freeze > requirements.txt
```

---

## Step 5: Deactivate the Virtual Environment
To exit the virtual environment, simply run:

```bash
deactivate
```

---

## Step 6: Delete a Virtual Environment (if needed)
If you need to remove the virtual environment, **make sure it is deactivated first**, then delete the `myenv` folder:

```bash
rm -rf myenv  # macOS/Linux
rmdir /s myenv  # Windows (Command Prompt)
```

---

## Troubleshooting
### 1. **Command not found: python / python3 / venv**
- Ensure Python is installed and added to your system `PATH`.
- Try using `python3` instead of `python`.

### 2. **"venv" is not recognised as an internal or external command (Windows)**
- Ensure you're using Python 3.7+.
- Try running:
  ```bash
  python -m ensurepip --default-pip
  ```

### 3. **Pip not found after activating the environment**
- Upgrade pip with:
  ```bash
  python -m pip install --upgrade pip
  ```

---

