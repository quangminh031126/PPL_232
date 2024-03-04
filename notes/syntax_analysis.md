# Note tuần 3 25/1/2024
## 5 dạng Văn Phạm liên quan đến list thường gặp trong BTL
1. Danh sách của x, không rỗng:

   * **BNF:** 
      xlist <- x xlist | x;
   * **EBNF:** 
      xlist <- x+;
2. Danh sách của x, có thể rỗng:

   * **BNF:** 
      xlist <- x xlist | **empty**;
   * **EBNF:** 
      xlist <- x*;
3. Danh sách của x cách bởi y, không rỗng:

   * **BNF**: 
      xlist <- x y xlist | x;
   * **EBNF**: 
      xlist <- x(y x)*;
4. Danh sách của x cách bởi y, có thể rỗng:

   * **BNF**: 
      xlist <- xprime | empty; 
      xprime <- x y xprime | x;
   * **EBNF**: 
      xlist <- x(y x)* | empty;
5. Văn phạm cho biểu thức trung tố
   * Cái nào xuất hiện *càng sớm* thì ưu tiên *càng thấp*.
   * Đệ quy bên nào thì kết hợp bên đó trước.
