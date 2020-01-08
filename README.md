# 資料結構演算法
希望能在這堂課有所收穫，並持續努力進步成長喔~

## 自我介紹:
我是巨資三B的鄭安傑，希望2020能把2019的願望完成:) <>
此生無大志，求每科過就好了~

## 上課第二周
### Linked List 與 Array 的優缺點
#### Array 優點
1. random access：只要利用index即可在O(1)時間對Array的資料做存取。
2. 較Linked list為節省記憶體空間：因為Linked list需要多一個pointer來記錄下一個node的位置。
#### Array 缺點
1. 新增/刪除資料很麻煩：若要在第一個位置新增資料，就需要把矩陣中所有元素往後移動。同理，若要刪除第一個位置的資料，也需要把矩陣中剩餘的元素往前移動。

#### Linked List 優點
1. 新增/刪除資料較Array簡單，只要對O(1)個node調整pointer即可，不需要如同Array般搬動其餘元素。
2. Linked list的資料數量可以是動態的，不像Array會有resize的問題。

#### Linked List 缺點
1. 因為Linked list沒有index，若要找到特定node，需要從頭開始找起，搜尋的時間複雜度為O(N)。
2. 需要額外的記憶體空間來儲存pointer。
## 上課第三周
#### Stack(堆疊)
堆疊(stack)是先進後出(FILO First In Last Out)的資料結構，意思是，先進去的資料最後出來。
可以使用push( )與pop( )來實現。

