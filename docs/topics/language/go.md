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
Business logic
## `func (self *Trader) name(){}`
This is receiver clause, making this a method attached to the Trader type.
`self` is just a convention which can be changed to anyword used to represents the instance of Trader.
`*Trader` a pointer to a Trade struct or type.
### why use pointer here?
Pointer Receiver,
### Receiver

# Error
- `@Win:~$ /usr/local/go/bin/go
-bash: /usr/local/go/bin/go: cannot execute binary file: Exec format error`
Wrong Architecture;
# goex
