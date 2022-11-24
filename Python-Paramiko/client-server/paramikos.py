import paramiko 
import os

class MysftpClient(paramiko.SSHClient):
    def putdir(self,source,target):

        for item in os.listdir(source):
            if os.path.isfile(os.path.join(source,item)):
                self.put(os.path.join(source,item),'%s/%s' % (target, item))
            else:
                self.mkdir('%s/%s' % (target, item), ignore_existing=True)
                self.putdir(os.path.join(source,item), '%s/%s' % (target, item))    

    def mkdir(self,path,mode=511,ignore_existing=False):

        try:
            super(MysftpClient,self).mkdir(path,mode)
        except IOError:
            if ignore_existing:
                pass
            else:
                raise    


