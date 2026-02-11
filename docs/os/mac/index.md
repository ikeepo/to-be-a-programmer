# Mac
## How to cast screen 
Download the app **mirrcast** on your android devices.
## How to Write to NTFS system
Pro NTFS Drive-NTFS Write Tool, follow its instruction get work done.
## 如何远程登录Linux服务器(GUI)
- noMachine
如下记录问题，登录后出现键盘不对应，并且鼠标光标消失。不好用
1. 在linux安装noMachine
```shell
#!/bin/bash
# 一键安装 Ubuntu 图形桌面 + NoMachine（适用于腾讯云）

# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装 Ubuntu 桌面环境（非最重的 GNOME，使用轻量 XFCE）
sudo apt install -y xfce4 xfce4-goodies

# 下载并安装 NoMachine
# 需要重新定向
curl -L -o nomachine.deb https://www.nomachine.com/free/linux/64/deb
sudo dpkg -i nomachine_8.11.3_1_amd64.deb

# 查看 NoMachine 状态
sudo /usr/NX/bin/nxserver --status

# 提示完成
echo "✅ 桌面和 NoMachine 安装完成，请确保安全组已开放 TCP 4000 端口"
echo "👉 现在你可以在 Mac 上用 NoMachine 客户端连接这台机器了"

```
2. 服务器开放4000端口

3. [ 本地安装客户端 ](https://www.nomachine.com/) 

#### 问题
- 重启后登录vnc方式lighthouse/ubuntu账号不成功

ssh登录可以，但是vnc不行，两边不是同一个密码，shell中运行`vncserver`后输入的密码或者不输入密码，会重新启用一个界面，在nomachine中可以看到。

- noMachine 键盘不对应
tab-6

q-7

w-8

e-9

r--

t-=

y-[

u-]

i-;

o-'

p-\

a-a

s-b

d-c

f-d

g-e

h-f

j-g

k-h

l-i

;-j

'-k

enter-/

shift-m

z-o

x-p

c-q

v-r

b-s

n-t

m-u

,-v

.-w

/-x

right-shift-y

{opt}-backspace

space - enter

UP-tab

##### [ RealVNC ](https://www.realvnc.com/en/?lai_vid=vgWXVPzn9sGe&lai_sr=10-14&lai_sl=l)
同样适用vncserver在服务器启动，然后ip:1连接；

