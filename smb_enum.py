from smb.SMBConnection import SMBConnection
import smbclient

class Connect():
    def __init__(self, target_ip, port=445, username="", password="", domain=''):
        self.target_ip = target_ip
        self.port = port
        self.username = username
        self.password = password
        self.domain = domain

    def test_anon(self):
        try:
            conn = SMBConnection(self.username, self.password, "smbclient", self.target_ip, self.domain, use_ntlm_v2=True, is_direct_tcp=True)
            if conn.connect(self.target_ip, self.port):
                print(f"Anonymous connection to {self.target_ip} was successful")
                conn.close()
                return True
            else:
                return False
        except Exception as e:
            print(f'The following error has occured {e}')
            return False
            
    def list_shares(self):
        if self.test_anon():
            list_shares = str(input("Would you like to list available shares and associated permissions y/n: "))
            if list_shares == 'y' or 'Y':
                try: 
                    conn = SMBConnection(self.username, self.password, self.target_ip, 'smbclient', self.domain, use_ntlm_v2=True, is_direct_tcp=True)
                    conn.connect(self.target_ip, self.port)
                    share_list = conn.listShares()
                    shared_list = conn.
                    for share in share_list:
                        print(f"""
                                Share Name: {share.name}
                                Share Comments: {share.comments}

                            """)
                    
                    conn.close()
                except Exception as e:
                    print(f"Following error has occured: {e}")
            elif list_shares == 'n' or 'N':
                print("closing program")
            else:
                print("invalid input")
        else:
            print(f"Anonymous access to {self.target_ip} was unsuccessful")


            
            
            

if __name__== "__main__":
    target_ip = '10.10.11.174'
    test = Connect(target_ip)
    test.test_anon()
    test.list_shares()
