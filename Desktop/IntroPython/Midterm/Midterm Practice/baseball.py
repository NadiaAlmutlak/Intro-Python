# in the case the csv is provided this code can be directly applicable by just changing the csv name
import csv

comparator_ops = ["min", "max"]  # these operators give us the different mathmatical function labels we may use
math_ops = ["sum", "avg"]

valid_op_names = comparator_ops + math_ops  # if another label is inserted and not part of the valid op lists,


# it will result in errors

def evaluate_sheet(column_name, op_name, fn="data.csv"):  # you can change the csv file input here
    result = None

    try:
        with open(fn, "r") as d:  # reads our data file
            cr = csv.reader(d, delimiter=",")

            op_index = valid_op_names.index(op_name)  # provides the valid ops within this function

            c_index = None
            count = 0

            for r in cr:
                # print(r)
                if c_index is None:
                    c_index = r.index(column_name)
                else:
                    count = count + 1
                    v = r[c_index]
                    if op_name in comparator_ops:
                        if result is None:
                            result = v
                        else:
                            if op_name == 'max' and v > result:
                                result = v
                            elif op_name == 'min' and v < result:
                                result = v
                    else:
                        if result is None:
                            result = 0
                        result = result + float(v)

            if op_name == 'avg':
                result = result / count
            d.close()

    except ValueError as v:
        print(type(v), v)
        result = None
    except FileNotFoundError as fe:
        print(type(fe), fe)
        result = None
    except UnicodeError as ue:
        print(type(ue), ue)
        result = None
    except TypeError as te:
        print(type(te), te)
        result = None
    except ValueError as ve:
        result = None
        print(type(ve), ve)

    return result

#Test cases

print("h,max = ", evaluate_sheet('h', 'max'))
print("h,max = ", evaluate_sheet('playerid', 'max'))
print("h,max = ", evaluate_sheet('h', 'sum'))
print("h,max = ", evaluate_sheet('playerid', 'max', 'foo.bar'))



print("yearid,max = ", evaluate_sheet('yearid', 'min'))
print("hr,min = ", evaluate_sheet('hr', 'min'))
print("hr,sum = ", evaluate_sheet('hr', 'sum'))
print("hr,avg = ", evaluate_sheet('hr', 'avg'))



