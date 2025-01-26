# pip install -r requirements.txt
# pip install uvicorn
uvicorn main:app --reload --env-file .env --proxy-headers --forwarded-allow-ips '*'