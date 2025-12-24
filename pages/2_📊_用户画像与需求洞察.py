import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# 页面配置
st.set_page_config(
    page_title="用户画像与需求洞察",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 数据加载函数
@st.cache_data
def load_image_labels():
    """加载图片标签数据"""
    weekday_path = "/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/打标结果/工作日标签.csv"
    weekend_path = "/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/打标结果/周末标签.csv"
    
    df_weekday = pd.read_csv(weekday_path)
    df_weekend = pd.read_csv(weekend_path)
    
    df_weekday['time_period'] = 'weekday'
    df_weekend['time_period'] = 'weekend'
    
    return df_weekday, df_weekend

@st.cache_data
def load_feedback_data():
    """加载用户反馈数据"""
    feedback_path = "/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.2_用户反馈分析/清洗结果/用户反馈数据_已打标_8000条_20并发.csv"
    df = pd.read_csv(feedback_path)
    return df

# 加载数据
try:
    df_weekday, df_weekend = load_image_labels()
    df_feedback = load_feedback_data()
    
    # ===== 第一部分：用户画像与使用场景 =====
    st.markdown("#### 用户画像与使用场景")
    
    # 1.1 数据来源说明（简化为一行）
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    total_samples = len(df_weekday) + len(df_weekend)
    st.info(f"📊 **数据来源**：分析了 **{total_samples}张** 用户拍照图片（工作日 {len(df_weekday)}张 + 周末 {len(df_weekend)}张），通过AI模型对图片进行 **3个维度** 的标注：**年级水平、内容类型、材料来源**")
    
    # 1.2 标注标准说明（可展开收起）
    with st.expander("📋 查看标注标准定义（团队对齐）", expanded=False):
        st.markdown("""
        ### 标注维度说明
        
        本次分析采用3个核心维度对用户拍照图片进行标注：**年级水平、内容类型、材料来源**
        
        ---
        
        #### 1️⃣ 年级水平（Grade Level）
        
        | 标签代码 | 含义 | 判断标准 |
        |---------|------|---------|
        | `grade_1_3` | 小学低年级（1-3年级） | 词汇简单、句子短、有图画辅助 |
        | `grade_4_6` | 小学高年级（4-6年级） | 基础词汇、简单语法、短段落 |
        | `grade_7_9` | 初中（7-9年级） | 中等难度、完整文章、语法练习 |
        | `grade_10_12` | 高中（10-12年级） | 复杂词汇、长文章、高级语法 |
        
        ---
        
        #### 2️⃣ 内容类型（Content Type）
        
        | 标签代码 | 中文名称 | 判断标准 | 数量 |
        |---------|---------|---------|------|
        | `reading_comprehension` | 阅读理解 | 有文章+问题+选项（**完整练习题**） | 124条 |
        | `reading_passage` | 阅读文章 | 只有文章，**没有配套问题**（用于预习/阅读） | 48条 |
        | `grammar_exercise` | 语法练习 | 填空题、改错题、语法选择题 | 42条 |
        | `vocabulary_exercise` | 词汇练习 | 单词填空、单词选择、词义匹配 | 41条 |
        | `dialogue_text` | 对话文本 | A: B: 形式的对话 | 31条 |
        | `cloze_test` | 完形填空 | 文章中有多处空格需填写 | 37条 |
        | `writing_assignment` | 写作作业 | 作文题目、写作范文 | 19条 |
        | `translation_exercise` | 翻译练习 | 中译英或英译中 | 14条 |
        | `exam_paper` | 试卷 | 完整试卷，有多种题型 | 6条 |
        
        **重点说明**：
        - ⚠️ **阅读理解 ≠ 阅读文章**
          - 阅读理解：练习题，有问题要做
          - 阅读文章：纯文本，用于阅读
        
        ---
        
        #### 3️⃣ 材料来源（Material Source）
        
        | 标签代码 | 中文名称 | 判断标准 | 数量 |
        |---------|---------|---------|------|
        | `workbook / homework_book` | 练习/作业材料 | 练习册或作业本（印刷/手写均包含） | 217条 |
        | `official_textbook` | 正式教材 | 有教材标识，排版正规 | 80条 |
        | `exam_paper` | 试卷 | 考试卷，有考试标题 | 33条 |
        | `screen_capture` | 屏幕截图 | 手机/电脑屏幕截图 | 31条 |
        | `handout` | 讲义 | 老师印发的资料 | 20条 |
        | `supplementary_book` | 课外读物 | 课外辅导书 | 12条 |
        | `other` | 其他 | 其他类型材料 | 10条 |
        
        **说明**：
        - ✅ 练习册和作业本视觉区别不明显，已合并为"练习/作业材料"
        - 📊 练习/作业材料占比近50%，是最主要的材料来源
        
        """)
    
    # 1.3 典型图片示例（可展开收起）
    with st.expander("🖼️ 查看典型图片示例（每种类型一个代表）", expanded=False):
        st.markdown("#### 典型图片示例")
        
        # 内容类型示例
        st.markdown("## 📝 内容类型示例")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 1️⃣ 阅读理解（有问题的练习题）")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (105)-1.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：阅读理解 + 练习册  
            **特征**：有文章+问题+选项
            """)
        
        with col2:
            st.markdown("##### 2️⃣ 阅读文章（纯文本，无问题）")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (22)-2.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：阅读文章 + 教材  
            **特征**：只有文章，用于预习阅读
            """)
        
        st.markdown("---")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("##### 3️⃣ 完形填空")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (104)-1.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：完形填空 + 练习册  
            **特征**：文章中有多处空格
            """)
        
        with col4:
            st.markdown("##### 4️⃣ 语法练习")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (112).jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：语法练习 + 练习册  
            **特征**：填空题、选择题
            """)
        
        st.markdown("---")
        
        col5, col6 = st.columns(2)
        
        with col5:
            st.markdown("##### 5️⃣ 词汇练习")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (20)-2.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：词汇练习 + 作业本  
            **特征**：单词填空、词义匹配
            """)
        
        with col6:
            st.markdown("##### 6️⃣ 对话文本")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (10)-1.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：对话文本 + 教材  
            **特征**：A: B: 形式的对话
            """)
        
        # 材料来源示例
        st.markdown("---")
        st.markdown("## 📚 材料来源示例")
        
        col7, col8 = st.columns(2)
        
        with col7:
            st.markdown("##### 7️⃣ 练习/作业材料（48.1%）")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (105)-1.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：练习/作业材料  
            **特征**：包括印刷练习册和手写作业本
            """)
        
        with col8:
            st.markdown("##### 8️⃣ 正式教材（17.7%）")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (110).jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：正式教材  
            **特征**：有教材标识，排版正规
            """)
        
        st.markdown("---")
        
        col9, col10 = st.columns(2)
        
        with col9:
            st.markdown("##### 9️⃣ 试卷（7.3%，周末高频）")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-周末/拍照翻译列表 (12)-3.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：试卷  
            **特征**：周末占比激增5倍
            """)
        
        with col10:
            st.markdown("##### 🔟 屏幕截图（6.9%）")
            try:
                st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.1_图片内容分布/拍照翻译图片-工作日/拍照翻译列表 (106)-2.jpg", 
                        use_container_width=True)
            except:
                st.warning("图片加载失败")
            st.markdown("""
            **标注**：屏幕截图  
            **特征**：手机或电脑屏幕截图
            """)
    
    # 1.4 核心发现
    st.markdown("<div style='margin: 30px 0 20px 0;'></div>", unsafe_allow_html=True)
    st.markdown("#### 核心发现")
    
    # 统计核心数据（在核心发现前面计算）
    df_all = pd.concat([df_weekday, df_weekend])
    total_samples = len(df_all)
    
    # 发现1：核心用户群清晰 - 初中生占60%
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
    col_text1, col_chart1 = st.columns([1.2, 1.8])
    
    with col_text1:
        # 统计年级分布
        grade_counts = df_all['grade_level'].value_counts()
        
        grade_7_9_pct = (grade_counts.get('grade_7_9', 0) / len(df_all) * 100)
        grade_4_6_pct = (grade_counts.get('grade_4_6', 0) / len(df_all) * 100)
        grade_10_12_pct = (grade_counts.get('grade_10_12', 0) / len(df_all) * 100)
        grade_1_3_pct = (grade_counts.get('grade_1_3', 0) / len(df_all) * 100)
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                    padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                <span style="font-size: 1.8rem; margin-right: 12px;">📊</span>
                <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">核心用户</h4>
            </div>
            <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    初中生（7-9年级）：<strong style="color: #2c3e50;">{grade_7_9_pct:.1f}%</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    小学高年级（4-6年级）：<strong style="color: #2c3e50;">{grade_4_6_pct:.1f}%</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    高中生：<strong style="color: #2c3e50;">{grade_10_12_pct:.1f}%</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    小学低年级：<strong style="color: #2c3e50;">{grade_1_3_pct:.1f}%</strong>
                </div>
            </div>
            <div style="margin-top: 20px; padding: 14px; background: rgba(255,255,255,0.7); 
                        border-radius: 8px; border-left: 4px solid #5a9fd4;">
                <strong style="color: #2c3e50; font-size: 0.88rem;">💡 结论：</strong>
                <span style="color: #34495e; font-size: 0.88rem;">功能设计更多考虑小高及初中英语难度</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_chart1:
        # 创建饼图 - 年级分布
        grade_map = {
            'grade_7_9': '初中生（7-9年级）',
            'grade_4_6': '小学高年级（4-6年级）',
            'grade_10_12': '高中生',
            'grade_1_3': '小学低年级',
            'unknown': '未知'
        }
        
        grade_data = []
        grade_labels = []
        for grade, count in grade_counts.items():
            grade_labels.append(grade_map.get(grade, grade))
            grade_data.append(count)
        
        fig1 = go.Figure(data=[go.Pie(
            labels=grade_labels,
            values=grade_data,
            hole=0.4,
            marker=dict(colors=['#5a9fd4', '#7fa5a4', '#d4a574', '#95a5a6']),
            textinfo='label+percent',
            textposition='outside',
            textfont=dict(size=11)
        )])
        
        fig1.update_layout(
            height=350,
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            annotations=[dict(
                text=f'{grade_7_9_pct:.0f}%<br>初中生',
                x=0.5, y=0.5,
                font_size=15,
                showarrow=False
            )]
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    # 发现2：核心场景是阅读理解 - 占比30%
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
    col_text2, col_chart2 = st.columns([1.2, 1.8])
    
    with col_text2:
        # 统计内容类型分布
        content_counts = df_all['content_type'].value_counts()
        total = len(df_all)
        
        reading_comp_pct = (content_counts.get('reading_comprehension', 0) / total * 100)
        reading_pass_pct = (content_counts.get('reading_passage', 0) / total * 100)
        grammar_pct = (content_counts.get('grammar_exercise', 0) / total * 100)
        vocab_pct = (content_counts.get('vocabulary_exercise', 0) / total * 100)
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e8f5e9 0%, #a5d6a7 100%); 
                    padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                <span style="font-size: 1.8rem; margin-right: 12px;">📖</span>
                <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">核心场景是阅读理解</h4>
            </div>
            <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    阅读理解：<strong style="color: #2c3e50;">{reading_comp_pct:.1f}%</strong>（第一大场景）
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    阅读文章：<strong style="color: #2c3e50;">{reading_pass_pct:.1f}%</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    语法练习：<strong style="color: #2c3e50;">{grammar_pct:.1f}%</strong>
                </div>
                <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
                    词汇练习：<strong style="color: #2c3e50;">{vocab_pct:.1f}%</strong>
                </div>
            </div>
            <div style="margin-top: 20px; padding: 14px; background: rgba(255,255,255,0.7); 
                        border-radius: 8px; border-left: 4px solid #6c9a8b;">
                <strong style="color: #2c3e50; font-size: 0.88rem;">💡 结论：</strong>
                <span style="color: #34495e; font-size: 0.88rem;">用户主要用于理解长文本</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_chart2:
        # 创建横向柱状图 - 内容类型TOP 6
        content_map = {
            'reading_comprehension': '阅读理解',
            'reading_passage': '阅读文章',
            'grammar_exercise': '语法练习',
            'vocabulary_exercise': '词汇练习',
            'dialogue_text': '对话文本',
            'cloze_test': '完形填空'
        }
        
        top_contents = content_counts.head(6)
        labels = [content_map.get(k, k) for k in top_contents.index]
        values = [(v / total * 100) for v in top_contents.values]
        
        fig2 = go.Figure()
        
        fig2.add_trace(go.Bar(
            y=labels[::-1],  # 反转顺序，让最大的在顶部
            x=values[::-1],
            orientation='h',
            marker=dict(
                color=values[::-1],
                colorscale=[[0, '#a5d6a7'], [1, '#2e7d32']],
                showscale=False
            ),
            text=[f'{v:.1f}%' for v in values[::-1]],
            textposition='outside',
            textfont=dict(size=11)
        ))
        
        fig2.update_layout(
            height=350,
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis_title='占比 (%)',
            yaxis_title='',
            xaxis=dict(range=[0, max(values) * 1.2])
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # 发现3：周末场景差异显著 - 试卷占比激增5倍
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
    col_text3, col_chart3 = st.columns([1.2, 1.8])
    
    with col_text3:
        # 统计工作日和周末的材料来源（合并练习册和作业本）
        weekday_material = df_weekday['material_source'].value_counts()
        weekend_material = df_weekend['material_source'].value_counts()
        
        weekday_total = len(df_weekday)
        weekend_total = len(df_weekend)
        
        # 练习/作业材料（合并）
        weekday_practice = ((weekday_material.get('workbook', 0) + weekday_material.get('homework_book', 0)) / weekday_total * 100)
        weekend_practice = ((weekend_material.get('workbook', 0) + weekend_material.get('homework_book', 0)) / weekend_total * 100)
        
        # 教材
        weekday_textbook = (weekday_material.get('official_textbook', 0) / weekday_total * 100)
        weekend_textbook = (weekend_material.get('official_textbook', 0) / weekend_total * 100)
        
        # 试卷
        weekday_exam = (weekday_material.get('exam_paper', 0) / weekday_total * 100)
        weekend_exam = (weekend_material.get('exam_paper', 0) / weekend_total * 100)
        
        # 写作作业
        weekday_writing = (df_weekday[df_weekday['content_type'] == 'writing_assignment'].shape[0] / weekday_total * 100)
        weekend_writing = (df_weekend[df_weekend['content_type'] == 'writing_assignment'].shape[0] / weekend_total * 100)
        
        exam_increase = weekend_exam / weekday_exam if weekday_exam > 0 else 0
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffcc80 100%); 
                    padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="display: flex; align-items: center; margin-bottom: 18px;">
                <span style="font-size: 1.8rem; margin-right: 12px;">📅</span>
                <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">周末场景差异显著</h4>
            </div>
            <div style="color: #34495e; font-size: 0.88rem; line-height: 1.8; margin-left: 8px;">
                <div style="margin: 8px 0; padding: 8px; background: rgba(255,255,255,0.5); border-radius: 6px;">
                    <strong style="color: #e65100;">工作日特征：</strong><br>
                    • 练习/作业材料 {weekday_practice:.1f}%、教材为主
                </div>
                <div style="margin: 8px 0; padding: 8px; background: rgba(255,255,255,0.5); border-radius: 6px;">
                    <strong style="color: #e65100;">周末特征：</strong><br>
                    • 试卷 {weekend_exam:.1f}%（工作日 {weekday_exam:.1f}%，↑{exam_increase:.1f}倍）<br>
                    • 练习/作业材料 {weekend_practice:.1f}%（工作日 {weekday_practice:.1f}%）<br>
                    • 写作作业 {weekend_writing:.1f}%（工作日 {weekday_writing:.1f}%）
                </div>
            </div>
            <div style="margin-top: 20px; padding: 14px; background: rgba(255,255,255,0.7); 
                        border-radius: 8px; border-left: 4px solid #d4a574;">
                <strong style="color: #2c3e50; font-size: 0.88rem;">💡 结论：</strong>
                <span style="color: #34495e; font-size: 0.88rem;">周末是集中复习/考试场景，试卷占比激增</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_chart3:
        # 创建分组柱状图 - 工作日 vs 周末材料来源对比（合并练习册和作业本）
        materials = ['练习/作业材料', '教材', '试卷', '屏幕截图']
        
        weekday_values = [
            weekday_practice,
            weekday_textbook,
            weekday_exam,
            (weekday_material.get('screen_capture', 0) / weekday_total * 100)
        ]
        
        weekend_values = [
            weekend_practice,
            weekend_textbook,
            weekend_exam,
            (weekend_material.get('screen_capture', 0) / weekend_total * 100)
        ]
        
        fig3 = go.Figure()
        
        fig3.add_trace(go.Bar(
            name='工作日',
            x=materials,
            y=weekday_values,
            marker=dict(color='#7fa5a4'),
            text=[f'{v:.1f}%' for v in weekday_values],
            textposition='outside',
            textfont=dict(size=10)
        ))
        
        fig3.add_trace(go.Bar(
            name='周末',
            x=materials,
            y=weekend_values,
            marker=dict(color='#ffb74d'),
            text=[f'{v:.1f}%' for v in weekend_values],
            textposition='outside',
            textfont=dict(size=10)
        ))
        
        # 添加试卷激增标注
        fig3.add_annotation(
            x='试卷',
            y=max(weekend_values) + 3,
            text=f"↑{exam_increase:.1f}倍",
            showarrow=True,
            arrowhead=2,
            arrowcolor='#e65100',
            font=dict(size=12, color='#e65100', weight='bold'),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#e65100',
            borderwidth=2
        )
        
        fig3.update_layout(
            height=350,
            barmode='group',
            margin=dict(t=40, b=20, l=20, r=20),
            xaxis_title='',
            yaxis_title='占比 (%)',
            legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.8)'),
            yaxis=dict(range=[0, max(max(weekday_values), max(weekend_values)) * 1.3])
        )
        
        st.plotly_chart(fig3, use_container_width=True)
    
    # ===== 第二部分：用户反馈分析 =====
    st.markdown("<div style='margin: 60px 0 20px 0;'></div>", unsafe_allow_html=True)
    st.markdown("##### 用户反馈分析")
    
    # 2.1 反馈数据概览（表格）
    st.markdown("<div style='margin: 30px 0 20px 0;'></div>", unsafe_allow_html=True)
    st.markdown("##### 📋 用户反馈问题分布（8000条AI打标数据）")
    
    # 统计反馈标签
    label_counts = df_feedback['label'].value_counts()
    total_feedback = len(df_feedback)
    
    # 准备表格数据
    feedback_stats = {
        '问题类型': [],
        '反馈数量': [],
        '占比': [],
        '评级': []
    }
    
    # 定义标签分组
    translation_quality_labels = ['翻译不准确', '翻译不完整', '翻译语言错误']
    pronunciation_labels = ['发音不准确', '朗读不自然', '朗读功能优化', '朗读卡顿重复', 
                           '朗读速度问题', '缺少中文朗读', '发音朗读问题', 'Audio_Issues']
    suggestion_labels = ['翻译语言扩展', '功能需求', '其他功能需求', '单词本收藏', 
                        '句子分析', '历史记录', 'Feature_Requests']
    
    # 翻译质量问题
    quality_count = sum([label_counts.get(label, 0) for label in translation_quality_labels])
    feedback_stats['问题类型'].append('翻译质量问题')
    feedback_stats['反馈数量'].append(f'{quality_count:,}')
    feedback_stats['占比'].append(f'{quality_count/total_feedback*100:.2f}%')
    feedback_stats['评级'].append('🔴 核心痛点')
    
    # 无法分类
    unclassified_count = label_counts.get('无法分类', 0)
    feedback_stats['问题类型'].append('其他/无法分类')
    feedback_stats['反馈数量'].append(f'{unclassified_count:,}')
    feedback_stats['占比'].append(f'{unclassified_count/total_feedback*100:.2f}%')
    feedback_stats['评级'].append('⚪ 正常反馈')
    
    # 满意反馈（标签是"满意表扬"）
    satisfied_count = label_counts.get('满意表扬', 0)
    feedback_stats['问题类型'].append('满意反馈')
    feedback_stats['反馈数量'].append(f'{satisfied_count:,}')
    feedback_stats['占比'].append(f'{satisfied_count/total_feedback*100:.2f}%')
    feedback_stats['评级'].append('🟢 正面评价')
    
    # 发音朗读问题
    pronunciation_count = sum([label_counts.get(label, 0) for label in pronunciation_labels])
    feedback_stats['问题类型'].append('发音朗读问题')
    feedback_stats['反馈数量'].append(f'{pronunciation_count:,}')
    feedback_stats['占比'].append(f'{pronunciation_count/total_feedback*100:.2f}%')
    feedback_stats['评级'].append('🟡 次要痛点')
    
    # 产品建议
    suggestion_count = sum([label_counts.get(label, 0) for label in suggestion_labels])
    feedback_stats['问题类型'].append('产品建议')
    feedback_stats['反馈数量'].append(f'{suggestion_count:,}')
    feedback_stats['占比'].append(f'{suggestion_count/total_feedback*100:.2f}%')
    feedback_stats['评级'].append('🔵 功能需求')
    
    # 其他问题（OCR识别、界面交互、速度等）
    other_count = total_feedback - (quality_count + unclassified_count + satisfied_count + pronunciation_count + suggestion_count)
    feedback_stats['问题类型'].append('其他问题')
    feedback_stats['反馈数量'].append(f'{other_count:,}')
    feedback_stats['占比'].append(f'{other_count/total_feedback*100:.2f}%')
    feedback_stats['评级'].append('⚪ 其他')
    
    # 创建DataFrame
    df_feedback_stats = pd.DataFrame(feedback_stats)
    
    # 使用HTML表格实现居中和高亮
    html_table = '<table style="width:100%; border-collapse: collapse; text-align: center; table-layout: fixed;">'
    html_table += '<thead><tr style="background-color: #f0f2f6;">'
    col_widths = ['25%', '20%', '20%', '35%']
    for i, col in enumerate(df_feedback_stats.columns):
        html_table += f'<th style="padding: 12px; border: 1px solid #ddd; width: {col_widths[i]}; font-weight: 600;">{col}</th>'
    html_table += '</tr></thead><tbody>'
    
    for idx, row in df_feedback_stats.iterrows():
        # 翻译质量问题行高亮
        if row['问题类型'] == '翻译质量问题':
            html_table += '<tr style="background-color: #ffebee;">'
        else:
            html_table += '<tr>'
        
        for col_idx, col in enumerate(df_feedback_stats.columns):
            value = row[col]
            # 占比列加粗
            if col == '占比' and row['问题类型'] == '翻译质量问题':
                html_table += f'<td style="padding: 10px; border: 1px solid #ddd; font-weight: 700;">{value}</td>'
            else:
                html_table += f'<td style="padding: 10px; border: 1px solid #ddd;">{value}</td>'
        html_table += '</tr>'
    
    html_table += '</tbody></table>'
    st.markdown(html_table, unsafe_allow_html=True)
    
    # 2.2 发音朗读问题详细数据
    st.markdown("<div style='margin: 40px 0 20px 0;'></div>", unsafe_allow_html=True)
    st.markdown("##### 🔊 发音朗读问题详细数据")
    
    # 加载发音朗读详细数据
    pronunciation_detail_path = "/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.2_用户反馈分析/清洗结果/发音朗读问题详细数据.csv"
    df_pronunciation = pd.read_csv(pronunciation_detail_path)
    
    # 显示统计信息
    st.info(f"📊 共 {len(df_pronunciation)} 条反馈，占总反馈的 {len(df_pronunciation)/total_feedback*100:.2f}%")
    
    # 统计各类型数量
    pronunciation_type_counts = df_pronunciation['label'].value_counts()
    st.markdown("**问题类型分布：**")
    type_stats = []
    for label, count in pronunciation_type_counts.items():
        type_stats.append(f"• {label}：{count}条")
    st.markdown("  \n".join(type_stats))
    
    # 显示详细表格
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    display_pronunciation = df_pronunciation[['feedback_date', 'label', 'feedback_content', 'scene']].copy()
    display_pronunciation.columns = ['反馈日期', '问题类型', '反馈内容', '使用场景']
    
    # 显示全部数据
    st.markdown(f"**全部 {len(display_pronunciation)} 条反馈详情：**")
    st.dataframe(
        display_pronunciation,
        use_container_width=True,
        height=500
    )
    
    # 提供下载按钮
    csv_pronunciation = df_pronunciation.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 下载全部发音朗读问题数据",
        data=csv_pronunciation.encode('utf-8-sig'),
        file_name="发音朗读问题详细数据.csv",
        mime="text/csv"
    )
    
    # 2.3 产品建议详细数据
    st.markdown("<div style='margin: 40px 0 20px 0;'></div>", unsafe_allow_html=True)
    st.markdown("##### 💡 产品建议详细数据")
    
    # 加载产品建议详细数据
    suggestion_detail_path = "/Users/pupu/Desktop/Claude/拍照翻译功能分析/2_定性分析/2.2_用户反馈分析/清洗结果/产品建议详细数据.csv"
    df_suggestion = pd.read_csv(suggestion_detail_path)
    
    # 显示统计信息
    st.info(f"📊 共 {len(df_suggestion)} 条反馈，占总反馈的 {len(df_suggestion)/total_feedback*100:.2f}%")
    
    # 统计各类型数量
    suggestion_type_counts = df_suggestion['label'].value_counts()
    st.markdown("**需求类型分布：**")
    type_stats_suggestion = []
    for label, count in suggestion_type_counts.items():
        type_stats_suggestion.append(f"• {label}：{count}条")
    st.markdown("  \n".join(type_stats_suggestion))
    
    # 显示详细表格
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    display_suggestion = df_suggestion[['feedback_date', 'label', 'feedback_content', 'scene']].copy()
    display_suggestion.columns = ['反馈日期', '需求类型', '反馈内容', '使用场景']
    
    # 显示全部数据
    st.markdown(f"**全部 {len(display_suggestion)} 条反馈详情：**")
    st.dataframe(
        display_suggestion,
        use_container_width=True,
        height=500
    )
    
    # 提供下载按钮
    csv_suggestion = df_suggestion.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 下载全部产品建议数据",
        data=csv_suggestion.encode('utf-8-sig'),
        file_name="产品建议详细数据.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(f"数据加载失败：{str(e)}")
    st.info("请确保数据文件路径正确")
