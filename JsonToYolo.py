import os
import json

def convert_to_yolo_label(json_data, output_path):
    # 解析 JSON 数据
    shapes = json_data["shapes"]
    image_path = json_data["imagePath"]
    image_height = json_data["imageHeight"]
    image_width = json_data["imageWidth"]

    # 处理每个形状
    yolo_labels = []
    for shape in shapes:
        label = shape["label"]
        points = shape["points"]
        shape_type = shape["shape_type"]

        # 将坐标从图像坐标系转换为 YOLO 标签坐标系
        x_center = (points[0][0] + points[1][0]) / (2 * image_width)
        y_center = (points[0][1] + points[1][1]) / (2 * image_height)
        width = abs(points[0][0] - points[1][0]) / image_width
        height = abs(points[0][1] - points[1][1]) / image_height

        # 构建 YOLO 标签字符串
        yolo_label = f"{label} {x_center} {y_center} {width} {height}"
        yolo_labels.append(yolo_label)

    return yolo_labels

def process_folder(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 处理文件夹中的每个 JSON 文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            # 读取 JSON 文件
            with open(os.path.join(input_folder, filename), 'r') as json_file:
                json_data = json.load(json_file)

            # 构建输出文件路径
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')

            # 调用函数进行转换并写入文件
            yolo_labels = convert_to_yolo_label(json_data, output_path)
            with open(output_path, 'w') as output_file:
                for label in yolo_labels:
                    output_file.write(label + '\n')

if __name__ == "__main__":
    # 指定输入和输出文件夹路径
    input_folder = 'datasets/3C-Circle-2024-01-31/2023_09_10_16_label_json'
    output_folder = 'datasets/3C-Circle-2024-01-31/labels'

    # 调用函数处理文件夹中的 JSON 文件
    process_folder(input_folder, output_folder)
