# TIKTOK AI智能翻译助手

一个专为TIKTOK直播设计的多国语言实时翻译助手，支持语音翻译和屏幕文字翻译功能。

## 功能特点

1. **语音实时翻译** - 支持多国语言的语音输入和实时翻译
2. **屏幕文字翻译** - 可识别屏幕上的文字并进行翻译
3. **直播间实时翻译** - 可连接TikTok直播间，实时翻译观众评论
4. **AI大模型管理** - 支持添加和管理多种AI大模型（翻译、语音识别、OCR等）
5. **多语言支持** - 支持中、英、日、韩、法、德、西等多种语言
6. **翻译结果保存** - 自动保存翻译记录到本地数据库
7. **语音输出** - 支持将翻译结果转换为语音播放

## 技术架构

- **编程语言**: Python + Java + SQLite
- **GUI框架**: PyQt5
- **音频处理**: PyAudio
- **屏幕捕获**: PyAutoGUI
- **图像处理**: OpenCV, Pillow
- **网络请求**: Requests
- **数据库**: SQLite

## 安装指南

1. 克隆项目代码:
   ```
   git clone <项目地址>
   ```

2. 安装依赖:
   ```
   pip install -r requirements.txt
   ```

3. 运行程序:
   ```
   python run.py
   ```

## 使用说明

1. **语音翻译**:
   - 在"语音翻译"标签页点击"开始录音"
   - 讲话结束后点击"停止录音"
   - 点击"翻译"按钮获取翻译结果

2. **屏幕翻译**:
   - 在"屏幕翻译"标签页设置捕获区域坐标和尺寸
   - 点击"开始捕获"开始屏幕文字识别
   - 点击"翻译"按钮获取翻译结果

3. **直播间翻译**:
   - 在"直播间翻译"标签页输入TikTok直播间完整URL地址
   - 可选地配置API密钥和API地址
   - 点击"连接直播间"按钮连接到指定直播间
   - 程序将自动获取并显示观众评论
   - 可选择自动采集文字和语音评论
   - 点击"开始翻译"按钮实时翻译评论

4. **AI模型管理**:
   - 在"AI模型管理"标签页可以添加、删除和激活各种AI模型
   - 支持翻译模型、语音识别模型、OCR模型和语音合成模型
   - 支持API和本地模型两种实现方式
   - 可以为每种功能指定不同的AI模型

5. **设置**:
   - 在"设置"标签页可设置源语言和目标语言
   - 可设置是否启用语音输出
   - 可设置翻译结果的保存路径


## 开发计划

- [x] 基础GUI界面开发
- [x] 数据库设计
- [x] UI交互体验优化
- [x] 直播间接入功能
- [x] AI大模型接入功能
- [ ] 集成真实AI翻译模型
- [ ] 实现语音识别功能
- [ ] 实现OCR文字识别功能
- [ ] 实现TTS语音合成功能
- [ ] 完善设置功能
- [ ] 测试和优化

## 注意事项

1. 本软件需要访问麦克风和屏幕录制权限
2. 翻译功能依赖AI模型，需要联网使用
3. 直播间功能需要有效的直播间URL地址
4. 如需访问海外TikTok，可能需要配置API代理
5. AI模型功能目前为框架实现，需要根据具体模型完善细节

## GUI特性

根据用户的GUI交互体验偏好，本应用特别优化了以下方面：

1. **多标签导航系统** - 清晰的功能分区，便于快速切换（直播间翻译、语音翻译、屏幕翻译、AI模型管理、设置、历史记录）
2. **加载状态指示** - 翻译过程中显示进度条，提供实时反馈
3. **错误处理机制** - 完善的异常处理和用户提示
4. **响应式布局** - 适应不同屏幕尺寸的布局设计
5. **丰富的UI组件** - 使用多种控件提供良好的交互体验
6. **数据交互功能** - 支持历史记录查看和管理
7. **模型管理功能** - 支持添加多个模型并指定启用模型
