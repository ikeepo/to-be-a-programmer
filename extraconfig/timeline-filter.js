function filterArticles(days, event) {
  // 1. 切换按钮激活状态
  const buttons = document.querySelectorAll(".filter-btn");
  buttons.forEach((btn) => btn.classList.remove("active"));
  if (event && event.currentTarget) {
    event.currentTarget.classList.add("active");
  }

  const items = document.querySelectorAll(".timeline-item");

  // 如果选择“全部”，直接展示所有行
  if (days === "all") {
    items.forEach((item) => (item.style.display = "block"));
    return;
  }

  // 2. 计算截止日期（当前时间减去 X 天）
  const now = new Date();
  const targetDate = new Date(now.getTime() - days * 24 * 60 * 60 * 1000);
  targetDate.setHours(0, 0, 0, 0); // 抹平当天的小时误差

  // 3. 执行动态隐藏/显示
  items.forEach((item) => {
    const itemDateStr = item.getAttribute("data-date");
    if (!itemDateStr) return;

    const itemDate = new Date(itemDateStr);

    if (itemDate >= targetDate) {
      item.style.display = "block"; // 符合条件的显示
    } else {
      item.style.display = "none"; // 不符合条件的隐藏
    }
  });
}
