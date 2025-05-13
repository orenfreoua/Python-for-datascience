def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
    elif isinstance(obj, float) and str(obj) == 'nan':
        print(f"Cheese: {obj} {type(obj)}")
    elif obj == 0 and isinstance(obj, int):
        print(f"Zero: {obj} {type(obj)}")
    elif obj == '' and isinstance(obj, str):
        print(f"Empty: {type(obj)}")
    elif obj is False:
        print(f"Fake: {obj} {type(obj)}")
    else:
        print("Type not Found")
        return 1
    return 0