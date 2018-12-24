from pip._vendor.distlib.compat import raw_input
#分片操作是索引操作的扩展，访问一个范围的数据
tag = '<a href = "http://www.python.org">Python web site </a>'
#[9:33] 访问的元素范围为 下标为9至下标为32的元素，而不是下标为33的元素，采用"前闭后开"的方法
print(tag[9:33])


numbers = [1,2,3,4,5,6,7,8,9,10]
#提取下标为3—5的数据,而不是下标3-7的数据
print(numbers[3:6])
print(numbers[0:1])

#访问最后三个元素，这样写能够访问到下标为13的元素，但是最大下标数据为9，因此要取到最好三位数据至少结尾下标为10，如果超界访问只访问提取有的数据，故下标10与14是一致的
print(numbers[7:14])

#从尾部访问后三个元素，无法访问到最后一个元素
print(numbers[-3:-1])

#从尾至头方向访问元素时，只需要置空最后一个索引为即可
print(numbers[-3:])

#左边的索引比右边的索引晚出现，理论上索引10数据出现的时机比索引7出现的时机要晚，换句话说就是不能把后面的索引放到前面一定按照排序顺序写索引，否则结果就都为是空列表
print(numbers[10:7])
#正负放在一起的时候，正的下标访问顺序要高于负的下标
print(numbers[-3:0])

#从头和从尾分别置空最后一个索引来提取队列所有数据
print(numbers[0:])

#下标-11与下标-14在访问提取数据上是一致的，都处于超界的操作，但是这样不违法，只访问提取有的数据
#后置空
print(numbers[-11:])
print(numbers[-14:])

#前置空
print(numbers[:3])
print(numbers[:14])
print(numbers[9])

#访问了所有的下标的数据
print(numbers[:])

#example:对URL进行分割
#url = raw_input("请输入URL： ")
#分割一个列表的时候可以正负下标一起使用
#domain  = url[11:-4]
#print("domain name: " + domain)

#步长的使用和设置，可以将不同分组的数据的首个数据元素遍历出来
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[3:6:2])
#按照步长2将元素组中每隔两个元素返回一个元素
print(numbers[::2])
#ValueError: slice step cannot be zero,步长不能够为0
#print(numbers[1:10:0])
#步长可以为负数，遍历数据从右往左进行访问
#当步长为负数时，下标1被访问应该在下标10之后，因此按照前面的规则，先被遍历的元素放左边，后被遍历的元素放右边，否则得到就是空序列[]
print(numbers[1:10:-1])
#这种元素遍历的写法才是合法的
print(numbers[10:1:-1])

#example：
print(numbers[::4])
print(numbers[8:3:-1])
print(numbers[10:0:2])
print(numbers[0:10:-2])
print(numbers[5::-2])
#根据-2推断出[10:5:-2],而不是[0:5:-2]
print(numbers[:5:-2])
