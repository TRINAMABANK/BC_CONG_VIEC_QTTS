import http.server
import socketserver
import socket
import webbrowser
import os
import sys

# Đảm bảo in tiếng Việt chuẩn trên Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 8080

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    local_ip = get_local_ip()
    
    print("=" * 60)
    print(" WEBAPP BÁO CÁO NGÀY CBNV BP QTTS - LOCAL SERVER")
    print("=" * 60)
    print(f"\n[+] Link mở trên Máy tính (PC / Laptop):")
    print(f"    http://localhost:{PORT}")
    print(f"\n[+] Link mở trên Điện thoại (cùng mạng Wi-Fi):")
    print(f"    http://{local_ip}:{PORT}")
    print("\n" + "=" * 60)
    print(" Máy chủ đang chạy... Nhấn Ctrl + C để dừng.")
    print("=" * 60 + "\n")
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã tắt máy chủ.")
