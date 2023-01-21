faculty_code = ['01', '02', *range(20, 41), 51, 53, 55, 58]
faculty_code = map(str, faculty_code)
print("OK") if input() in faculty_code else print("Error")