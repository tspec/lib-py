
def execute_steps(spec_list: list) -> None:
    module_name = "steps"
    class_name = "Steps"
    module = __import__(module_name)
    for func_name in spec_list:
        if hasattr(module, class_name):
            cls = getattr(module, class_name, None) #Find the class you need from the import module
            if cls:
                instance = cls() #Instances of generated classes
                if hasattr(instance, func_name):
                    func = getattr(instance, func_name) #Find the class method you need from the import module
                    func() #Method in Execution Class
                else:
                    print("No way was found.")
            else:
                print("No class was found")
        else:
            print("No module found")       

def dummy():
    return True
