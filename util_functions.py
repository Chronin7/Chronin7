def get_valid_type(type_return, prompt, invalid_prompt="Invalid input. Please try again.", valid=None,title=""):
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