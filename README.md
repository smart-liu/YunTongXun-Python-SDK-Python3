# YunTongXun-Python-SDK-Python3

鉴于第三方平台云通讯的Python-SDK只有Python2.7版本，

同时由于工作版本是Python3，

因此，重写了云通讯的Python-SDK部分代码，满足兼容Python3版本的需求。

从云通讯官网下载Python版本的SDK，解压文件。

## 一、进入SDK文件夹，复制CCPRestSDK.py，进行重写

#### 第一点

将：
```python 
import md5
```

改为：
```python
from hashlib import md5
```

#### 第二点

将：
```python
import urllib2
```

改为：
```python
import urllib.request, urllib.error, urllib.parse
```

#### 第三点

将所有：
```python
md5.new(signature).hexdigest().upper()
```

改为：
```python
md5(signature.encode()).hexdigest().upper()
```

#### 第四点

将所有：
```python
req.add_data(body)
```

改为：
```python
req.data = body.encode()
```

#### 第五点

将所有：
```python
base64.encodestring(src).strip()
```

改为：
```python
base64.encodestring(src.encode()).strip().decode()
```

#### 第六点

将所有：
```python
except Exception, error:
```

改为：
```python
except Exception as error:
```

### Pythoner眼中的语法错误

#### 第七点

去掉";"

注意：由于部分字符串中有";"的存在，请勿一次性全部修改，防止出现新的错误

#### 第八点

背景：Python是一门强类型语言，数据类型之间很少隐形转换

将所有：
```python
if (self.ServerPort <= 0):
```

改为：
```python
if (int(self.ServerPort) <= 0):
```
## 二、进入DENO文件夹，复制SendTemplateSMS.py，进行重写。
内容见文件SendTemplateSMS.py

## 三、进入DENO文件夹，复制xmltojson.py。

## 四、综合，将以上三个文件打包，新建__init__.py，构建一个新的模块

以上，用于工作过程中表现正常

注意：

由于只是用了短信验证，对于语音验证等其他功能没有进行测试，不保证是否正常运行，只是对版本问题和语法问题进行纠正。
 
另外，作为实际工作用途，导包路径问题需要注意。
 
