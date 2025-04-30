import inspect 

class Console_Utility:
    
    def Header(self, title = ""):

        if title != "":
            print()
            print()
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{title.ljust(60, ' ').rjust(65, ' ').ljust(80, '-').rjust(100, '-')}>")
            print(f'{'<'.ljust(101, '_')}>')
        else:
            print()
            print()
            caller_frame = inspect.stack()[1]
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{caller_frame.function.ljust(60, ' ').rjust(65, ' ').ljust(80, '-').rjust(100, '-')}>")
            print(f'{'<'.ljust(101, '_')}>')
            
 