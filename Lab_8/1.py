import json
from urllib.error import URLError, HTTPError
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Dữ liệu danh sách các chuỗi
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]

# Chuyển đổi danh sách thành chuỗi JSON
best_food_chains_string = json.dumps(best_food_chains)

# Tạo và ghi dữ liệu JSON vào file HTML
try:
    # Mở tập tin HTML để ghi
    with open("best_food_chains.html", "w", encoding="utf-8") as file:
        # Viết nội dung HTML với chuỗi JSON được bao bọc trong thẻ <pre> để dễ nhìn
        file.write("<html><body><h2>Danh sách các chuỗi cửa hàng thức ăn nhanh:</h2>")
        file.write("<pre>" + best_food_chains_string + "</pre>")
        file.write("</body></html>")
    print("Dữ liệu đã được ghi vào file 'best_food_chains.html'.")

except (URLError, HTTPError) as e:
    # Xử lý lỗi khi có vấn đề trong quá trình thao tác URL
    print(f"Lỗi xảy ra: {e}")

# Nhận xét kết quả:
# Khi mở tập tin best_food_chains.html trong trình duyệt, bạn sẽ thấy tiêu đề và
# danh sách các chuỗi cửa hàng thức ăn nhanh được hiển thị trong định dạng JSON.
# Dữ liệu được định dạng dễ đọc và rõ ràng, giúp người xem dễ dàng nắm bắt nội dung.
