"""
拍照翻译功能分析 - Streamlit展示应用

这是一个交互式的数据分享平台，用于团队内部展示拍照翻译功能的完整分析结果。
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import sys

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# 页面配置
st.set_page_config(
    page_title="拍照翻译功能分析",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .insight-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2ecc71;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #f39c12;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 主页内容
def main():
    # 标题
    st.markdown('<div class="main-header">📸 拍照翻译功能完整分析</div>', unsafe_allow_html=True)
    
    # 副标题和介绍
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; margin-bottom: 2rem;">
        分析拍照翻译功能在模型优化后的留存表现，判断是否为低频场景，并规划后续功能方向
    </div>
    """, unsafe_allow_html=True)
    
    # 项目概览
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="分析时间跨度",
            value="90天",
            delta="2025.9-10"
        )
    
    with col2:
        st.metric(
            label="渗透率提升",
            value="+0.2%",
            delta="模型优化后"
        )
    
    with col3:
        st.metric(
            label="次日留存率",
            value="13.6%",
            delta="未变化",
            delta_color="off"
        )
    
    with col4:
        st.metric(
            label="分析维度",
            value="6个",
            delta="定量+定性"
        )
    
    # 核心问题
    st.markdown('<div class="sub-header">🎯 核心问题</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>❓ 为什么留存没提升？</h4>
            <p>模型优化+展示优化带来渗透率提升，但次日留存率维持13.6%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>📊 是否低频天花板？</h4>
            <p>需要通过数据判断当前留存水平是否已是低频需求的自然天花板</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>🎯 后续优化方向？</h4>
            <p>调整北极星指标、优化批量体验，还是转向召回策略</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 分析框架
    st.markdown('<div class="sub-header">🔍 分析框架</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📊 定量分析", "🔍 定性分析"])
    
    with tab1:
        st.markdown("""
        ### 定量分析内容
        
        #### 1. 使用频次分布与留存关系 ⏳ 进行中
        - 整体使用频次分布（按使用天数分层）
        - 按分位数（P25、P50、P75）自然分层
        - 批量翻译行为与留存关系
        - 补充指标：再拍一张点击率、统计描述
        
        **负责人**：数据分析师 | **预计完成**：约10-12个工作日
        
        #### 2. 工作日 vs 周末留存分析 📋 待启动
        - 工作日和周末的使用频次差异
        - 工作日和周末的留存率差异
        - 验证学习场景假设
        
        **负责人**：产品团队 | **预计完成**：3天
        """)
    
    with tab2:
        st.markdown("""
        ### 定性分析内容
        
        #### 1. 用户拍摄图片内容分布 🔄 进行中
        - 采样高频用户和低频用户的图片（各200-300张）
        - 使用多模态模型批量打标签
        - 分析内容类型、学科分布、使用场景
        
        **关键维度**：内容类型、文字特征、学科属性、使用场景、特殊标记
        
        #### 2. 用户反馈分析 📋 待启动
        - 近1年用户反馈数据分析
        - 分类：功能缺失、识别问题、体验问题、使用场景
        - 提取高频痛点和需求
        
        #### 3. 竞品拍照翻译功能调研 📋 待启动
        - 主要竞品：Google Translate、有道翻译、百度翻译、作业帮
        - 对比维度：核心功能、延伸功能、留存机制、场景化功能
        - 重点关注：留存钩子设计、场景深挖、用户评论分析
        """)
    
    # 当前进度
    st.markdown('<div class="sub-header">📈 项目进度</div>', unsafe_allow_html=True)
    
    progress_data = {
        '分析模块': [
            '使用频次分布与留存',
            '工作日周末留存分析',
            '图片内容分布分析',
            '用户反馈分析',
            '竞品功能调研',
            '综合分析与建议'
        ],
        '进度': [10, 0, 15, 0, 0, 0],
        '状态': ['⏳ 等待数据分析师', '📋 待启动', '🔄 标签设计中', '📋 待启动', '📋 待启动', '📋 待启动']
    }
    
    progress_df = pd.DataFrame(progress_data)
    
    # 进度条可视化
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=progress_df['分析模块'],
        x=progress_df['进度'],
        orientation='h',
        text=progress_df['状态'],
        textposition='outside',
        marker=dict(
            color=progress_df['进度'],
            colorscale='Blues',
            showscale=False
        )
    ))
    
    fig.update_layout(
        title='各模块完成进度 (%)',
        xaxis_title='完成度',
        yaxis_title='',
        height=400,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 关键洞察（示例）
    st.markdown('<div class="sub-header">💡 已有关键发现</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>✅ 新老用户留存差异显著</h4>
        <p>• 老用户7日留存：<strong>13.6%</strong></p>
        <p>• 新用户7日留存：<strong>7.6%</strong></p>
        <p>• <strong>结论</strong>：新用户留存明显更低，首次体验或新手引导可能存在问题</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
        <h4>⚠️ 渗透提升但留存未变</h4>
        <p>• 渗透率提升：<strong>+0.2%</strong></p>
        <p>• 留存率变化：<strong>持平</strong></p>
        <p>• <strong>待验证</strong>：识别优化带来的渗透提升是否获取了"低质量"用户（一次性用户）</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 下一步行动
    st.markdown('<div class="sub-header">🚀 下一步行动</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 本周任务
        - [ ] 导出90天留存数据
        - [ ] 启动工作日/周末留存分析
        - [ ] 采集图片样本（高频+低频用户）
        - [ ] 完成图片标签体系设计
        """)
    
    with col2:
        st.markdown("""
        ### 下周计划
        - [ ] 接收数据分析结果
        - [ ] 完成图片内容分布分析
        - [ ] 发送用户反馈数据给AI助手
        - [ ] 启动竞品调研
        """)
    
    # 页脚
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #95a5a6; font-size: 0.9rem;">
        📅 项目启动时间：2025年12月19日 | 📍 当前进度：15%
    </div>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()

