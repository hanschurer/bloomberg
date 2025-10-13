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
