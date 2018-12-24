from pip._vendor.distlib.compat import raw_input


print("-----------------------------1--------------------------------")
#输入一个年份，打印第四个元素
fourth = raw_input('Year:   ')[3]
print(fourth)

print("--------------------------2-----------------------------------")

#索引的使用
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
ending = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
year = raw_input('Year:   ')
month = raw_input('Month(1-12):   ')
day = raw_input('Day(1-31):   ')
print(type(month))
print(type(year))
print(type(day))

#输入的字符都是字符串类型需要进行数值的转换
month_number = int(month)
day_number = int(day)

#索引访问数据的时候记得 -1 的操作
month_name = months[month_number - 1]
ordinal = day + ending[day_number - 1]

print( month_name + '   ' + ordinal + ',  ' + year)


