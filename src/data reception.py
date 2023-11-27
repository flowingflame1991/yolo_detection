"""import serial

# 创建串口对象
ser = serial.Serial('COM3', 115200, timeout=None)

if ser.is_open:
    print("串口已打开")

# 接收数据
data_received = ser.read()  # 根据实际情况设置要接收的数据长度
print("接收到的数据：", data_received.decode('utf-8'))

# 关闭串口连接
ser.close()"""
"""import serial

def read_serial(port, baudrate):
    ser = serial.Serial(port, baudrate)
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print("Received:", data)

if __name__ == "__main__":
    port = "COM4"  # 根据您的系统和串口设备更改
    baudrate = 115200  # 根据E22-900T30S的配置更改
    read_serial(port, baudrate)"""

"""import serial

def read_serial(port, baudrate):
    ser = serial.Serial(port, baudrate)
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('gbk').strip()
                print("Received:", data)
                ser.flush()  # 刷新输出缓冲区
    except KeyboardInterrupt:
        ser.close()
        print("KeyboardInterrupt. Serial port closed.")

if __name__ == "__main__":
    port = "COM3"  # 根据您的系统和串口设备更改
    baudrate = 115200  # 根据您的实际需求更改
    read_serial(port, baudrate)"""
# 保存到文档
"""import serial

def read_e22_data(port, baudrate, output_file):
    ser = serial.Serial(port, baudrate)
    try:
        with open(output_file, "a") as file:
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('gbk').strip()
                    file.write(data + "\n")  # 将数据写入文件
                    file.flush()  # 立即刷新文件缓冲区
    except KeyboardInterrupt:
        ser.close()
        print("KeyboardInterrupt. Serial port closed.")

if __name__ == "__main__":
    port = "COM3"  # 根据您的系统和串口设备更改
    baudrate = 115200  # 根据您的实际需求更改
    output_file = "data.txt"  # 设置保存数据的文件名
    read_e22_data(port, baudrate, output_file)"""

"""import serial
import struct
import pymysql

# 配置串口参数
ser = serial.Serial('COM3', 115200)  # 替换为您的串口和波特率

# 连接到 MySQL 数据库
conn = pymysql.connect(host='localhost', user='root', password='root', database='use')
# 创建游标对象
cursor = conn.cursor()
# 读取串口数据
data = ser.read(20)
# 根据实际情况，调整读取数据的字节数

if data:
    # 解析数据，根据您的数据格式进行解析
    values = struct.unpack('<iiff8sf', data)  # 根据实际数据格式进行解包，<iiff8sf 表示整数、浮点数和字符串的格式

    # 获取数据
    id=values[0]
    heart = values[1]
    respiration = values[2]
    blinks = values[3]
    pulses= values[4]
    wounds = values[5].decode('gbk')
   # temperature = values[6]

# 将数据插入数据库
sql = f"INSERT INTO casualty ( heart_rate, breath, blink, pulse, wound) " \
    f"VALUES ( '{id}','{heart}', '{respiration}', '{blinks}', '{pulses}', '{wounds}');"
cursor.execute(sql)
conn.commit()

# 关闭数据库连接
conn.close()"""
import serial
import pymysql

# 打开串口
ser = serial.Serial('COM5', 115200)  # 根据实际情况修改串口号和波特率

# 连接MySQL数据库
conn = pymysql.connect(
    port = 3306,
    host='127.0.0.1',  # 数据库主机地址
    user='root',  # 数据库用户名
    password='root',  # 数据库密码
    database='wound'  # 数据库名称
)
cursor = conn.cursor()

# 查询最后一行的ID
def get_last_id():
    query = "SELECT id FROM casualty ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0

try:
    while True:
        # 读取串口数据
        data = ser.readline().decode("GBK").strip()  # 根据实际情况进行解码和去除非数据部分

        # 假设数据格式为 "类型:数据1,数据2,数据3..."，使用冒号分隔类型和数据
        if ":" in data:
            # 分割类型和数据
            data_type, data_values = data.split(":")
            values = data_values.split(",")  # 将数据按逗号分隔成列表

            if data_type == "respiration":
                # 将心率数据插入到数据库
                insert_query = "INSERT INTO casualty (respiration) VALUES (%s)"
                cursor.execute(insert_query, (values,))
                respiration_id = get_last_id()
                conn.commit()

            elif data_type == "heart":
                # 将心跳数据插入到与相同respiration ID的行的heart列中
                insert_query = "UPDATE casualty SET heart = %s WHERE id = %s"
                cursor.execute(insert_query, (values, respiration_id))
                conn.commit()

            elif data_type in ["blinks", "pulses", "wounds", "temperature", "latlon"]:
                # 将blinks, pulses, wounds, temperature, latlon数据插入到与相同respiration ID的行的相应列中
                insert_query = "UPDATE casualty SET {column_name} = %s WHERE id = %s"
                column_name = data_type
                cursor.execute(insert_query.format(column_name=column_name), (values, respiration_id))
                conn.commit()

            else:
                print("未知数据类型：{}".format(data_type))

finally:
    # 关闭串口和数据库连接
    ser.close()
    cursor.close()
    conn.close()
