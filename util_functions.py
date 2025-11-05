#error 001 is error in get_valid_type function
#error 002 is error in get_error_type function
#error 003 is error in type_text function
#error 004 is error in clear_term function
#error 005 is error in alternate_random function
#error 006 is error in
#error 007 is error in
#error 008 is error in
#error 009 is error in
#error 010 is error in
#error 011 is error in
#error 012 is error in
#error 013 is error in
#error 014 is error in
#error 015 is error in
#error 016 is error in
#error 017 is error in
#error 018 is error in
#error 019 is error in
#error 020 is error in
#error 021 is error in
#error 022 is error in
#error 023 is error in
#error 024 is error in
#error 025 is error in
#error 026 is error in
#error 027 is error in
#error 028 is error in
#error 029 is error in
#error 030 is error in
#error 031 is error in
#error 032 is your fault whoever is sitting at the computer
def get_valid_type(type_return, prompt, invalid_prompt="Invalid input. Please try again.", valid=None,typing=False,end="",type_speed=False,random_bounds=(0,.1)):
    """
    get_valid_type is a glorified input statement that auto checks and looks like someone is typing if enabled
    Args:
        type_return (data type): the data type that should be returned (int, float, str, ect)
        prompt (string): what the prompt for the input statement
        invalid_prompt (string): what is printed if the user inputs a invalid input, auto set to "Invalid input. Please try again."
        valid (None, tuple, list): can be a tuple, a list or just None, will check if input is in the tuple or list (tuple for ranges of numbers and lists for specific inputs and none if there is no requirement) defaults to None
        typing (boolean): if the output is "typed" (True is for on False is for off) defaults to False
        end (string): what the end of the input char is, defaults to ""
        random_bounds (tupple): the random bounds for the speed of the "typeing", defaults to (0,.1)
    """
    try:
        if typing==False:
            while True:
                try:                
                    to_return = type_return(input(prompt))
                    if valid is None:
                        return to_return
                    if isinstance(valid, tuple):
                        if valid[0] <= to_return <= valid[1]:
                            return to_return
                        else:
                            type_return(input(f"Invalid Amount\nInput must be between {valid[0]} and {valid[1]}: {end}"))
                    elif isinstance(valid, list):
                        if to_return in valid:
                            return to_return
                        else:
                            type_return(input(f"Invalid Input\nInput must be one of: {valid}: {end}"))
                    else:
                        return to_return
                except ValueError:
                    type_return(input(f"Invalid Input\n{invalid_prompt}"))
        else:
            while True:
                try:             
                    type_text(prompt,"",True,random_bounds)   
                    to_return = type_return(input())
                    if valid is None:
                        return to_return
                    if isinstance(valid, tuple):
                        if valid[0] <= to_return <= valid[1]:
                            return to_return
                        else:
                            type_text(f"Invalid Amount\nInput must be between {valid[0]} and {valid[1]}.","\n",True,random_bounds)  
                            continue
                    elif isinstance(valid, list):
                        if to_return in valid:
                            return to_return
                        else:
                            type_text(f"Invalid Input \nInput must be one of: {valid}.","\n",True,random_bounds)
                            continue
                    else:
                        return to_return
                except ValueError:
                    type_text(f"Invalid Input\n{invalid_prompt}","\n",True,random_bounds)
                    continue
    except:
        print("error 001 occurred, please try again")
def get_error_type(error_number):
    """
    get_error_type returns the error string based on the error number
    Args:
        error_number (int): the error number
    """
    try:
        return [None,"get_valid_type","get_error_type","type_text","clear_term","alternet_random",None,None,None][error_number]
    except:
        print("error 002 occurred, please try again")
def type_text(text,end="\n",typing=True,random_bounds=(0,.1)):
    """
    type_text is basically a glorified print statement that prints out text that looks like someone is typeing
    Args:
        text (string): this is what is printed
        end (string): what the end of the print char is, defaults to "\n"
        typing (boolean): if the output is "typed" (True is for on False is for off) defaults to True
        random_bounds (tuple): the random bounds for the speed of the "typeing", defaults to (0,.1)
    """
    try:
        import random,time
        if typing==False:
            print(text,end=end)
        else:
            for x in text:
                time.sleep(random.uniform(*random_bounds))
                print(x,end="")
            print("",end=end)
        return
    except:
        print("error 003 occurred, please try again")
def clear_term():
    """
    clears the terminal
    """
    try:
        import os
        if os.name == 'nt':
            os.system('cls')
        if os.name == 'posix':
            os.system('clear')
        if os.name != 'nt' and os.name != 'posix':
            print("\n" * 500)    
        return
    except:
        print("error 004 occurred, please try again")
def alternate_random(bounds,type_of_random=int,seed=None):
    """
    alternate_random returns a random number between the bounds, can be int or float
    Args:
        bounds (tupple): the bounds for the random number
        type_of_random (data type): the data type of the random number (int or float) defaults to int
    """
    try:
        import os,time
        nums=[]
        nums.append(os.getpid())
        nums.append(os.getppid())
        nums.append(os.cpu_count())
        nums.append(os.path.getsize(__file__))
        nums.append(int(time.time()*1000))
        if seed is None:
            seed=sum(nums)
        else:
            seed=seed+sum(nums)
        random_number=((((seed**7)%nums[3]/nums[2])*nums[2])+nums[0]+nums[1])% (bounds[1]-bounds[0])+bounds[0]
        if type_of_random==int:
            return int(random_number)
        if type_of_random==float:
            return float(random_number)
    except:
        print("error 005 occurred, please try again")
class threads:
    """
    A class that is more usefull than the normal threading class
    """
    def __init__(self,target,args=()):
        """
        initializes the thread
        Args:
            target (function): the function that the thread will run
            args (tuple): the arguments for the function, defaults to ()
        """
        try:
            import threading
            self.thread=threading.Thread(target=target,args=args)
        except:
            print("error 006 occurred, please try again")
    def start(self):
        """
        starts the thread
        """
        try:
            self.thread.start()
        except:
            print("error 007 occurred, please try again")
    def join(self):
        """
        joins the thread
        """
        try:
            self.thread.join()
        except:
            print("error 008 occurred, please try again")
    def is_alive(self):
        """
        checks if the thread is alive
        Returns:
            boolean: True if the thread is alive, False if not
        """
        try:
            return self.thread.is_alive()
        except:
            print("error 009 occurred, please try again")
    def repeat_function(func, times, delay=0, args=()):
        """
        repeats a function a certain number of times with a delay between each call
        Args:
            func (function): the function to be called
            times (int): the number of times to call the function
            delay (int): the delay between each call in seconds, defaults to 0
            args (tuple): the arguments for the function, defaults to ()
        """
        try:
            import time
            for _ in range(times):
                func(*args)
                time.sleep(delay)
        except:
            print("error 010 occurred, please try again")
    def repeat_function_until_stop(func, delay=0, args=()):
        """
        repeats a function until the thread is stopped with a delay between each call
        Args:
            func (function): the function to be called
            delay (int): the delay between each call in seconds, defaults to 0
            args (tuple): the arguments for the function, defaults to ()
        """
        try:
            import time
            while True:
                func(*args)
                time.sleep(delay)
        except:
            print("error 011 occurred, please try again")
    def get_data(self):
        """
        gets data from the thread via lists
        Returns:
            list: the data from the thread
        """
        try:
            return self.thread.data
        except:
            print("error 012 occurred, please try again")
    def set_data(self, data):
        """
        sets data for the thread via lists
        Args:
            data (list): the data to be set for the thread
        """
        try:
            self.thread.data = data
        except:
            print("error 013 occurred, please try again")
    def input_thread_setup(self):
        """
        sets up a thread for instant inputs, usefull for games
        required modules: threading, queue, sys, select
        """
        try:
            import threading
            import queue
            import sys
            import select

            class InputThread(threading.Thread):
                def __init__(self):
                    super().__init__()
                    self.queue = queue.Queue()
                    self.daemon = True

                def run(self):
                    while True:
                        if select.select([sys.stdin], [], [], 0.1)[0]:
                            user_input = sys.stdin.readline().strip()
                            self.queue.put(user_input)

                def get_input(self):
                    inputs = []
                    while not self.queue.empty():
                        inputs.append(self.queue.get())
                    return inputs

            self.input_thread = InputThread()
            self.input_thread.start()
        except:
            print("error 013 occurred, please try again")
def factorial(n):
    """
    calculates the factorial of a number
    Args:
        n (int): the number to calculate the factorial of
    Returns:
        int: the factorial of the number
    """
    try:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    except:
        print("error 014 occurred, please try again")
def fibonacci(n):
    """
    calculates the nth fibonacci number
    Args:
        n (int): the position of the fibonacci number to calculate
    Returns:
        int: the nth fibonacci number
    """
    try:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except:
        print("error 015 occurred, please try again")
def is_prime(n):
    """
    checks if a number is prime
    Args:
        n (int): the number to check
    Returns:
        boolean: True if the number is prime, False if not prime
    """    try:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    except:
        print("error 016 occurred, please try again")
def get_ip_adress():
    """
    gets the local ip address of the computer
    Returns:
        string: the local ip address
    """
    try:
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        print("error 017 occurred, please try again")
def get_mac_address():
    """
    gets the mac address of the computer
    Returns:
        string: the mac address
    """
    try:
        import uuid
        mac = uuid.getnode()
        mac_address = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        return mac_address
    except:
        print("error 018 occurred, please try again")
def get_system_info():
    """
    gets basic system information
    Returns:
        dict: a dictionary containing system information
    """
    try:
        import platform
        system_info = {
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor()
        }
        return system_info
    except:
        print("error 019 occurred, please try again")
def read_file(file_path):
    """