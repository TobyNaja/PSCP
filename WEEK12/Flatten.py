"""dsad"""
def flatten_and_sort(lst):
    """ทำให้ list แบนเรียบและเรียงตัวเลขจากมากไปน้อย"""
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_and_sort(item))
        else:
            flat_list.append(item)
    return sorted(flat_list, reverse=True)
lst = eval(input())
print(flatten_and_sort(lst))
