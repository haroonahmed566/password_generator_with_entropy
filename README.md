# 🔐 Password Generator With Entropy (CLI)

A Python-based command-line tool that generates **secure, random passwords** using the `secrets` module — perfect for creating passwords that are safe from brute-force and dictionary attacks.

### 🚀 Features

- Cryptographically secure password generation using `secrets`
- Optional inclusion/exclusion of:
  - Digits (`0-9`)
  - Special characters (`!@#$%...`)
- Password entropy calculation (optional)
- Copies the password directly to your clipboard
- CLI flags for quick integration into automation workflows

---

### 📦 Requirements

- Python 3.6+
- `pyperclip` (install with `pip install pyperclip`)

---

### 🛠️ Installation

```bash
git clone https://github.com/haroonahmed566/password_generator_with_entropy/
cd password_generator_with_entropy
pip install -r requirements.txt  # optional, just includes pyperclip
or 
pip install pyperclip
```
## Usage

python password_generator.py [options] \n
🔧 CLI Options\n
Flag	Description	Default\n
-l, --length	Length of the password	14 \n
-nd, --no-digits	Exclude digits from the password	False \n
-ns, --no-special	Exclude special characters	False \n
-e, --entropy	Show entropy score of the generated password	False \n

## Examples
Generate a secure 20-character password with digits and symbols:


python password_generator.py -l 20
Generate a 12-character password without digits or special characters:


python password_generator.py -l 12 --no-digits --no-special

Show entropy of the generated password:
python password_generator.py -e

## Why secrets?
Unlike Python’s random module, secrets uses cryptographically secure pseudorandom number generation (CSPRNG), making it suitable for password and token generation. Read more → https://docs.python.org/3/library/secrets.html

### Output Example

Generated Password: x7G*Lq!@9zZ0#VmR
Password copied to clipboard
Generated Password's entropy score: 95.16
