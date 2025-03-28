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
In go, a receiver is a special parameter in a method declaration that ties the method to a a specific type.
It's what makes a function a "method" rather than a standalone function.

- Pointer Receiver
the caller's Trader isn't copied, only a pointer is passed.
Modifications are reflected in the caller’s Trader.

- Value Receiver
The method works with a duplicate of the originial Trader, so modifications to self inside the method don't affect the caller's instance.
## reflected
In programming, when we say modifications are "reflected" in the caller's object, it means that any changes made to the object inside a function or method persist ouside that function.
The caller sees those changes.
This happens because the method is working directly with the originial object via a reference or pointer rather than a copy.
## Reference vs Pointer
A pointer is an explicit variable that holds the memory address of another variable. It's a low-level concept borrewed from language like C.
A reference is a higher-level abstraction in many language. It's an alias or handle to an existing variable, often managed by the language to hide raw memory addresses from the programmer.
Go doesn't have "reference" as a distinct language feature.
# Build In
## make vs new
make is specifically designed to create and initialize certain built-in types that can't be fully set up with just a literal or declaration.
`new` creates a zeroed instance of a type and gives you a pointer to it.
`make` creates a fully initialzed, usable instance of slices, maps or channels - types that need more than just zeroing.
`make` returns the instance which require initialization beyond zeroing.
`new` returns a pointer leaving initialization to you.
##### zeroes the memory vs initialize
Zeroes the Memory sets all the bytes of a memory block to zero, it's a basic, minimal setup - nothing more than clearing the slate.
Initialize prepares a data structure for use by setting it up with specific values or internal state beyond just zeroing.
Some types(slices, maps, channels) are unusable as just zero values - they need structure to function.

## chan
chan is a keyword in Go that defines a channel type.
Channels are a core feature of Go's concurrency model, used for communication and synchronization between goroutines.
## goroutine
`go func()`
##### goroutine vs coroutine in Python
goroutine is lightweight threads managed by the Go runtime, not the OS. It's fully concurrent - gotoutines run independently and can execute in parallel on multiple CPU cores.
goroutines are typically communicate with each other by cahnnels, enabling safe data exchange without locks.
Coroutines are single-threaded and cooperative - coroutines run in one thread and yield control explicitly at `await`. No true parallelism unless combined with threads or processes.
## channels
Its purpose is enabling goroutines to share data safely without locks, embodying Go's "don't communicate by shareing memory; share memory by communicating" philosophy.
channel as a Mediator:
- Above Memeory: channels sit "above" raw memory, instead of goroutines accessing a shared variable directly, they interact via the channel. The channel manages the meory and ensures safe access.
- Data Flow: send and receive.  What's more important is that the channel powers the layer concept, pass the data one layer to another.
##### multichanel
`single channel = list + lock + cond_var`
`multiple channels` follow some business logic to make data flow.
对于数据处理场景，当数据需要在多个业务逻辑链条内进行逐层使用时候，因为通过函数调用方式一次只能走一条逻辑链，这就导致逻辑链条的复杂、混乱而难以管理。用channel管理逻辑链条更加清晰明确，特别是多条、多层次的业务逻辑。
换个角度说，业务逻辑（层级+传导）的构建通过channel的逐层传递实现，不应该通过函数返回值的调用、传参实现。
通过channel，数据的传递（业务逻辑的展开）是隐性的，不需要函数有返回值，函数只实现具体的业务逻辑。
函数对数据的需求通过channel获取，也不需要显式传入。
channel类似深埋地底的电缆，传递各种数据，表面干净整齐，只需要有几个地表监视节点；传参类似地面的电线，杂乱。



# Error
- `@Win:~$ /usr/local/go/bin/go
-bash: /usr/local/go/bin/go: cannot execute binary file: Exec format error`
Wrong Architecture;
#
