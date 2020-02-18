def three_sum_closest(list_ints, s):
    list_ints = sorted(list_ints)
    p1 = 0
    p2 = p1+1
    len_list = len(list_ints)
    p3 = len_list - 1
    curr_sum = 0
    closest_sum = '#'
    while p2 < p3:
        curr_sum = list_ints[p1] + list_ints[p2] + list_ints[p3]
        if closest_sum != "#":
            if curr_sum == s:
                closest_sum = curr_sum
                break
            if (abs(s - curr_sum) < abs(s - closest_sum)):
                closest_sum = curr_sum
            if curr_sum > s:
                p3 -= 1
            else:
                p2 += 1
        else:
            closest_sum = curr_sum
        if p2 == p3:
            p1 = p1 + 1
            p2 = p1 + 1
            p3 = len_list - 1
    print(list_ints[p1] + list_ints[p3] + list_ints[p2])


three_sum_closest([-4, -8, -10, -9, -1, 1, -2, 0, -8, -2], 0)
