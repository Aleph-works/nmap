# Nmap
 A python script for parallelized scanning of open host ports.

## Usage

Specify host to scan (either **domain** or **IP-address**),  **number of threads** for parallel scanning and **port range**.
Here is a [list of TCP and UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers), the well-known ports are often most interesting and span the range of **1** to **1024**.

```
Enter host: 127.0.0.1
Enter threads: 10
Enter start port range: 1
Enter end port range: 1024

Scanning...

Found open port: 80/http
Found open port: 135/epmap
Found open port: 445/microsoft-ds
Found open port: 443/https
Found open port: 843/unknown
Found open port: 902/unknown
Found open port: 912/unknown
...
Done! (7.312 sec)
```

