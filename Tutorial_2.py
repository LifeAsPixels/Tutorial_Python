from Tutorial import *
import time


# delete a variable
big_number = 9999
del big_number

def main():
    t0 = time.time()
    
    Instance = Basics.Tutorial()
    Instance.Util.Header(title = "Python Tutorial")
    print(Instance.__doc__)
    
    
    Instance.String_Manipulation()
    
    
    t1 = time.time()
    Instance.Util.Header("Application Stats")
    print(f'Program took {t1-t0:.4f} seconds to execute.')
if __name__ == "__main__":
    main()