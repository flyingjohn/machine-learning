<h1>numpy基本</h1>

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
<B>
  numpy里面复数使用j来表示，而不是i,也就是说上面的2j实际上就是复数，是complex类型
  一般3x4的矩阵,shape显示(3,4)，numpy里面对于只有一维的矩阵不使用(n)的形式，而是使用(n,)的形式
</B>

4：数据类型
bool	布尔值，一位
int	平台相关整数，int32或int64
int8	字节（-128 ~ 127）
int16	整数（-32768 ~ 32767）
int32	整数（-2 ** 31 ~ 2 ** 31 - 1）
int64	整数（-2 ** 63 ~ 2 ** 63 - 1）
uint8	无符号整数（0 ~ 255）
uint16	无符号整数（0 ~ 65535）
uint32	无符号整数（0 ~ 2 ** 32 - 1）
uint64	无符号整数（0 ~ 2 ** 64 - 1）
float16	半精度浮点，符号位，5 位指数，10 位尾数
float32	单精度浮点，符号位，8 位指数，23 位尾数
float64或float	双精度浮点，符号位，11 位指数，52 位尾数
complex64	复数，由两个 32 位浮点表示（实部和虚部）
complex128或complex	复数，由两个 64 位浮点表示（实部和虚部）
tips:</br><B>
bool()函数只有0返回的是false其余都是true</br>
复数不能转化为除了布尔型之外的任何类型
</B>

