## Programming Code:
* Câu 1: Làm recursion
* Câu 2: list conprehension
* Câu 3: higher order function

self.visit(ctx.ids())
ctx.ids().accept(self)
## 5 khẩu quyết:
    1. Viết từ dưới lên trên. Vì luật sinh có nhiều token (terminal) ở dưới. Luật sinh nào.
    2. Có bao nhiêu luật sinh con thì xử lý riêng bấy nhiêu trường hợp.
    3. Từ cha chỉ quan đến con, không quan tâm đến con của con.
    4. Cứ gặp non-terminal node thì dùng visit. Khi gọi visit xong là phải biết nó trả về cái gì.
    5. Khi xử lí 1 node, ta phải cố gắng nhìn vào các lớp AST> Xem thử với cái dữ liệu của cái node đó thì tạo được cái gì thì ta phải tạo được nhiều nhất có thể. 
    6. Nếu viết bằng BNF mà không biết kết hợp sao thì kết hợp lại đi thì 60% là chạy 