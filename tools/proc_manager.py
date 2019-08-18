import subprocess

class Process:
    def __init__(self):
        self.proc_name = None
        self.proc_pid = None
        
    def get_proc_pid_by_name(self, proc_name):
        proc_list = self.proc_list()
        try:
            if len(proc_list[proc_name.encode()]) > 1:
                print("There are several processes with that name: {0}".format(proc_list[proc_name.encode()]))
                pid = input("Which one? - ")
                self.proc_name = proc_name
                self.proc_pid = pid
                return pid
            else:
                pid = proc_list[proc_name.encode()][0].decode()
                self.proc_name = proc_name
                self.proc_pid = pid
                return pid
            
        except KeyError:
            print("There are no processes with that name " + proc_name)
            return 0
    
    def proc_list(self):
        procs = dict()
        for proc in [line.split() for line in subprocess.check_output("tasklist").splitlines()][3:]:
            proc_name = proc[0]
            proc_pid = proc[1]
            if proc_name not in procs:
                procs[proc_name] = [proc_pid]
            else:
                proc_pids = procs[proc_name]
                proc_pids.append(proc_pid)
                procs[proc_name] = proc_pids
        return procs
    
    def show_proc(self):
        if self.proc_pid is not None:
            #win32api