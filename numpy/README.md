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

4：非字符型数据类型
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
复数不能转化为除了布尔型之外的任何类型,numpy里面复数的形式是a+bj的形式，b必须有，
就算是0也是0j,而且中间不能加上* ,也就是说只能写成1+0j的形式，不是1+2* j之类的。
</B>

5：eye函数
eye函数的作用是产生对角矩阵，一般是用来产生单位阵，但是它可以产生N!=M的矩阵。
numpy.eye(N, M=None, k=0, dtype=<type 'float'>)
N:行数
M:列数，如果不指定的话和N一样
K:偏移，默认是0，如果是1的话，左上角移到第二列，类似
array([[ 0.,  1.,  0.],
       [ 0.,  0.,  1.],
       [ 0.,  0.,  0.]])
</br>

6:allclose()函数
用于比较两个矩阵是否是相近的，不是相等，只要他们的差距满足一定的条件就行，具体的描
述在https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html
</br>

7:矩阵求逆矩阵
使用numpy.linalg.inv(a)就可以求出逆矩阵，逆矩阵与原矩阵满足
dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])也就是相乘等于单位矩阵


