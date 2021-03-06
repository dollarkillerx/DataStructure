# DataStructure

### 复杂度分析
1. [时间复杂度&空间复杂度](./时间复杂度.md) T(n) = O(f(n))
2. [最好，最坏，平均，均摊 时间复杂度](./深入时间复杂度.md)

### 数组
> 数组在内存中依次存储 开辟一块连续的内存空间
`[0,1,2,3,4,5,6,7,8,9,10]`
- 查询和修改时间复杂度：
应该list是连续的内存空间 所以 可以通过寻址公式来来更具下标随机访问
下标×每块地址
所以数组查询时间复杂度为 O(1)
- 增加和删除时间复杂度：
应为数组的存储结构是连续的 当添加和删除一个数据的时候 这个数据后面的元素都会发生改变
例如：
[0,1,2,3,4,5,6]
当删除1的时候2,3,4,5,6都会往前移动以为 添加于次相同 so 时间复杂度为O(n)

### 链表
> 链表在数据中存储的结构为链式
开头 -> 0|next -> 1|next -> 2|next -> 3|next ->null
第一个数据指第二个数据的头 依次  so 查询需要遍历整个链表 
- 查询时间复杂度为O(n)
- 删除只需更改指针的指向 so 删除和添加的时间复杂度为O(1)
- 删除数据需要先找到 查询时间复杂度为O(n) 删除的时间复杂度为O(1) so更具加法法则 时间复杂度为O(n)

### 链表 和 数组
链表查询时间复杂度为：O(n) 更新时间复杂度为O(1)
数组通过下标随机访问查询时间复杂度为:O(1) 更新和插入时间复杂度为O(n)

### 栈
> 先进先出
入栈和出栈的时间复杂度为O(1)
当栈的容量满了的时候，复杂度为O(n)

### 队列
> 先进后出
阻塞队列： 队列里面没有数据的时候 读取就会阻塞，当队列里面数据满了的时候 写入就会阻塞
并发队列： 当多线程读取的时候，加锁 

### 递归
> 递归 把一个问题分成多个子问题，解决
比如 你在电影院想要知道自己在那个位置，but自己又不知道自己在那个位置 ，你就要问你的前排他在那个位置 你的位置是他的位置的加一，
SO 他也不知道他在那个位置 他就要继续先上问 这就是一个递归。当问到第一个人他在那个位置 他会告诉你我在第一个位置
f(1) = 1
f(n) = f(n-1) +1
```
public there(n) {
    if(n==1) return 1;
    return f(n-1) +1;
}
```
又因为数据的生成是在栈中的，高规模的数据会导致内存溢出  so 必须对递归的规模最限制
递归会生成大量的数据 空间复杂度就会变高 so 递归虽然简单，but 这消耗资源也太大了
### 排序算法
#### 冒泡排序
> 这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端（升序或降序排列），就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名“冒泡排序”。
```
int[] test = {5,3,10,8,3,1}
for(int i=0;i<test.length-1;i++){
    for(int p;p<test.length-1-i;p++){
        if(int[p]>int[p+1]){
            int temp = int[p+1];
            int[p+1]=int[p];
            int[p] = temp;
        }
    }
}
```

#### 二分查询
```
int[] test = {1,2,3,4,5,6,7,8,9};
int start = 0;
int end = test.length - 1;
while(start <= end){
    mid = (start + end)/2;
    guess = test[mid];
    if(guess == mid) {
        return mid;
    }
    if(guess > item) {
        start = mid - 1;
    }else{
        low = mid + 1;
    }

}
```
#### 插入排序
> 插入排序从第二个开始与前面的做比较如果小就交换
```
int[] test = {2,45,48,4,7,59,1};

```

#### 选择排序
> 两个数组 一个需要排序的数组 一个是空数组
> 将待排序数组中的最大的存入 空数组中 以此类推
```
int[] test1 = {4,5,1,2,3,6,8,0,9,94,1}
int[] test3 = new int[test1.length]
for(int i:test1) {
    int max = max(test1)
    test1.unset(max)
    test3.add(max)
}
```

#### 递归
```
public vido digui(n) {
    if(n>10){
        System.out.println(n);
        n--;
        digui(n);
    }else{
        System.out.println("递归完成");
    }
}
```
> 每个递归都要两个条件: 基线条件和递归条件

#### 栈
> 所有函数的调用都会进入调用栈

#### 快速排序 divide and conquer ,D&C 分而治之
- 编写一个sum函数计算数组中的值
```
int[] test = {1,2,3,4,5,6,7,8,15};
public int sum (int[] test) {
    if(test.length!=0) {
        return test[0] + sum(test) // 貌似这里不能够移除啊,还是要用ArrayList来做 
    }
}
List<Interget> test = Arrays.asList(test);;
public int sum (List<Interget>  test) {
    if(test.length!=0) {
        return test[0] + sum(test.remove(0))
    }else{
        return false;
    }
}
```

### 散列表
> 数组实现，通过一个 散列函数 当值转换为唯一一个地址存储到数组中，就可以通过寻址公式得到该元素，查询时间复杂度为O(1)