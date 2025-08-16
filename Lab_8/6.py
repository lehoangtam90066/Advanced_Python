import requests

# Thiết lập các tham số cho API
parameters = {"lat": 37.78, "lon": -122.41}

# Gọi API để lấy dữ liệu
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Kiểm tra mã trạng thái của phản hồi
if response.status_code == 200:
    try:
        # Chuyển đổi dữ liệu trả về sang định dạng JSON
        json_data = response.json()

        # In ra loại dữ liệu
        print(type(json_data))

        # In ra toàn bộ dữ liệu JSON
        print(json_data)

        # Bổ sung đoạn mã để lấy duration của phần tử đầu tiên
        if 'response' in json_data and len(json_data['response']) > 0:
            duration = json_data['response'][0]['duration']
            print("Duration of the first element:", duration)
        else:
            print("No response data available.")
    except ValueError:
        print("Error decoding JSON. Response content:")
        print(response.text)  # In ra nội dung phản hồi để kiểm tra
else:
    print(f"Error: Received response with status code {response.status_code}.")
    print("Response content:", response.text)  # In ra nội dung phản hồi để kiểm tra
