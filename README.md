# Hướng Dẫn Sử Dụng Sản Phẩm Thiết Bị Giúp Nhận Diện Khuôn Mặt và Điểm Danh

![Hình ảnh sản phẩm](link-to-your-image.jpg) <!-- Thay đổi link đến hình ảnh sản phẩm của bạn -->

## Giới thiệu
Chào mừng bạn đến với hướng dẫn sử dụng sản phẩm Thiết bị giúp nhận diện khuôn mặt và điểm danh! Tài liệu này sẽ giúp bạn hiểu rõ hơn về cách sử dụng sản phẩm một cách hiệu quả nhất.

## Nội Dung

1. [Thông Tin Sản Phẩm](#thong-tin-san-pham)
2. [Hướng Dẫn Sử Dụng](#huong-dan-su-dung)
3. [Liên Hệ Hỗ Trợ](#lien-he-ho-tro)

## Thông Tin Sản Phẩm

- **Tên sản phẩm:** Camera nhận diện khuôn mặt
- **Phiên bản python sử dụng:** 3.8.10
## Hướng Dẫn Sử Dụng

### Bước 1: Kiểm Tra Phụ Kiện
- Đảm bảo kết nối chắc chắn và lắp đặt đúng cách cho board camera được gửi cho ban giám khảo bằng dây và điện áp phù hợp

### Bước 2: Lắp Đặt
- Nên lắp đặt ở nơi khô ráo, đảm bảo an toàn và đầy đủ ánh sáng

### Bước 3: Khởi Động
- Chỉ cần cắm nguồn điện và thiết bị sẽ khởi động và kết nối vào wifi
-  **Lưu ý, tên và mật khẩu mặc định của wifi mà thiết bị kết nối là: SSID: noname ; PSK: 12345678** . Giám khảo cần phát wifi trên máy chủ sẽ xử lý dữ liệu, cách làm (cho Windows 11) ở ảnh dưới
-  """""Picture""""""
-  Quan trọng, ở bước này, giám khảo phải thực hiện cài phần mềm trên máy chủ để xử lý (tuy nhiên phần mềm chạy sẽ rất nhẹ nên có thể chạy trên Laptop(gaming) hoặc máy bàn nếu muốn)
-  Tại thư mục vừa tải về, mở cửa sổ terminal (trên window, với đường dẫn tới thư mục và quyền admin) và làm các bước sau:
-  Nhập lệnh 
  ``pip install -r tinsta.txt`` và chờ để hệ thống tải thư viện cần thiết để chạy chương trình
- Sau khi tải xong nhập lệnh ``python app.py``
- Nếu thành công sẽ hiện ra như sau:


### Bước 4: Sử Dụng
- Sau khi thực hiện bước 3 thành công và chương trình không báo lỗi, trên máy chủ đang chạy chương trình, mở trình duyệt web và nhập ``localhost:5000`` , khi này sẽ được đưa tới trang web nơi chương trình đang chạy
- Nếu muốn truy cập web trên thiết bị khác, hãy đảm bảo thiết bị được kết nối vào cùng mạng với máy chủ (SSID:noname ; PSK:12345678) và mở trình duyệt, nhập <ip máy chủ đang chạy>:5000 
- Để biết được ip máy chủ , mở terminal của máy chủ và nhập ``ipconfig`` sẽ nhận được một địa chỉ có mẫu đại loại như 192.168.x.x

## Liên Hệ Hỗ Trợ

Nếu bạn gặp bất kỳ vấn đề nào hoặc cần thêm thông tin, vui lòng liên hệ với chúng tôi qua:

- **Email:** nguyenquanganh460@gmail.com
- **Điện thoại:** 0936249568 (ZALO)

---
Chúng em hi vọng ban giám khảo sẽ hài lòng với sản phẩm này.
