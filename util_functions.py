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
def get_valid_type(type_return, prompt, invalid_prompt="Invalid input. Please try again.", valid=None,title=""):
    try:
        while True:
            try:
                to_return = type_return(input(prompt))
                if valid is not None:
                    return to_return
                if isinstance(valid, tuple):
                    if valid[0] <= to_return <= valid[1]:
                        return to_return
                    else:
                        type_return(input("Invalid Amount", f"Input must be between {valid[0]} and {valid[1]}."))
                elif isinstance(valid, list):
                    if to_return in valid:
                        return to_return
                    else:
                        type_return(input("Invalid Input", f"Input must be one of: {valid}."))
                else:
                    return to_return
            except ValueError:
                type_return(input("Invalid Input", invalid_prompt))
    except:
        print("error 001 occurred, please try again")
def get_error_type(error_number):
    return [None,"get_valid_type","get_error_type",None,None,None,None,None,None][error_number]