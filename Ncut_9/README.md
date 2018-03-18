作者主页在http://www.cis.upenn.edu/~jshi/software/，其中代码有一个bug,在eigs_new里面存在matlab版本不兼容导致的bug,matlab 2008b ~ 2013a之间的版本能够使用，
其余版本会报错，error using arpackc , expect 2 ouput arguments,其余版本需要
把ncut.m里面81行的eigs_new改为eigs。