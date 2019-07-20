花了5个小时才把geopandas安装好，有必要记录下。

最终安装成功还是要感谢Geoff Boeing教授的这篇教程，教授给出了非常详细的操作步骤。

总结一下要点：

1. geopandas依赖于gdal, fiona, pyproj, shapely，需要依次安装依赖库。最重要的是在install gdal之后，要把gdal的环境变量添加到系统里！这也是我在找到教授的教程前，装了几个小时一直失败的原因。
2. Fiona对依赖的gdal包有特定限制。直接在已有的Python环境中用pip或者conda install gdal并不可行，需要指定版本号。而且，用conda安装Fiona以及geopandas时候，会出现兼容性报错。建议使用轮子安装的方式。轮子下载地址。 网站里已经说明了Fiona对gdal有版本号的要求。比如我下载的是Fiona-1.8.6-cp37-cp37m-win_amd64.whl，就需要使用2.4版本的gdal：GDAL-2.4.1-cp37-cp37m-win_amd64.whl。起初我用了最新版本3.0的gdal，发现安装Fiona后，出现import error。