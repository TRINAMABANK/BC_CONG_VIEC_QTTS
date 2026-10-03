# BÁO CÁO NGÀY CBNV BP QTTS (NAM A BANK)

Ứng dụng Web Mobile & PWA quản lý và tự động tổng hợp báo cáo công việc hàng ngày chuẩn hành chính dành cho Cán bộ Nhân viên Bộ phận Quản trị Tài sản (Phòng HCQT - Nam A Bank).

![NAM A BANK](https://img.shields.io/badge/NAM%20A%20BANK-Ph%C3%B2ng%20HCQT-0072ce?style=for-the-badge)
![PWA Ready](https://img.shields.io/badge/PWA-Ready-16a34a?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## 🌟 Tính năng nổi bật

- **Giao diện chuẩn Doanh nghiệp:** Toàn bộ ứng dụng sử dụng chuẩn font **Times New Roman**, màu xanh thương hiệu Nam A Bank sang trọng, tối ưu 100% cho màn hình điện thoại và máy tính.
- **Thống kê thời gian thực:** Tự động đếm Tổng số việc, Việc hoàn thành, Việc đang xử lý trong ngày.
- **Nhập liệu & Quản lý nhanh:**
  - Nhập nội dung công việc nhiều dòng.
  - Phân loại theo đúng 7 nhóm việc: *Mua sắm, Quản lý tài sản, Sửa chữa, Vận hành, Hành chính, Họp / Trao đổi, Khác*.
  - Đánh dấu hoàn thành (gạch ngang nội dung), hỗ trợ chỉnh sửa (✏️) và xóa (🗑️).
- **Tự động tổng hợp báo cáo:**
  - Cấu trúc chuẩn: *Kính gửi Ban Lãnh đạo*, *I. Các việc đã hoàn thành*, *II. Các việc đang xử lý / tiếp tục ngày mai*, *III. Công việc phát sinh / vấn đề cần hỗ trợ*, *Trân trọng*.
- **Xuất File Word (.doc) chuẩn mẫu:**
  - Tự động chèn tiêu đề chuẩn **NAM A BANK – Phòng HCQT** & **Quốc hiệu Tiêu ngữ**.
  - Định dạng chuẩn khổ giấy A4, lề chuẩn, khoảng cách dòng `Before: 0pt` và `After: 0pt` theo quy chuẩn soạn thảo văn bản hành chính.
- **Gửi Email & Sao chép nhanh:** Tích hợp mở ứng dụng Email với tiêu đề và nội dung điền sẵn, sao chép báo cáo vào clipboard chỉ với 1 click.
- **Progressive Web App (PWA):**
  - Cài đặt trực tiếp lên màn hình điện thoại iPhone (Safari) / Android (Chrome) không cần qua App Store.
  - Hoạt động offline mượt mà với Service Worker.
  - Lưu trữ dữ liệu an toàn trên trình duyệt (LocalStorage).

---

## 🚀 Hướng dẫn cài đặt & Chạy ứng dụng

### 1. Mở trực tiếp (Offline)
- Mở trực tiếp file `index.html` bằng trình duyệt web bất kỳ.
- Hoặc click đúp chuột vào file `Chay_Phan_Mem.bat` trên Windows.

### 2. Chạy Server cục bộ kết nối Điện thoại
1. Click đúp vào `Chay_May_Chu_Ket_Noi_Dien_Thoai.bat` (hoặc chạy lệnh `python server.py`).
2. Mở trình duyệt trên điện thoại (cùng mạng Wi-Fi) và truy cập vào link IP hiển thị trên màn hình (ví dụ: `http://192.168.1.10:8080`).

---

## 📂 Cấu trúc thư mục

```text
├── index.html                           # Giao diện chính Web App (HTML, CSS, JS)
├── manifest.json                        # Khai báo cấu hình PWA Web App
├── sw.js                                # Service Worker hỗ trợ offline
├── icon.svg                             # Biểu tượng vector ứng dụng BP QTTS
├── server.py                            # Máy chủ Web server Python cục bộ
├── Chay_Phan_Mem.bat                    # File 1-click mở giao diện dạng App Desktop
├── Chay_May_Chu_Ket_Noi_Dien_Thoai.bat  # File 1-click khởi động Web Server
└── README.md                            # Tài liệu dự án
```

---

*Phát triển phục vụ công tác báo cáo công việc hàng ngày CBNV BP QTTS - Nam A Bank.*
