# 使用 Node.js 的 Alpine 镜像作为基础
FROM node:18-alpine

# 设置工作目录
WORKDIR /mealprovider2024

# 复制 package.json 和 package-lock.json 到工作目录
COPY package*.json ./

# 安装依赖项
RUN npm install

# 全局安装 Angular CLI
RUN npm install -g @angular/cli

# 复制所有项目文件到工作目录
COPY . .

# 暴露应用的运行端口
EXPOSE 4200

# 启动 Angular 应用
CMD ["ng", "serve", "--host", "0.0.0.0"]

