# NemoIdAccount

Thông tin tài khoản NemoWallet.
## Các thuộc tính
Tên | Kiểu dữ liệu | Mô tả | Ghi chú
------------ | ------------- | ------------- | -------------
**sub** | **str** | Đây là mã định danh của người dùng, duy nhất trong tất cả các tài khoản NEMO ID  | [tùy chọn] 
**email** | **str** | Địa chỉ email của tài khoản | [tùy chọn] 
**email_verified** | **bool** | Xác minh email đã được thực hiện hay chưa | [tùy chọn] 
**name** | **str** | Tên người dùng | [tùy chọn] 
**gender** | **str** | Giới tính | [tùy chọn] 
**birthday** | **str** | Ngày sinh | [tùy chọn] 
**profile_picture** | **str** | Liên kết đến hình ảnh trang cá nhân của tài khoản | [tùy chọn] 
**public_key** | **str** | Khóa công khai được sử dụng để xác thực yêu cầu JSON-RPC | [tùy chọn] 
**redirect_uri** | **str** | URI chuyển hướng | [tùy chọn] 
**client_id** | **str** | ID của Client | [tùy chọn] 
**access_token** | **str** | Mã thông báo được sử dụng để truy cập dịch vụ | [tùy chọn] 
**expires_in** | **int** | Thời gian (giây) tính từ lúc tạo mã thông báo, mà mã thông báo có hiệu lực | [tùy chọn] 
**id_token** | **str** | JWT chứa thông tin xác thực của người dùng, được ký bởi NEMO ID | [tùy chọn] 
**refresh_token** | **str** | Mã thông báo làm mới | [tùy chọn] 
**token_type** | **str** | Loại token | [tùy chọn] 
**google_two_factor_authentication** | **bool** | Xác thực g2fa có được bật hay không | [tùy chọn] 
**fund_password** | **bool** | Mật khẩu quỹ được bật hay không | [tùy chọn] 
**signature** | **object** | Phản hồi chữ ký từ máy chủ, được sử dụng cho các yêu cầu JSON-RPC | [tùy chọn] 
**nemo_address** | **str** | Địa chỉ Ethereum của NemoWallet | [tùy chọn] 
**wallet_address** | **list** | Các địa chỉ Ethereum của các ví MetaMask được liên kết" | [tùy chọn] 

[[Quay lại đầu trang]](#) [[Quay lại danh sách API]](./README.md#tài-liệu-về-api-endpoints) [[Quay lại danh sách Model]](./README.md#tài-liệu-về-models) [[Quay lại README]](./README.md)