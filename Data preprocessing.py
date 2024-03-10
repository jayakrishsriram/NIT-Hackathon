import xml.etree.ElementTree as ET
import os
def convert_xml_to_yolo(xml_file, txt_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    classes = []
    xmin = []
    ymin = []
    xmax = []
    ymax = []
    confidences = []
    for obj in root.iter('object'):
        class_name = obj.find('name').text
        classes.append(class_name)
        bbox = obj.find('bndbox')
        xmin.append(int(bbox.find('xmin').text))
        ymin.append(int(bbox.find('ymin').text))
        xmax.append(int(bbox.find('xmax').text))
        ymax.append(int(bbox.find('ymax').text))
        confidence = obj.find('confidence')
        if confidence is not None:
            confidences.append(float(confidence.text))
        else:
            confidences.append(1.0)

    # Format the extracted information as per YOLO's text file format
    with open(txt_file, 'w') as f:
        for i in range(len(classes)):
            cx = (xmin[i] + xmax[i]) / 2
            cy = (ymin[i] + ymax[i]) / 2
            w = xmax[i] - xmin[i]
            h = ymax[i] - ymin[i]
            f.write(f"0 {cx/image_width} {cy/image_height} {w/image_width} {h/image_height} {confidences[i]}\n")

if __name__ == "__main__":
    
    path = 'C:\\Users\\jayak\\Downloads\\hackathon\\RDD2022_India\\India\\train\\xmls'
    for filename in os.listdir(path):  
        if not filename.endswith('.xml'): continue
        xml_file = os.path.join("C:\\Users\\jayak\\Downloads\\hackathon\\RDD2022_India\\India\\train\\xmls\\", filename)
        txt_file = os.path.join("C:\\Users\\jayak\\Downloads\\hackathon\\RDD2022_India\\India\\train\\otxt\\", os.path.splitext(xml_file)[0] + '.txt')
        root = ET.parse(xml_file).getroot()
        image_width = int(root.find('size').find('width').text)
        image_height = int(root.find('size').find('height').text)
        convert_xml_to_yolo(xml_file, txt_file)