import re
import time
import json
import sqlite3
import requests


class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers={'User-Agent':user_agent}
        r = requests.get(url,headers=headers)
        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None



class HtmlParser(object):

    def parser_url(self,response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls!=None :
            # 将urls进行去重
            return list(set(urls))
        else:
            return None




    def parser_json(self,page_url,response):
        '''
        解析响应
        :param response:
        :return:
        '''
        #将=和；之间的内容提取出来
        # print page_url
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result!=None :
            value=json.loads(result)


            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print (e)
                return None
            if isRelease:
                if value.get('value').get('hotValue')==None:
                    return self._parser_release(page_url,value)
                else:
                    return self._parser_no_release(page_url,value,isRelease=2)
            else:
                return self._parser_no_release(page_url,value)



    def _parser_release(self,page_url,value):
        '''
        解析已经上映的影片
        var result_201611132231493282 = { "value":{"isRelease":true,"movieRating":{"MovieId":108737,"RatingFinal"
        :7.7,"RDirectorFinal":7.7,"ROtherFinal":7,"RPictureFinal":8.4,"RShowFinal":10,"RStoryFinal":7.3,"RTotalFinal"
        :10,"Usercount":4067,"AttitudeCount":4300,"UserId":0,"EnterTime":0,"JustTotal":0,"RatingCount":0,"TitleCn"
        :"","TitleEn":"","Year":"","IP":0},"movieTitle":"奇异博士","tweetId":0,"userLastComment":"","userLastCommentUrl"
        :"","releaseType":1,"boxOffice":{"Rank":1,"TotalBoxOffice":"5.66","TotalBoxOfficeUnit":"亿","TodayBoxOffice"
        :"4776.8","TodayBoxOfficeUnit":"万","ShowDays":10,"EndDate":"2016-11-13 22:00","FirstDayBoxOffice":"8146
        .21","FirstDayBoxOfficeUnit":"万"}},"error":null};var movieOverviewRatingResult=result_201611132231493282
        :param page_url:电影链接
        :param value:json数据
        :return:
        '''
        try:
            isRelease = 1
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')
            MovieId =  movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount =  movieRating.get('AttitudeCount')


            if value.get('value').get('boxOffice')== None:

                return(MovieId, movieTitle, RatingFinal,
                      ROtherFinal, RPictureFinal, RDirectorFinal,
                      RStoryFinal, Usercount, AttitudeCount,
                      u'无',u'无',u'无',u'无', isRelease)
            else:
                boxOffice = value.get('value').get('boxOffice')
                TotalBoxOffice = boxOffice.get('TotalBoxOffice')
                TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
                TodayBoxOffice = boxOffice.get('TodayBoxOffice')
                TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')
                ShowDays = boxOffice.get('ShowDays')
                try:
                    Rank = boxOffice.get('Rank')
                except Exception as e:
                    Rank = 0
            # 将提取其中的内容进行返回
                return (MovieId, movieTitle, RatingFinal,
                    ROtherFinal, RPictureFinal, RDirectorFinal,
                    RStoryFinal, Usercount, AttitudeCount,
                    TotalBoxOffice + TotalBoxOfficeUnit,
                    TodayBoxOffice + TodayBoxOfficeUnit,
                    Rank, ShowDays, isRelease)
        except Exception as e:
            print (e,page_url,value)
            return None

    def _parser_no_release(self,page_url,value,isRelease = 0):
        '''
        var result_201611141343063282 = { "value":{"isRelease":false,"movieRating":
        {"MovieId":236608,"RatingFinal":-1,"RDirectorFinal":0,"ROtherFinal":0,
        "RPictureFinal":0,"RShowFinal":0,"RStoryFinal":0,"RTotalFinal":0,
        "Usercount":5,"AttitudeCount":19,"UserId":0,"EnterTime":0,
        "JustTotal":0,"RatingCount":0,"TitleCn":"","TitleEn":"","Year":"",
        "IP":0},"movieTitle":"江南灵异录之白云桥","tweetId":0,
        "userLastComment":"","userLastCommentUrl":"","releaseType":2,
        "hotValue":{"MovieId":236608,"Ranking":53,"Changing":4,
        "YesterdayRanking":57}},"error":null};
        var movieOverviewRatingResult=result_201611141343063282;
        :param page_url:
        :param value:
        :return:
        '''
        try:
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId =  movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount =  movieRating.get('AttitudeCount')
            try:
                Rank = value.get('value').get('hotValue').get('Ranking')
            except Exception as e:
                Rank = 0
            return (MovieId, movieTitle, RatingFinal,
                    ROtherFinal, RPictureFinal, RDirectorFinal,
                    RStoryFinal, Usercount, AttitudeCount, u'无',
                    u'无', Rank, 0, isRelease)
        except Exception as e:
            print (e,page_url,value)
            return None







class DataOutput(object):
    def __init__(self):
        self.cx = sqlite3.connect("movie.db")
        self.create_table('movie')
        self.datas=[]

    def create_table(self,table_name):
        '''
        创建数据表
        :param table_name:表名称
        :return:
        '''
        values = '''
        id integer primary key,
        MovieId integer,
        MovieTitle varchar(40) NOT NULL,
        RatingFinal REAL NOT NULL DEFAULT 0.0,
        ROtherFinal REAL NOT NULL DEFAULT 0.0,
        RPictureFinal REAL NOT NULL DEFAULT 0.0,
        RDirectorFinal REAL NOT NULL DEFAULT 0.0,
        RStoryFinal REAL NOT NULL DEFAULT 0.0,
        Usercount integer NOT NULL DEFAULT 0,
        AttitudeCount integer NOT NULL DEFAULT 0,
        TotalBoxOffice varchar(20) NOT NULL,
        TodayBoxOffice varchar(20) NOT NULL,
        Rank integer NOT NULL DEFAULT 0,
        ShowDays integer NOT NULL DEFAULT 0,
        isRelease integer NOT NULL
        '''
        self.cx.execute('CREATE TABLE IF NOT EXISTS  %s( %s ) '%(table_name,values))


    def store_data(self,data):
        '''
        数据存储
        :param data:
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_db('movie')

    def output_db(self,table_name):
        '''
        将数据存储到sqlite
        :return:
        '''
        for data in self.datas:
            self.cx.execute("INSERT INTO %s (MovieId,MovieTitle,"
                            "RatingFinal,ROtherFinal,RPictureFinal,"
                            "RDirectorFinal,RStoryFinal, Usercount,"
                            "AttitudeCount,TotalBoxOffice,TodayBoxOffice,"
                            "Rank,ShowDays,isRelease) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) "
                            "" % table_name, data)
            self.datas.remove(data)
        self.cx.commit()

    def output_end(self):
        '''
        关闭数据库
        :return:
        '''
        if len(self.datas)>0:
            self.output_db('movie')
        self.cx.close()

class SpiderMan(object):

    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self,root_url):
        content = self.downloader.download(root_url)
        urls = self.parser.parser_url(content)
        #构造一个获取评分和票房链接，类似
        #http://service.library.mtime.com/Movie.api?
        # Ajax_CallBack=true
        # &Ajax_CallBackType=Mtime.Library.Services
        # &Ajax_CallBackMethod=GetMovieOverviewRating
        # &Ajax_CrossDomain=1
        # &Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F108737%2F
        # &t=2016 11 13 22 31 49 3282
        # &Ajax_CallBackArgument0=108737
        for url in urls:
            try:
                t = time.strftime("%Y%m%d%H%Motion%S3282", time.localtime())
                rank_url ='http://service.library.mtime.com/Movie.api' \
                          '?Ajax_CallBack=true' \
                          '&Ajax_CallBackType=Mtime.Library.Services' \
                          '&Ajax_CallBackMethod=GetMovieOverviewRating' \
                          '&Ajax_CrossDomain=1' \
                          '&Ajax_RequestUrl=%s' \
                          '&t=%s' \
                          '&Ajax_CallBackArgument0=%s'%(url[0],t,url[1])
                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url,rank_content)
                self.output.store_data(data)
            except Exception as e:
                 print ("Crawl failed")
        self.output.output_end()
        print ("Crawl finish")

if __name__=='__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Beijing/')
