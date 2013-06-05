rquire 'open-uri'

class Spider
    attr_accessor :todo, :visited, :error

    def initialize
        @todo = {}
        @visited = {}
        @error = {}
    end    

    def crawl target_url='http://www.360buy.com/'
        begin
            open(target_url).read.scan(/href=["|'](.+?)["|']/){|url|
                url = url[0]
                url = target_url.match(/(http:\/\/([^\/]+))\//)[1] << url if url =~ /^\//
                    @todo[url.split('#')[0]] = nil if url =~ /www\.360buy\.com/ && !(url =~ /[\.png|\.js|\.css|\.jpg|\.jpeg|\.bmp]$/) && (!@visited.has_key?(url))
            }
            puts target_url if !@visited.has_key?(target_url)
            @visited[target_url] = nil
        rescue
            puts "error url is: #{target_url}"
            @error[target_url] = nil
        ensure
        end
        crawl @todo.shift[0] if @todo.size > 0
    end
end

spider = Spider.new
puts "start crawling.."
spider.crawl
puts "mission compelted... whole website url size is: #{spider.visited.size}, error page size is: #{spider.error.size}" 
