class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0  # 当前页面是 history[cur]

    def visit(self, url: str) -> None:
        self.cur += 1
        del self.history[self.cur:]  # 把浏览历史前进的记录全部删除
        self.history.append(url)  # 从当前页跳转访问 url 对应的页面

    def back(self, steps: int) -> str:
        self.cur = max(self.cur - steps, 0)  # 后退 steps 步
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, len(self.history) - 1)  # 前进 steps 步
        return self.history[self.cur]


# 不取巧的最优解
class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    '''
    TODO
    build up BrowserHistory

    HACK
    doubly LinkedList

    head <-> URL1 <-> URL2 ..
    url_node = {url: URL1, ...}
    '''
    def __init__(self, homepage: str):
        self.curr = homepage
        self.pages = Node(homepage)
        self.url_node = {self.curr: self.pages}

    '''
    TC: O(1)
    '''
    def visit(self, url: str) -> None:
        # clear forward pages
        cur_page = self.url_node[self.curr]
        if cur_page.next:
            cur_page.next.prev = None
            cur_page.next = None

        # add url
        node = Node(url)
        cur_page.next = node
        node.prev = cur_page
        self.url_node[url] = node
        self.curr = url

    '''
    TC: O(min(steps, m)), where m is backward visits
    '''
    def back(self, steps: int) -> str:
        cur_page = self.url_node[self.curr]
        while steps > 0 and cur_page.prev:
            cur_page = cur_page.prev
            steps -= 1
        self.curr = cur_page.url
        return self.curr

    '''
    TC: O(min(steps, n)), where n is forward visits
    '''
    def forward(self, steps: int) -> str:
        cur_page = self.url_node[self.curr]
        while steps > 0 and cur_page.next:
            cur_page = cur_page.next
            steps -= 1
        self.curr = cur_page.url
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
