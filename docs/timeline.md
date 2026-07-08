# 📅 文章时间线

<div class="filter-buttons" style="margin-bottom: 20px;">
  <button onclick="filterArticles('all')" class="filter-btn active">全部文章</button>
  <button onclick="filterArticles(7)" class="filter-btn">过去 7 天</button>
  <button onclick="filterArticles(30)" class="filter-btn">过去 30 天</button>
</div>

{{ generate_timeline() }}
<style>
  /* 简单的按钮样式 */
  .filter-btn {
    padding: 6px 12px;
    margin-right: 5px;
    border: 1px solid #ccc;
    background: #fff;
    cursor: pointer;
    border-radius: 4px;
  }
  .filter-btn.active {
    background: #007bff;
    color: #fff;
    border-color: #007bff;
  }
</style>
