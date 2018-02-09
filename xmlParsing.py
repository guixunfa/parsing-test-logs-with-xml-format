import sys
import glob
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as nu
def traversalDir_XMLFile(path):
    #判断路径是否存在  
    if (os.path.exists(path)):
    #得到该文件夹路径下下的所有xml文件路径  
        f = glob.glob(path + '\\*.txt')
        airLeakVal = []
        airLeakMax = []
        #airLeakMin = []
        for file in f:
            print(file)
            #打开xml文档  
            #dom = xml.dom.minidom.parse(file)
            tree = ET.parse(file)
            root = tree.getroot()
            print("root content- ", root.tag, ":", root.attrib)

            for children2 in root:
                print("children2 content= ", children2.tag, ":", children2.attrib)
                for children3 in children2:
                    print("child3 content= ",children3.tag, ":", children3.attrib)
                    for children4 in children3:
                        print("child4 content= ", children4.tag, ":", children4.text)
                        if "Val" in children4.tag:
                            airLeakVal.append(children4.text)
                        #elif "Max" in children4.tag:
                            #if len(airLeakMax) <= 100:
                                #airLeakMax.append(children4.text)
                        #elif "Min" in children4.tag:
                            #airLeakMin.append(float(children4.text))
        plt.xticks(rotation=90)
        plt.hist(airLeakVal,bins=25,facecolor='blue',edgecolor='black')
        #plt.hist(airLeakMax,color='red')
        plt.title("the distribution of airLeak data")
        #plt.hist(airLeakMin)
        plt.show()

traversalDir_XMLFile(r"C:\Users\ryan.gui\\Desktop\goo\Python\Airleak test log\arileak test log")