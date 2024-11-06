import os
import glob
import sqlite3
from nxc.config import nxc_workspace


class NXCModule:

    """
    Module checks smb.db file (on IP + Hostname) when connected with system rights and prints login information as -id login.
    --------------------------------------------------------------------------
    nxc smb 10.10.10.10 -M info
        [+] (Pwnd3!): TEST-PC\\administrator:password -id 12 (Prints Pwnd3! accounts with credential ID to login faster)  

    nxc smb 10.10.10.10 -id 12    
    """

    name = "info"
    description = "Module checks 'smb.db' file (on IP + Hostname) when connected to the system and prints login information from logs"
    supported_protocols = ['smb', 'rdp', 'wmi', 'ldap', 'winrm']
    opsec_safe = True  
    multiple_hosts = True  

    def __init__(self):
        self.context = None
        self.module_options = None
        self.base_path = os.path.expanduser('~/.nxc/workspaces')

    def options(self, context, module_options):
        pass

    def on_login(self, context, connection):
        workspace_path = os.path.join(self.base_path, nxc_workspace, '')
        for name in glob.glob(workspace_path):
            con = sqlite3.connect(f'file:{name}/smb.db?mode=ro', uri=True)
            cur = con.cursor()
            sqlselect = 'select DISTINCT hosts.ip, hosts.hostname, hosts.domain, users.username, users.password, users.id from users CROSS JOIN admin_relations on users.id = admin_relations.userid CROSS JOIN hosts on hosts.id = admin_relations.hostid where hosts.ip = "' + connection.host + '" and hosts.hostname = "' + connection.hostname + '" order by users.id desc'
            cur.execute(sqlselect)
            rows = cur.fetchall()
            for row in rows:
                context.log.success( '\033[1;33;40m' + '(Pwnd3!) ' + '\x1b[0m' + row[2] + '\\' + row[3]+":"+row[4] + ' -id=' + str(row[5]))
            con.close()        
