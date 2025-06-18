from dotenv import load_dotenv
import os

print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir('.'))

load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')

if api_key:
    print(f"✅ API Key found: {api_key[:10]}...")
else:
    print("❌ API Key not found")
    
# Check if .env file exists
if os.path.exists('.env'):
    print("✅ .env file exists")
    with open('.env', 'r') as f:
        content = f.read()
        print("File content:", repr(content))
else:
    print("❌ .env file not found")