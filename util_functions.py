#error 001 is error in get_valid_type function
#error 002 is error in get_error_type function
#error 003 is error in
#error 004 is error in
#error 005 is error in
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
def get_valid_type(type_return, prompt, invalid_prompt="Invalid input. Please try again.", valid=None,typeing=False,end="",type_speed=False,random_bounds=(0,.1)):
    """
    get_valid_type is a glorifyed input statement that auto checks and looks like someone is typeing if enabled
    Args:
        type_return (data type): the data type that shuld be returned (int, float, str, ect)
        prompt (string): what the prompt for the input statement
        invalid_prompt (string): what is printed if the user inputs a invalid input, auto set to "Invalid input. Please try again."
        valid (None, tupple, list): can be a tupple, a list or just None, will check if input is in the tupple or list (tupple for ranges of numbers and lists for spisific inputs and none if there is no requierment) defaults to None
        typeing (boolean): if the output is "typed" (True is for on False is for off) defalts to False
        end (string): what the end of the input char is, defalts to ""
        random_bounds (tupple): the random bounds for the speed of the "typeing", defalts to (0,.1)
    """
    try:
        if typeing==False:
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
    try:
        return [None,"get_valid_type","get_error_type",None,None,None,None,None,None][error_number]
    except:
        print("error 002 occurred, please try again")
def type_text(text,end="\n",typeing=True,random_bounds=(0,.1)):
    """
    
    """
    try:
        import random,time
        if typeing==False:
            print(text,end=end)
        else:
            for x in text:
                time.sleep(random.uniform(*random_bounds))
                print(x,end="")
            print("",end=end)
        return
    except:
        print("error 003 occurred, please try again")
    

