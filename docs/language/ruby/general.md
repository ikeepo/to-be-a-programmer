# [Ruby ](https://www.ruby-lang.org/en/documentation/installation/)
## Common
```shell

```
## Version Management
- [`rbenv`](https://github.com/rbenv/rbenv#readme)
```shell
sudo apt install rbenv
rbenv init # fresh
# add to .bashrc
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
# fresh
source ~/.bashrc
# install func
rbenv install -l
rbenv install 3.1.2
rbenv global 3.1.2
rbenv local 3.1.2
rbenv versions
```
