"""
使用频次与留存分析页面
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# 页面配置
st.set_page_config(
    page_title="使用频次与留存分析",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 读取数据
@st.cache_data
def load_data():
    # 使用绝对路径
    data_path = "/Users/pupu/Desktop/Claude/拍照翻译功能分析/1_定量分析/1.1_使用频次分布与留存/new拍照翻译)使用次数摸排.csv"
    df = pd.read_csv(data_path, encoding='utf-8-sig')
    return df

try:
    df = load_data()
    
    # ===== 1. 关键数据概览和表格 =====
    # 提取关键数据行
    key_rows_all = df[df['app活跃天数分层'] == '合计'].iloc[:8].copy()
    
    # 调整顺序：按天数排序，合计放最后
    order_map = {
        '合计': 0,
        '使用1天': 1,
        '使用2天': 2,
        '使用3天': 3,
        '使用4-5天': 4,
        '使用6-10天': 5,
        '使用10天以上': 6
    }
    key_rows_all['sort_order'] = key_rows_all['翻译使用天数分层'].map(order_map)
    key_rows_sorted = key_rows_all.sort_values('sort_order')
    
    # 将使用1天的次留和七留改为0
    key_rows_sorted.loc[key_rows_sorted['翻译使用天数分层'] == '使用1天', '平均功能次留率'] = '0%'
    key_rows_sorted.loc[key_rows_sorted['翻译使用天数分层'] == '使用1天', '平均功能七留率'] = '0%'
    
    # 准备显示的数据
    display_data = key_rows_sorted[['翻译使用天数分层', '翻译uv', '占比', '平均功能次留率', 
                                     '平均功能七留率', '平均使用间隔(天)(剔除1次的)', '日人均翻译张数']].copy()
    
    # 重命名列
    display_data.rename(columns={'平均使用间隔(天)(剔除1次的)': '平均使用间隔(天)'}, inplace=True)
    
    # 将合计行移到最后
    summary_row = display_data[display_data['翻译使用天数分层'] == '合计']
    other_rows = display_data[display_data['翻译使用天数分层'] != '合计']
    display_data = pd.concat([other_rows, summary_row])
    
    # 显示表格，使用HTML实现居中
    st.markdown("##### 📋 拍照翻译功能使用数据")
    
    # 添加统计说明
    st.markdown("""
    <div style="color: #666; font-size: 0.85rem; line-height: 1.6; margin: 12px 0 20px 0;">
        <strong>统计范围</strong><br>
        时间：2025年10月1日至11月30日<br>
        用户范围：在此期间使用过拍照翻译功能的所有用户<br>
        异常值处理：去除单日使用超过50次的用户、去除单次会话翻译超过30张的用户<br><br>
        <strong>口径定义</strong><br>
        使用次数：用户在10月1日至11月30日使用拍照翻译功能的天数（去重计算）。<br>
        日均翻译张数：用户平均每天翻译的图片数量。
    </div>
    """, unsafe_allow_html=True)
    
    # 使用HTML表格实现居中对齐和固定列宽
    col_widths = ['14%', '12%', '10%', '12%', '12%', '15%', '13%']
    html_table = '<table style="width:100%; border-collapse: collapse; text-align: center; table-layout: fixed;">'
    html_table += '<thead><tr style="background-color: #f0f2f6;">'
    for i, col in enumerate(display_data.columns):
        html_table += f'<th style="padding: 12px; border: 1px solid #ddd; width: {col_widths[i]};">{col}</th>'
    html_table += '</tr></thead><tbody>'
    
    for idx, row in display_data.iterrows():
        if row['翻译使用天数分层'] == '合计':
            html_table += '<tr style="background-color: #e8f4f8; font-weight: 600;">'
        else:
            html_table += '<tr>'
        for col in display_data.columns:
            html_table += f'<td style="padding: 10px; border: 1px solid #ddd;">{row[col]}</td>'
        html_table += '</tr>'
    
    html_table += '</tbody></table>'
    st.markdown(html_table, unsafe_allow_html=True)
    
    # ===== 2. 核心发现（左侧文字+右侧图表）=====
    st.markdown("")
    st.markdown("#### 核心发现")
    
    # 发现1: 使用天数分层 + 饼图
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
    col_text1, col_chart1 = st.columns([1.2, 1.8])
    
    with col_text1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                    padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                <span style="font-size: 1.8rem; margin-right: 12px;">📊</span>
                <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">使用天数分层</h4>
            </div>
            <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    <strong style="color: #2c3e50;">60%</strong> 一次性用户：翻译是偶发需求
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    <strong style="color: #2c3e50;">35%</strong> 中频用户 (使用2-10天)
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    <strong style="color: #2c3e50;">仅2%</strong> 超高频用户 (10天+)
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_chart1:
        # 准备数据
        usage_data = df[df['app活跃天数分层'] == '合计'].iloc[1:8].copy()
        usage_data = usage_data[usage_data['翻译使用天数分层'] != '合计']
        
        # 创建饼图
        fig1 = go.Figure(data=[go.Pie(
            labels=usage_data['翻译使用天数分层'],
            values=usage_data['翻译uv'],
            hole=0.4,
            marker=dict(colors=['#95a5a6', '#7f8c8d', '#b8c5d6', '#9db4c8', '#7fa5a4', '#6c9a8b']),
            textinfo='label+percent',
            textposition='outside',
            textfont=dict(size=11)
        )])
        
        fig1.update_layout(
            height=350,
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            annotations=[dict(
                text='60%<br>一次性用户',
                x=0.5, y=0.5,
                font_size=14,
                showarrow=False
            )]
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    # 发现2: 平均使用间隔 + 柱状图
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
    col_text2, col_chart2 = st.columns([1.2, 1.8])
    
    with col_text2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #e8f5e9 0%, #a5d6a7 100%); 
                    padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                <span style="font-size: 1.8rem; margin-right: 12px;">⏱️</span>
                <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">平均使用间隔</h4>
            </div>
            <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    整体平均：<strong style="color: #2c3e50;">7.11天</strong> (周频需求)
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    高频用户：<strong style="color: #2c3e50;">3.37天</strong> (每3天用1次)
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    中低频用户：<strong style="color: #2c3e50;">7-8天</strong> (每周用1次)
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_chart2:
        # 准备数据
        x_labels = ['使用2天', '使用3天', '使用4-5天', '使用6-10天', '使用10天+']
        y_interval = [7.71, 8.01, 7.17, 5.47, 3.37]
        
        fig2 = go.Figure()
        
        fig2.add_trace(go.Bar(
            x=x_labels,
            y=y_interval,
            marker=dict(color='#7fa5a4'),
            text=[f'{v}天' for v in y_interval],
            textposition='outside'
        ))
        
        fig2.add_hline(
            y=7.11,
            line_dash="dash",
            line_color="#95a5a6",
            line_width=2,
            annotation_text="整体平均 7.11天",
            annotation_position="top right",
            annotation=dict(
                font_size=12,
                font_color="#95a5a6"
            )
        )
        
        fig2.update_layout(
            height=350,
            showlegend=False,
            margin=dict(t=30, b=20, l=20, r=80),
            xaxis_title='',
            yaxis_title='使用间隔(天)',
            yaxis=dict(range=[0, 10])
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # 发现3: 次留率与七留率 + 对比图
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
    col_text3, col_chart3 = st.columns([1.2, 1.8])
    
    with col_text3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffcc80 100%); 
                    padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                <span style="font-size: 1.8rem; margin-right: 12px;">📈</span>
                <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">次留率与七留率基本一致</h4>
            </div>
            <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    功能次留率：<strong style="color: #2c3e50;">11.46%</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    功能七留率：<strong style="color: #2c3e50;">11.58%</strong> (几乎持平)
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    理论次留率：<strong style="color: #2c3e50;">≈14%</strong> (1/7天)
                </div>
            </div>
            <div style="margin-top: 20px; padding: 14px; background: rgba(255,255,255,0.7); 
                        border-radius: 8px; border-left: 4px solid #d4a574;">
                <strong style="color: #2c3e50; font-size: 0.88rem;">💡 结论：</strong>
                <span style="color: #34495e; font-size: 0.88rem;">用户不是"第2天不用就流失"，而是"7天内某天会回来"</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_chart3:
        # 准备数据
        x_labels_retention = ['使用2天', '使用3天', '使用4-5天', '使用6-10天', '使用10天+']
        y_next = [5.10, 8.02, 11.32, 17.77, 34.18]
        y_7day = [3.81, 6.96, 11.04, 18.52, 35.81]
        
        fig3 = go.Figure()
        
        fig3.add_trace(go.Bar(
            name='次留率',
            x=x_labels_retention,
            y=y_next,
            marker=dict(color='#7fa5a4'),
            text=[f'{v}%' for v in y_next],
            textposition='outside'
        ))
        
        fig3.add_trace(go.Bar(
            name='七留率',
            x=x_labels_retention,
            y=y_7day,
            marker=dict(color='#b8c5d6'),
            text=[f'{v}%' for v in y_7day],
            textposition='outside'
        ))
        
        fig3.update_layout(
            height=350,
            barmode='group',
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis_title='',
            yaxis_title='留存率 (%)',
            legend=dict(x=0.02, y=0.98),
            yaxis=dict(range=[0, 40])
        )
        
        st.plotly_chart(fig3, use_container_width=True)
    
    # 发现4: 日均翻译张数 + 折线图
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
    col_text4, col_chart4 = st.columns([1.2, 1.8])
    
    with col_text4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f3e5f5 0%, #ce93d8 100%); 
                    padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                <span style="font-size: 1.8rem; margin-right: 12px;">📸</span>
                <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">日均翻译张数</h4>
            </div>
            <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    一次性用户：<strong style="color: #2c3e50;">2.32张</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    高频用户：<strong style="color: #2c3e50;">3.38张</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    全部区间：<strong style="color: #2c3e50;">2-3.4张</strong>
                </div>
            </div>
            <div style="margin-top: 20px; padding: 14px; background: rgba(255,255,255,0.7); 
                        border-radius: 8px; border-left: 4px solid #9b8fb9;">
                <strong style="color: #2c3e50; font-size: 0.88rem;">💡 结论：</strong>
                <span style="color: #34495e; font-size: 0.88rem;">"连续拍摄2-3张"的场景，应优化连续体验</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_chart4:
        # 准备数据
        x_labels_photos = ['使用1天', '使用2天', '使用3天', '使用4-5天', '使用6-10天', '使用10天+']
        y_photos = [2.32, 2.67, 2.83, 2.92, 3.02, 3.38]
        
        fig4 = go.Figure()
        
        fig4.add_trace(go.Scatter(
            x=x_labels_photos,
            y=y_photos,
            mode='lines+markers',
            marker=dict(color='#6c9a8b', size=10),
            line=dict(color='#6c9a8b', width=3),
            fill='tozeroy',
            fillcolor='rgba(108, 154, 139, 0.15)'
        ))
        
        fig4.update_layout(
            height=350,
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis_title='',
            yaxis_title='日均翻译张数',
            yaxis=dict(range=[0, 4])
        )
        
        st.plotly_chart(fig4, use_container_width=True)

except Exception as e:
    st.error(f"数据加载失败: {str(e)}")
    st.info("请确保数据文件路径正确")
