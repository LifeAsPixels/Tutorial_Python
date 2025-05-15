import inspect 

class Console_Utility:
    
    def Header(self, title = ""):

        if title != "":
            print()
            print()
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{title.ljust(len(title) + 5, ' ').rjust(len(title) + 10, ' ').ljust(60, '-').rjust(100, '-')}>")
            print(f'{'<'.ljust(101, '_')}>')
        else:
            print()
            print()
            caller_frame = inspect.stack()[1]
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{caller_frame.function.ljust(len(caller_frame.function) + 5, ' ').rjust(len(caller_frame.function) + 10, ' ').ljust(60, '-').rjust(100, '-')}>")
            print(f'{'<'.ljust(101, '_')}>')
            
 