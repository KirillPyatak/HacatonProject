# Install dependencies
```
cd server
```
```
python3 -m venv venv
```
pip install -r requirements.txt
```
# Make migrations
```
make migrate-create
```
```
make migrate-up
```
# Run app
```
uvicorn run:app --reload 
```

# Run Admin
```
waitress-serve --listen=127.0.0.1:5000 admin:app
```