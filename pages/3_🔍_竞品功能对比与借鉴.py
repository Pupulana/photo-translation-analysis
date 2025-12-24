# -*- coding: utf-8 -*-
"""
竞品功能对比与借鉴页面
"""

import streamlit as st
from pathlib import Path

# 页面配置
st.set_page_config(
    page_title="竞品功能对比与借鉴",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== 翻译工具趋势 =====
st.markdown("#### 📖 翻译工具趋势")
st.markdown("""
<div style="color: #666; font-size: 0.88rem; margin: 8px 0 16px 0;">
调研竞品：有道词典、作业帮、百度翻译、快对、夸克扫描王
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ===== 核心发现 =====
st.markdown("#### 📊 核心发现")
st.markdown("")

# ===== 核心发现1：从翻译工具到学习服务 =====
st.markdown("##### 📚 从翻译工具到学习服务")
st.markdown("")

st.markdown("""
<div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
            padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
    <div style="display: flex; align-items: center; margin-bottom: 18px;">
        <span style="font-size: 1.8rem; margin-right: 12px;">💡</span>
        <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">核心：让翻译内容可沉淀、可复习</h4>
    </div>
    <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
        <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
            <strong style="color: #2c3e50;">有道词典：</strong>重点单词标记，快速收藏单词和句子
        </div>
        <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
            <strong style="color: #2c3e50;">夸克扫描王：</strong>段落涂抹翻译，点击单词查看释义
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown("**竞品案例**")

# 3张图片横排
col_a, col_b, col_c = st.columns([1, 1, 1])
with col_a:
    st.markdown("**有道词典 - 重点单词标记**")
    try:
        st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析_副本/4_团队分享/图片/有道翻译-重点单词标记_副本.jpg", 
                use_container_width=True)
    except:
        st.info("📷 图片加载失败")

with col_b:
    st.markdown("**夸克扫描王 - 段落涂抹翻译**")
    try:
        st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析_副本/4_团队分享/图片/夸克扫描王-段落涂抹翻译_副本.jpg", 
                use_container_width=True)
    except:
        st.info("📷 图片加载失败")

with col_c:
    st.markdown("**有道词典 - 快速收藏单词及句子**")
    try:
        st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析_副本/4_团队分享/图片/有道翻译-快速收藏单词及句子_副本.jpg", 
                use_container_width=True)
    except:
        st.info("📷 图片加载失败")

st.markdown("<div style='margin: 40px 0;'></div>", unsafe_allow_html=True)

# ===== 核心发现2：AI能力融入 =====
st.markdown("##### 🤖 AI能力融入")
st.markdown("")

st.markdown("""
<div style="background: linear-gradient(135deg, #e8f5e9 0%, #a5d6a7 100%); 
            padding: 28px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
    <div style="display: flex; align-items: center; margin-bottom: 18px;">
        <span style="font-size: 1.8rem; margin-right: 12px;">💡</span>
        <h4 style="color: #2c3e50; margin: 0; font-size: 1.05rem; font-weight: 600;">核心：从"翻译准确"到"理解+讲解"</h4>
    </div>
    <div style="color: #34495e; font-size: 0.9rem; line-height: 1.9; margin-left: 8px;">
        <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
            <strong style="color: #2c3e50;">百度翻译：</strong>语法分析，标注主谓宾、时态、句型，语法错误检查
        </div>
        <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
            <strong style="color: #2c3e50;">作业帮：</strong>AI对话辅导，提供语法分析和详细讲解
        </div>
        <div style="margin: 12px 0; padding-left: 12px; border-left: 3px solid rgba(255,255,255,0.6);">
            <strong style="color: #2c3e50;">快对：</strong>问小对，按住可对单词和段落进行AI对话问答
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown("**竞品案例**")

# 3张图片横排
col_a, col_b, col_c = st.columns([1, 1, 1])
with col_a:
    st.markdown("**百度翻译 - 语法分析**")
    try:
        st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析_副本/4_团队分享/图片/百度-语法分析_副本.jpg", 
                use_container_width=True)
    except:
        st.info("📷 图片加载失败")

with col_b:
    st.markdown("**作业帮 - AI对话辅导**")
    try:
        st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析_副本/4_团队分享/图片/作业帮-对话辅导-语法分析_副本.jpg", 
                use_container_width=True)
    except:
        st.info("📷 图片加载失败")

with col_c:
    st.markdown("**快对 - 问小对（段落）**")
    try:
        st.image("/Users/pupu/Desktop/Claude/拍照翻译功能分析_副本/4_团队分享/图片/点击问小对-段落.jpg", 
                use_container_width=True)
    except:
        st.info("📷 图片加载失败")

st.markdown("<div style='margin: 60px 0;'></div>", unsafe_allow_html=True)

# ===== 下个季度规划 =====
st.markdown("#### 🎯 下个季度规划")
st.markdown("")

# 3个规划方向卡片
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); 
                padding: 24px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                min-height: 380px; border: 2px solid #ffb74d; display: flex; flex-direction: column;">
        <div style="display: flex; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 1.6rem; margin-right: 10px;">🤖</span>
            <h4 style="color: #e65100; margin: 0; font-size: 1rem; font-weight: 600;">AI辅导与学习闭环</h4>
        </div>
        <div style="color: #5d4037; font-size: 0.88rem; line-height: 1.8; flex: 1;">
            <div style="background: rgba(255,255,255,0.6); padding: 10px; border-radius: 6px; margin-bottom: 12px; font-weight: 600;">
                目标：对话讲解功能渗透达到 X%
            </div>
            <div style="margin: 10px 0;">
                • 外化AI深度辅导能力，上线"AI对话讲解"功能，支持长难句讲解、语法分析等场景
            </div>
            <div style="margin: 10px 0;">
                • 打通"查词-收藏-背诵"链路，支持生词一键收藏，并串联背单词模块
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); 
                padding: 24px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                min-height: 380px; border: 2px solid #7986cb; display: flex; flex-direction: column;">
        <div style="display: flex; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 1.6rem; margin-right: 10px;">📱</span>
            <h4 style="color: #283593; margin: 0; font-size: 1rem; font-weight: 600;">提升翻译功能体验</h4>
        </div>
        <div style="color: #37474f; font-size: 0.88rem; line-height: 1.8; flex: 1;">
            <div style="background: rgba(255,255,255,0.6); padding: 10px; border-radius: 6px; margin-bottom: 12px; font-weight: 600;">
                目标：功能7留率提升至20%
            </div>
            <div style="margin: 10px 0;">
                • <strong>多页扫描：</strong>支持一次拍摄多张图片并统一处理，支持左右滑动横向切换翻译结果，满足连续拍摄场景
            </div>
            <div style="margin: 10px 0;">
                • <strong>历史记录：</strong>在相机页增加历史记录入口
            </div>
            <div style="margin: 10px 0;">
                • <strong>TTS优化：</strong>原文点读功能渗透率提升至X%
            </div>
            <div style="margin: 10px 0;">
                • <strong>前端优化：</strong>持续迭代拍照后的结果页布局
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); 
                padding: 24px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                min-height: 380px; border: 2px solid #ba68c8; display: flex; flex-direction: column;">
        <div style="display: flex; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 1.6rem; margin-right: 10px;">🔧</span>
            <h4 style="color: #6a1b9a; margin: 0; font-size: 1rem; font-weight: 600;">持续优化算法效果</h4>
        </div>
        <div style="color: #4a148c; font-size: 0.88rem; line-height: 1.8; flex: 1;">
            <div style="background: rgba(255,255,255,0.6); padding: 10px; border-radius: 6px; margin-bottom: 12px; font-weight: 600;">
                目标：段落框正确率达到X%，字符准确率达到X%
            </div>
            <div style="margin: 10px 0;">
                • <strong>多模态融合识别：</strong>建立智能路由策略，艺术字走多模态模型，复杂排版/多框场景走传统OCR模型
            </div>
            <div style="margin: 10px 0;">
                • <strong>图像质量修复：</strong>持续迭代矫正与擦除模型，解决擦除不净、背景变暗问题，提升结果页视觉还原度
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
