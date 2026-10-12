import secrets
import string
import argparse
from pathlib import Path

def generate_password(length: int = 12, use_numbers: bool = True, use_symbols: bool = True) -> str:
    if length < 8:
        raise ValueError("Password must be at least 8 characters")

    alphabet = string.ascii_letters
    if use_numbers:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{}<>?/"

    return ''.join(secrets.choice(alphabet) for _ in range(length))

def save_password(path: Path, username: str, password: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{username}: {password}\n")

def main() -> None:
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("-u", "--username", required=True, help="Username for which to generate a password")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (minimum 8)")
    parser.add_argument("--no-numbers", action="store_true", help="Disable numbers")
    parser.add_argument("--no-symbols", action="store_true", help="Disable symbols")
    parser.add_argument("--save", action="store_true", help="Save to local .local_passwords (gitignored)")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_numbers=not args.no_numbers,
        use_symbols=not args.no_symbols,
    )

    print(f"Generating password for {args.username}")
    print(f"Generated Password: {password}")

    if args.save:
        save_path = Path(".local_passwords")
        save_password(save_path, args.username, password)
        print(f"Saved to {save_path} (ensure it's in .gitignore)")

if __name__ == "__main__":
    main()
