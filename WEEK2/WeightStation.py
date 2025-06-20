"""WeightStation"""
def main():
    """WeightStation"""
    average_weight = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    weight4 = (average_weight*4)-weight1-weight2-weight3
    total_weight = weight1+weight2+weight3+weight4
    half_average = average_weight/2
    lower_bound = average_weight - half_average
    upper_bound = average_weight + half_average
    if total_weight > 15000:
        print("Overweight")
    elif lower_bound <= weight1 <= upper_bound:
        if lower_bound <= weight2 <= upper_bound:
            if lower_bound <= weight3 <= upper_bound:
                if lower_bound <= weight4 <= upper_bound:
                    print(f"Pass {weight4:.2f}")
                else:
                    print("Unbalance")
            else:
                print("Unbalance")
        else:
            print("Unbalance")
    else:
        print("Unbalance")
main()
