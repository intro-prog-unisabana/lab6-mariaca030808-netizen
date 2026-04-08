# Write your code here!
def employee_print(employee_info):
    print("Name:", employee_info.get("Name", "N/A"))
    print("Salary:", employee_info.get("Salary", "N/A"))
    print("Role:", employee_info.get("Role", "N/A"))

    employee_info.pop("Name", None)
    employee_info.pop("Salary", None)
    employee_info.pop("Role", None)
    if len(employee_info) == 0:
        print("No other info!")
    else:
        for key, value in employee_info.items():
          print(key + ":", value)
