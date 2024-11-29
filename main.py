import json


def sum_prop(num: int, gender: str, case: str):
    table = ""
    with open('table.json', 'r') as file:
        table = json.load(file)
    if num == 0:
        print(table["0"][gender])
    temp_num = num
    segments = [""]
    i_segments = 0
    while temp_num > 0:
        i_segments = i_segments + 1
        temp_str = str(temp_num)
        segments.append(temp_str[-4:])
        temp_num = temp_num // 1000
    total_str_num = ""
    while i_segments > 0:
        nums = [""]
        for char in segments[i_segments]:
            nums.insert(1, char)
        i_nums = len(nums) - 1
        sum_num = 0
        while i_nums > 0:
            sum_num = sum_num + int(nums[i_nums])
            temp_str_num = ""
            if i_segments == 1 and i_nums == 1 and (nums[i_nums] == "1" or nums[i_nums] == "2"):
                temp_str_num = table[str(i_segments)][str(i_nums)][nums[i_nums]][gender][case]
            elif i_nums == 2 and nums[i_nums] == "1":
                temp_str_num = table[str(i_segments)][str(i_nums)][nums[i_nums]][nums[i_nums - 1]][gender]
                nums[1] = "0"
            else:
                temp_str_num = table[str(i_segments)][str(i_nums)][nums[i_nums]][gender]
            if temp_str_num != "":
                total_str_num = total_str_num + temp_str_num + " "
            i_nums = i_nums - 1
        if i_segments != 1 and sum_num != 0:
            temp_word = table[str(i_segments)]["s"][nums[1]][gender]
            total_str_num = total_str_num + temp_word + " "
        i_segments = i_segments - 1
    print(total_str_num)


sum_prop(14, "и", "ж")




