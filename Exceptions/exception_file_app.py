import glob
import os
import re

def iterate_fds(pid):
    dir = '/proc/'+str(pid)+'/fd'
    if not os.access(dir,os.R_OK|os.X_OK): return

    for fds in os.listdir(dir):
        for fd in fds:
            full_name = os.path.join(dir, fd)
            try:
                file = os.readlink(full_name)
                if file == '/dev/null' or \
                  re.match(r'pipe:\[\d+\]',file) or \
                  re.match(r'socket:\[\d+\]',file):
                    file = None
            except OSError as err:
                if err.errno == 2:     
                    file = None
                else:
                    raise(err)

            yield (fd,file)



def isFileinUsed(ifile):
    widlcard = "/proc/*/fd/*"
    lfds = glob.glob(widlcard)
    for fds in lfds:
        try:
            file = os.readlink(fds)
            if file == ifile:
                return True            
        except OSError as err:
            if err.errno == 2:     
                file = None
            else:
                raise(err)
    return False     