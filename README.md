# DSP_301_asm2
Nộp bài ASM2 môn DSP_301: chấm điểm học sinh và lưu file tổng kết tự động. 

GIỚI THIỆU
Đây là một công cụ được viết bằng ngôn ngữ Python chỉ bao gồm một file. Được dùng để xử lý các tập điểm thi của học sinh, đưa ra một vài phân tích cơ bản, cuối cùng là lưu tự động điểm của học sinh sau khi chấm vào file định dạng .txt. 

YÊU CẦU:
Để chạy được file Python này, hệ thống của bạn cần có các gói công cụ được cài đặt như dưới đây: 
- Python 3
- Thư viện Pandas
- Thư viện Numpy

HƯỚNG DẪN:
- Tải xuống file python ở đây.
- Copy đường dẫn đến thư mục chứa các file lớp. 
- Thay phần đường dẫn vào str đầu tiên ở vị trí: 
    + dòng 8: filepath1 =  "/Users/hoalam/this mac/Data Sciency/GT_KHDL/data_file_asm2/" + filename + ".txt"
    + dòng 105: fullpath = "/Users/hoalam/this mac/Data Sciency/GT_KHDL/data_file_asm2/Output/"+ filename + "_grade.txt"
    Để tạo đường dẫn tới file lớp cần phân tích và đường dẫn khác tới thư mục sẽ chứa file sẽ lưu điểm.
- Chạy file hiện ra dòng: "Enter a file name: ", nhập tên file lớp. Ví dụ: class1.
- Khi hiện ra báo cáo cơ bản về điểm lớp và đã lưu được danh sách học sinh kèm điểm thi,
    trình duyệt hiện ra dòng: "Kiểm tra lớp khác (0,1)"
    + Nhập 1 để kiểm tra lớp tiếp theo;
    + Nhập 0 để kết thúc chương trình.

CHỨC NĂNG:
- Kiểm tra và in ra các dòng không hợp lệ bao gồm: Mã học sinh và đáp án
- Báo cáo số lượng học sinh có điểm tổng kết > 80
- Báo cáo điểm trung bình
- Báo cáo điểm cao nhất
- Báo cáo điểm thấp nhất 
- Báo cáo miền giá trị của điểm
- Báo cáo trung vị
- Câu bị bỏ qua nhiều nhất và câu sai nhiều nhất
- Xuất file điểm của từng học sinh

TIẾP THEO: 
- Hỏi kiểm tra lớp khác. 












