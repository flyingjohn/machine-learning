numpy的基本函数

1:创建矩阵
首先，通过numpy创建的矩阵和一般多为数组不一样，它存在一些属性，因此，如果想要从
python数组转化为numpy数组的话，可以通过array函数。
a=[1,2,3] a=numpy.array(a)<br/>
The function zeros creates an array full of zeros, the function ones creates an 
array full of ones, and the function empty creates an array whose initial content 
is random and depends on the state of the memory. By default, the dtype of the 
created array is float64.<br/>
通过zerons,ones,empty可以忽略初始化，自动添加相应得到数据<br/>
range可以从start,stop,step,dtype创建数据<br/>
linspace可以自动的等距创建数据，numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)如果retstep为true的话返回的不仅仅是array
还要返回step([],)<br/>

2:运算
**
.sum() .min() .max()其中，可以在上述函数里面加上参数axis=?,?从1开始，1代表最里层，
也就是单个数字

3:dot
对于标量来说，乘法，np.dot(3,4)=12,对于向量来说，内积， np.dot([2j, 3j], [2j, 3j])=(-13+0j)，对于
矩阵来说，dot就代表矩阵乘法 
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.dot(a, b)=array([[4, 1],[2, 2]])

tips:
numpy里面复数使用j来表示，而不是i,也就是说上面的2j实际上就是复数，是complex类型



