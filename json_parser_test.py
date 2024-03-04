import subprocess

def test_valid_json_files():
    valid_files = [
        "test_files/step1/valid.json",
        "test_files/step2/valid.json",
        "test_files/step2/valid2.json",
        "test_files/step3/valid.json"
    ]
    for file_path in valid_files:
        result = subprocess.run(["python", "json_parser.py", file_path], capture_output=True, text=True)
        assert "final result" in result.stdout

def test_invalid_json_files():
    invalid_files = [
        "test_files/step1/invalid.json",
        "test_files/step2/invalid.json",
        "test_files/step2/invalid2.json",
        "test_files/step3/invalid.json",
        # Add more invalid files if needed
    ]
    for file_path in invalid_files:
        result = subprocess.run(["python", "json_parser.py", file_path], capture_output=True, text=True)
        assert "JSON parsing failed" in result.stdout
