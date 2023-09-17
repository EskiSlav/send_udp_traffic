# Send UDP traffic
This application sends UDP traffic to the specified destination. Script uses data from file `input.txt` and sends each line of the file as an individual packet.

## Requirements
- Python version 3.9.
- Built-in packages are used.

## Installation
All you need to do is basically clone the repository and use your installed python. 
```bash
git clone https://github.com/EskiSlav/send_udp_traffic.git
```

## Usage
```bash
python3 send_udp_traffic.py IP PORT [filename..]
```

## Examples
### Example 1
```
$ python send_udp_traffic.py 127.0.0.1 8080

File is not specified. Using input.txt.
Using filename input.txt
Sent: 05/15/2023, 11:59:35 2021-09-02 23:59:49 imap-login: Info: Login: user=<a.a.koval>, method=DIGEST-MD5, rip=46.113.212.139, lip=195.148.115.117, mpid=3751, TLS, session=<ISmiddxsagnLBasdtwuhdTv>
Sent: 05/15/2023, 11:59:36 2021-09-02 23:59:51 pop3-login: Info: Login: user=<a.a.kozak>, method=DIGEST-MD5, rip=10.100.200.200, lip=10.100.200.1, mpid=3754, TLS, session=<SIDLdsdsgnLuNsKZAoX>
Sent: 05/15/2023, 11:59:37 2021-09-02 23:59:33 imap(a.a.vakarchuk): Info: Logged out in=636 out=1946
Sent: 05/15/2023, 11:59:38 2021-09-06 16:04:24 imap-login: Info: Disconnected (auth failed, 1 attempts in 2 secs): user=<a.a.zelenskiy>, method=DIGEST-MD5, rip=37.173.121.159, lip=195.148.115.117, TLS, session=<YJaqdssdsssdWWf>
^C
Exitting...
```

### Example 2
```
$ python send_udp_traffic.py 127.0.0.1 8080 input_AD.txt

Using filename input_AD.txt
Sent: 05/15/2023, 12:04:45 "Authentication.clientAccount"="squid@domain.COM”
Sent: 05/15/2023, 12:04:46 "Authentication.clientAccount"="possum@domain.COM”
Sent: 05/15/2023, 12:04:47 "Authentication.serverAccount"="squid@domain.COM”
Sent: 05/15/2023, 12:04:48 "Valid.clientAccount"="squid@domain.COM”
Sent: 05/15/2023, 12:04:49 "Authentication.clientAccount"="viacheslav.kozachok@betta.sec.ua”
^C
Exitting...

```
