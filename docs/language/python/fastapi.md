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

## CROS
端口不同 = 不同 Origin

浏览器阻止了你的请求，因为 后端没有允许跨域访问。

Preflight Request， 浏览器先问后端：我能不能从 3000 访问你？”

CORS 是严格按 Origin 字符串匹配, tunnel 会使得域变为外部网址；

对于外网，应该使前端只访问相对路径，而不产生绝对ip。

最佳方式是让fastapi统一管理前端，前端build后将静态文件挂载到fastapi下由其统一管理。这样就避免跨域问题。
前端文件、数据都可以挂载，但是挂载要放在路由定义之后，最好就放在文件最后面。

也可临时在CORS中添加外网IP, 此时会出现一个问题，就是笔记本可以访问，但是手机、平板又出现跨域问题，这是因为移动端浏览器更严格，origin会变化，可以通过添加`allow_origin_regex=r"https://.*\.xxx\.com",`实现访问，保证复合所有origin变体。

```shell 
# 允许 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://192.168.2.19:3000/" # 没有，分割
        "http://127.0.0.1:3000/" # origin不能有/
        "http://localhost:3000/"
        ],  # 或 ["*"] 允许所有
```
# Refs
[^1] [FastAPI Dependency](https://fastapi.tiangolo.com/tutorial/dependencies/)
