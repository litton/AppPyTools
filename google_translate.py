from googletrans import Translator
import xml.dom.minidom
import xml.sax
#https://github.com/ssut/py-googletrans
class GoogleTranslate:   

    list = {} 
    dicts ={}
    def __init__(self):
         self.translator = Translator()
         self.language = ""

    def generate_target_file(self):
        filename = self.language + '_values.xml'
        with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write("<resources>\n")
            for key in self.dicts.keys():
                value = self.dicts[key]
                value = value.replace('% s','%s')
                value = value.replace('% S','%s')
                value = value.replace('% d','%d')
                value = value.replace('\ n','\n')
                line = "<string name=\"" + key +  "\">" + value + "</string>\n"
                print(line)
                f.write(line)
            f.write("</resources>\n")

    def start(self,language):
        self.language = language
        for key in self.list.keys():
            value = self.list[key]
            if value:
                a = self.translator.translate(value,dest=language)
                self.dicts[key] = a.text
        
        self.generate_target_file()


    def read_file(self,path):
       # 创建一个 XMLReader
        parser = xml.sax.make_parser()
        # 关闭命名空间
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        # 重写 ContextHandler
        Handler = StringXmlHandler(self.list)
        parser.setContentHandler(Handler)
        parser.parse(path)
       
    
        


class StringXmlHandler(xml.sax.ContentHandler):
    def __init__(self,list):
        self.CurrentData = ""
        self.name=""
        self.key=""
        self.value=""
        self.list = list
    
    def startElement(self,tag,attributes):
        self.CurrentData = tag
        if tag == 'string':
            value = attributes["name"]
            self.key = value
            #print(value)

     # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "string":
             print (self.key + "<-->" +  self.value)
             self.list[self.key] = self.value

    def characters(self,content):
        if self.CurrentData == "string":
            self.value = content

       







    
