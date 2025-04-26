# FastAPI
# Concepts
- `path operation function `
A python function defines the logic for handling a specific HTTP request.
```python
@app.get('/ping')
def pong():
  return {"ping":"pong"}
```
# Dependency Injection[^1]
- `settings: Settings = Depends(get_settings) vs settings: Settings = get_settings()`
First is Dependency Injection, run on request, later is run at module load.

# Refs
[^1] [FastAPI Dependency](https://fastapi.tiangolo.com/tutorial/dependencies/)
