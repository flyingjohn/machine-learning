<h1>numpy基本</h1>

1:创建矩阵
首先，通过numpy创建的矩阵和一般多为数组不一样，它存在一些属性，因此，如果想要从
python数组转化为numpy数组的话，可以通过array函数。
a=[1,2,3] a=numpy.array(a)<br/>
The function zeros creates an array full of zeros, the function ones creates an 
array full of ones, and the function empty creates an array whose initial content 
is random and depends on the state of the memory. By default, the dtype of the 
created array is float64.<br/>
通过zeros,ones,empty可以忽略初始化，自动添加相应得到数据,默认dtype是float64
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

8:zeros函数构建矩阵
numpy.zeros(shape, dtype=float, order='C')
shape是元组（m,n）分别代表行和列
dtypr不解释，order可以忽略，官网上讲的是Whether to store multidimensional data in C- or Fortran-contiguous (row- or column-wise) order in memory，意思就是说在内存中是优先储存行还是列，C是前者。

9:切片以及迭代
单维度上面可以进行切片，比如说:</br>
import numpy as np</br>
a=np.array([[1,2,3],[2,3,4],[3,4,5]])</br>
因为a是2维的，所以如果想要得到2行2列的数3，可以使用a[1][1],也可以使用a[1,1],在numpy里面可以使用a[1,1]的形式进行索引，逗号分隔的就是维度。也可以使
用a[(1,1)]的形式，里面使用元组。如果使用a[1:2]那么得到的就是[2,3,4],这就是numpy的切片，在某个维度上切片，语法和python切片一致。此时由于省略了其他
维度的信息，numpy会默认的添加成a[1:2,:]的形式，也就是其他为全取，也可以使用...来代替其他维度的信息，也就是说a[1:2,...]结果相同。numpy的array支持for in 语法，迭代的是每一行（如果是二维的），那么如果是三维的，比如说</br>
d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])</br>
for row in d:</br>
  print row</br>
结果是</br>
[[1 2]</br>
 [3 4]]</br>
[[5 6]</br>
 [7 8]]</br>
 也就是说不管多少维，一次for in 就是最外层那一维的一行。如果想得到所有元素，最里层的每个元素，就是1,2,3这些，那么需要使用array的flat属性：
 for element in d.flat:</br>
  print element</br>
 结果是1,2,3,4,5,6,7,8，也就是说他会不断地迭代知道找到里面的元素，不管存在多少维。</br>
 
 10.产生随机数组
 使用np.random模块里面的函数可以产生随机数以及根据某些分布产生数组。官网https://docs.scipy.org/doc/numpy/reference/routines.random.html
 可以使用np.random.rand(d1,d2,...,dn)产生随机数组，输入不是元组，如果需要输入是元组，那么使用np.random.random或者np.random.random_sample,
np.random.rand(3,2)
array([[ 0.14022471,  0.96360618],  #random
       [ 0.37601032,  0.25528411],  #random
       [ 0.49313049,  0.94909878]]) #random
产生的是均匀分布在[0,1)  ]的均匀分布。
np.random.random和random_sample参数是元组，产生的连续均匀分布在[0,0,1.0)  ]的数组。
根据分布产生数组类似，
python:mu, sigma = 0, 0.1 # mean and standard deviation
python:s = np.random.normal(mu, sigma, 1000)
s产生的就是服从正态分布的数组

11.产生矩阵
前面所有产生矩阵的函数，比如说eye,one,ones,zero,zeros,array,random.rand等都产生的是array,也就是数组，不是矩阵，矩阵只能是二维的，矩阵可以
使用*,** 等运算，数组也可以使用这些运算,只是意义不一样，结果也可能不一样。只有二维的数组可以通过matrix和mat产生相应的矩阵，</br>
mat=matrix(data,copy=False)</br>
a=np.mat('4 3; 2 1')</br>
c=np.array([[4, 3], [2, 1]])</br>
print(a**2)</br>
[[22 15]</br>
[10  7]]</br>
print(c**2)</br>
[[16  9]</br>
[ 4  1]]</br>
可以查看http://blog.csdn.net/vincentlipan/article/details/20717163 ，只不过里面说矩阵只能dot进行乘法运算是错误的，也可以使用*.</br>

12.数组遍历
numpy里面ndarray(也就是array)存在一个十分便利的遍历方式,比如说向比较数组里面元素是否>0.5:</br>
python:b=numpy.random.random(3,3)</br>
python:b>0.5</br>
会返回这样的矩阵</br>
[[FALSE,TRUE,FALSE],[...],[...]]之类的</br>
让里面所有的大于0.5的数赋值为1，那么</br>
b[b>0.5]=1</br>
