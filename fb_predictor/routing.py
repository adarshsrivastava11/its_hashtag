from channels.routing import route
channel_routing = [
            route("crawl", "crawler.consumers.crawl"),
            ]
