"""import serial
# 创建串口对象
ser = serial.Serial('COM3', 115200, timeout=None)

if ser.is_open:
    print("串口已打开")

# 发送数据
data_to_send = '' # 将要发送的数据转换为字节格式
ser.write(data_to_send)

# 关闭串口连接
ser.close()"""
"""
def send_serial(port, baudrate, data):
    ser = serial.Serial(port, baudrate, rtscts=True)
    ser.write(data.encode())
    ser.close()


if __name__ == "__main__":
    port = "COM3"  # 根据您的系统和串口设备更改
    baudrate = 115200  # 根据您的实际需求更改
    data = "000"  # 您要发送的数据
    send_serial(port, baudrate, data)"""
"""import serial
import codecs

def send_serial(port, baudrate, data):
    ser = serial.Serial(port, baudrate)
    encoded_data = codecs.encode(data, 'gbk')  # 将字符串编码为utf-8格式的字节
    ser.write(encoded_data)
    ser.close()

if __name__ == "__main__":
    port = "COM4"  # 根据您的系统和串口设备更改
    baudrate = 115200  # 根据您的实际需求更改
    data = "你好" # 需要发送的汉字字符串
    send_serial(port, baudrate, data)"""
"""import serial
import struct

# 配置串口参数
ser = serial.Serial('COM4', 115200)  # 替换为您的串口和波特率

# 准备要发送的数据
id=12
heart = 80
respiration = 18
blinks = 5
pulse = 70
wounds = '无'
temperature = 36.5

# 将字符串编码为GBK格式
wound = wounds.encode('utf-8')

# 将数据打包为二进制格式
data = struct.pack( 'iiff8s f',id,heart, respiration, blinks, pulse, wound, temperature)

# 发送数据到串口
ser.write(data)

# 关闭串口
ser.close()"""

"""import serial
import time

# 打开串口
ser = serial.Serial('COM5', 115200)  # 根据实际情况修改串口号和波特率


def send_data(data_type, value):
    # 构造要发送的数据格式
    data = data_type + ":" + value

    # 发送数据
    ser.write(data.encode())  # 根据实际情况进行编码


# 发送有眨眼数据
send_data("blinks", "有")

# 停顿一段时间，等待接收方处理数据
time.sleep(1)

# 发送无眨眼数据
send_data("blinks", "无")

# 关闭串口
ser.close()"""


"""import serial

# 打开串口
ser = serial.Serial('COM5', 115200)  # 根据实际情况修改串口号和波特率

def send_data(data_type, data_values):
    message = f"{data_type}:{','.join(data_values)}\n"  # 数据类型和数值用冒号分隔并添加换行符
    ser.write(message.encode())

# 示例数据
heart_data = ["70"]
respiration_data = ["15"]
blinks_data = ["2"]
pulses_data = ["10"]
wounds_data = ["1"]
temperature_data = ["36.5"]
latlon_data = ["40.7128,-74.0060"]

# 发送心率数据
send_data("heart", heart_data)

# 发送呼吸数据
send_data("respiration", respiration_data)

# 发送眨眼数量数据
send_data("blinks", blinks_data)

# 发送脉搏数量数据
send_data("pulses", pulses_data)

# 发送伤口数量数据
send_data("wounds", wounds_data)

# 发送温度数据
send_data("temperature", temperature_data)

# 发送经纬度数据
send_data("latlon", latlon_data)

# 关闭串口
ser.close()"""
"""import serial

# 设置串口参数
ser = serial.Serial('COM5', 115200, timeout=1)

# 发送心率数据
heart_data = "heart:12"  # 替换为实际的心率数据
heart_data_bytes = heart_data.encode('GBK')
ser.write(heart_data_bytes)"""

"""# 发送呼吸数据
respiration_data = "respiration:45"  # 替换为实际的呼吸数据
respiration_data_bytes = respiration_data.encode('gbk')
ser.write(respiration_data_bytes)

# 发送眨眼数据
blinks_data = "blinks:1"  # 替换为实际的眨眼数据
blinks_data_bytes = blinks_data.encode('gbk')
ser.write(blinks_data_bytes)

# 发送脉搏数据
pulses_data = "pulses:1"  # 替换为实际的脉搏数据
pulses_data_bytes = pulses_data.encode('gbk')
ser.write(pulses_data_bytes)

# 发送伤口数据
wounds_data = "wounds:1"  # 替换为实际的伤口数据
wounds_data_bytes = wounds_data.encode('gbk')
ser.write(wounds_data_bytes)

# 发送体温数据
temperature_data = "temperature:36.5,36.7,36.8"  # 替换为实际的体温数据
temperature_data_bytes = temperature_data.encode('gbk')
ser.write(temperature_data_bytes)

# 发送经纬度数据
latlon_data = "latlon:39.9042,116.4074"  # 替换为实际的经纬度数据
latlon_data_bytes = latlon_data.encode('gbk')
ser.write(latlon_data_bytes)"""


import serial

# 打开串口
ser = serial.Serial('COM3', 115200)  # 根据实际情况修改串口号和波特率

def send_data(data_type, data_value):
    # 根据数据类型构造要发送的数据
    if data_type == "heart":
        data = f"heart:{data_value}\n"
    elif data_type == "respiration":
        data = f"respiration:{data_value}\n"
    elif data_type in ["blinks", "pulses", "wounds", "temperature", "latlon"]:
        data = f"{data_type}:{','.join(str(value) for value in data_value)}\n"

    # 发送数据到串口
    ser.write(data.encode())  # 根据实际情况进行编码

# 示例数据
heart_data = 75
respiration_data = 18
blinks_data = [1]
pulses_data = [80]
wounds_data = [5]
temperature_data = [36.5]
latlon_data = ["40.7128,-74.0060"]

try:
    # 发送心率数据
    send_data("heart", heart_data)

    # 发送呼吸数据
    send_data("respiration", respiration_data)

    # 发送blinks数据
    send_data("blinks", blinks_data)

    # 发送pulses数据
    #send_data("pulses", pulses_data)

    # 发送wounds数据
    send_data("wounds", wounds_data)

    # 发送temperature数据
    send_data("temperature", temperature_data)

    # 发送latlon数据
    send_data("latlon", latlon_data)

finally:
    ser.close()