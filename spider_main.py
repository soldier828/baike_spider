from baike_spider import html_download
from baike_spider import html_parser
from baike_spider import output_html
from baike_spider import url_manager
import time

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = output_html.OuputHtml()

    def craw(self, root_rul):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            #time.sleep(3)
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print "craw falied"
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)