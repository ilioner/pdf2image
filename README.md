# pdf2image

### 环境配置：

#### 1. 安装ImageMagick
ImageMagick是一个免费编辑创建合成图片的软件，大多数功能都来自命令行工具，具体可以参照[http://www.imagemagick.org/script/index.php](http://www.imagemagick.org/script/index.php)
	
	brew install imagemagick

> ###### 注意，使用brew安装都是7.x版本，使用wand时会出错，需要安装6.x版本。

> ##### 解决办法：
> ###### 1.安装6.x版本
> 	
> 		brew install imagemagick@6
> 
> ###### 2.取消链接7.x版本
> 
> 		brew unlink imagemagick

> ######  * Unlinking /usr/local/Cellar/imagemagick/7.0.7-4… 71 symlinks removed
> ###### 3.强制链接6.x版本
> 
> 		 brew link imagemagick@6 --force

> ######  * Linking /usr/local/Cellar/> imagemagick@6/6.9.9-15… 75 symlinks created
> ###### 4.export环境变量
>  
> 		echo 'export PATH="/usr/local/opt/imagemagick@6/bin:$PATH"' 
>  
> 		~/.bash_profile
> 
> ok，以上解决imagemagick版本问题。


#### 2. 安装gs

必须安装gs，否则pdf无法转换。
 
 	brew install gs
 	
#### 3. 安装wand(按照自己的python版本来安装)
wand：是Imagemagick的Python接口

	pip3 install wand


### 安装文档参考

http://blog.csdn.net/wwj_748/article/details/78135879?utm_source=tuicool&utm_medium=referral


