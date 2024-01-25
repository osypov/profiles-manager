import os
from pathlib import Path
import shutil
import info
from driver.main import d
# from .cli import Client

class Manager:
    def __init__(self, proxy=None):
        self.sorted_profiles = []
        self.profiles_dir = Path("profiles").absolute()
        self.profile_list = self.profiles_dir.joinpath("profile_list.txt")


        self.current_list = self.get_profiles_list()

        self.proxy = proxy

    def get_profile_path_by_name(self, name):
        return self.profiles_dir.joinpath(name).absolute()

    def get_profiles_list(self):
        profile_list_exists = os.path.exists(self.profile_list)

        if not profile_list_exists: return []

        with open(self.profile_list) as f:
            o = f.read().split(",")

        return o
    
    def run_profile(self, profile, proxy=True, headless=False):
        path = self.get_profile_path_by_name(profile)
        self.path = path
        self.write_profile_if_not_exists(profile)
        # if proxy:
        #     proxy = info.Proxies[0]
        #     self.proxy = proxy

        proxy = self.proxy

        
        print(path)


        driver = d(path, headless=headless, proxy=proxy)
        return driver
    

    def get_profile_path(self):
        return self.path
    
    def write_profile(self, profile: str):
        if "," in profile:
            raise Exception("Profile could not contain \",\" symbol ")
        self.current_list.append(profile)
        with open(self.profile_list, "w") as f:
            f.write(",".join(self.current_list))

    def write_profile_if_not_exists(self, profile):
        path = self.get_profile_path_by_name(profile)

        if not os.path.exists(path): self.write_profile(profile)



    def delete_profile(self, profile: str):
        path = self.get_profile_path_by_name(profile)

        profile_exists = os.path.exists(path)

        if not profile_exists: return False

        shutil.rmtree(path)

    def clear_all(self, ):
        shutil.rmtree(self.profiles_dir)
        os.mkdir(self.profiles_dir)


    

