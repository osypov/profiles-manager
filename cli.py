from .profiles_manager import Manager
from time import sleep

class Client:
    def __init__(self, pm: Manager, script, args,):
        self.pm = pm
        self.script = script
        self.args = args
        self.d_args = vars(args)
        
    def check(self, arg):
        if not self.d_args.get(arg):
            raise BaseException("no %s" % arg)
        

    def profile(self):
        self.check("p")


        d = self.pm.run_profile(self.args.p)

        sleep(10000)
    def clear(self):
        
        while 1:
            r = input("Are you sure? [type yes or no] $ ")

            r = r.strip()

            if r == "y" or r == "yes":
                break
            elif r == "n" or r == "no":
                exit()


        self.pm.clear_all()

    def cli(self):
        match self.script:
            case "profile":
                self.profile()
            
            case "clear":
                self.clear()



