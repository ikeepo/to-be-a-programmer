# [Go](https://go.dev/learn/)
[Install multiple Go versions](https://go.dev/doc/manage-install)
You need to download first, [all releases](https://go.dev/dl/).
```
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.24.1.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin  # .profile
source .profile
go version
```
Acquire skills from the [example](https://gobyexample.com/);

## Why `for` has multiple implemented method


# Error
- `@Win:~$ /usr/local/go/bin/go
-bash: /usr/local/go/bin/go: cannot execute binary file: Exec format error`
Wrong Architecture;
