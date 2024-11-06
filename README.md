# NetExec Module: Info

The **Info** module of NetExec is designed to check the `smb.db` file for previously connected sessions. It verifies if the connection was established with System or Administrator rights when accessing the host. 

## Features

- **Connection Verification**: The module checks if both the IP address and hostname exist with Administrator rights.
- **Login Information**: It prints the login information in the format `-id login`. This ID can be used to log in as the displayed user, provided the password is valid.
- **Protocol Support**: The module can check various protocols, including:
  - SMB
  - RDP
  - WMI
  - LDAP
  - WinRM

## Limitations

Currently, the module only saves login information in the `smb.db` file. As a result, the output will primarily consist of SMB-related information.

## Conclusion

The Info module is a useful tool for checking and managing connections with high-level access. It helps penetration testers retest security assessments to determine if the passwords for Administrator accounts have changed.

## Example Usage

```
┌──(root㉿X)-[~]
└─# nxc -t 512 smb 192.168.56.108
SMB         192.168.56.108  445    DC1              [*] Windows Server 2008 R2 Enterprise 7600 x64 (name:DC1) (domain:domain.com) (signing:True) (SMBv1:True)

┌──(root㉿X)-[~]
└─# nxc -t 512 smb 192.168.56.108 -M info <--
SMB         192.168.56.108  445    DC1              [*] Windows Server 2008 R2 Enterprise 7600 x64 (name:DC1) (domain:domain.com) (signing:True) (SMBv1:True)
INFO        192.168.56.108  445    DC1              [+] (Pwnd3!) domain.com\Administrator:password1 -id=393 <--

┌──(root㉿X)-[~]
└─# nxc -t 512 smb 192.168.56.108 -id=393 <--
SMB         192.168.56.108  445    DC1              [*] Windows Server 2008 R2 Enterprise 7600 x64 (name:DC1) (domain:domain.com) (signing:True) (SMBv1:True)
SMB         192.168.56.108  445    DC1              [+] domain.com\Administrator:password1 (Pwn3d!)  
```

![Example Usage](https://github.com/user-attachments/assets/9bbdca0a-353f-4562-9f61-a5d4db376765)
