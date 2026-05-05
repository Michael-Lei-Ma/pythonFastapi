pipeline {
    agent any

    environment {
        // Docker 镜像配置
        DOCKER_IMAGE = 'fastapi-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = 'py-fastapi-container'
        HOST_PORT = '8000'
        CONTAINER_PORT = '8001'
        KEEP_COUNT = '5'
    }

    stages {
        stage('1. 代码拉取') {
            steps {
                echo '从 GitHub 拉取最新代码...'
                checkout scm
            }
        }

        stage('2. 环境准备') {
            steps {
                echo '准备 Python 虚拟环境...'
                bat '''
                    py -3.13 -m pip install --upgrade pip
                    py -3.13 -m pip install -r requirements.txt
                '''
            }
        }

        stage('3. 运行测试') {
            steps {
                echo '运行 pytest 单元测试...'
                bat '''
                    pytest --alluredir=allure-results
                '''
            }
        }

        stage('4. 构建 Docker 镜像') {
            steps {
                echo '构建 Docker 镜像...'
                script {
                    // 构建新镜像
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('5. 停止并移除旧容器') {
            steps {
                echo '停止正在运行的旧容器...'
                script {
                    // 使用 || true 避免容器不存在时报错
                    bat "docker stop ${CONTAINER_NAME} || exit 0"
                    bat "docker rm ${CONTAINER_NAME} || exit 0"
                }
            }
        }

        stage('6. 启动新容器') {
            steps {
                echo '启动新的 Docker 容器...'
                bat """
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${HOST_PORT}:${CONTAINER_PORT} \
                        --restart unless-stopped \
                        ${DOCKER_IMAGE}:latest
                """
            }
        }

//         stage('7. 健康检查') {
//             steps {
//                 echo '等待服务启动并进行健康检查...'
//                 script {
//                     // 等待 5 秒让服务启动
//                     sleep time: 5, unit: 'SECONDS'
//
//                     // 检查容器是否正常运行
//                     def containerStatus = bat(script: "docker ps --filter name=${CONTAINER_NAME} --format '{{.Status}}'", returnStdout: true).trim()
//                     echo "容器状态: ${containerStatus}"
//
//                     // 检查服务是否可访问
//                     def response = bat(script: "curl -s http://localhost:${HOST_PORT}", returnStdout: true).trim()
//                     echo "服务响应: ${response}"
//
//                     if (response.contains('404') || response.contains('error')) {
//                         error('健康检查失败：服务未正常响应')
//                     }
//                 }
//             }
//         }

//         stage('8. 清理旧镜像') {
//             steps {
//                 script {
//                     echo '清理旧的 Docker 镜像，保留最近3个'
//                     bat """
//                         docker image prune -a -f --filter 'until=24h'
//                         docker system prune -f
//                         docker volume prune -f
//
//                     """
//
//                     echo '清理未使用的 Docker 镜像...'
//                     bat "docker image prune -f"
//                 }
//             }
//         }
        stage('8. 清理旧镜像') {
            steps {
                script {
                    echo '清理旧的 Docker 镜像，保留最近3个'

                    bat """
                    echo ===== 获取镜像列表 =====

                    for /f "skip=%KEEP_COUNT% tokens=1" %%i in (
                        'docker images %DOCKER_IMAGE% --format "{{.Repository}}:{{.Tag}}" --sort=created'
                    ) do (
                        echo 删除镜像 %%i
                        docker rmi -f %%i
                    )

                    echo ===== 清理悬空镜像 =====
                    docker image prune -f
                    """
                }
            }
        }



    }

    post {
        success {
            echo '==================== 部署成功！ ===================='
            echo "FastAPI 服务已部署到: http://localhost:${HOST_PORT}"
            echo "API 文档: http://localhost:${HOST_PORT}/docs"
        }
        failure {
            echo '==================== 部署失败！ ===================='
            echo '请检查 Jenkins 构建日志获取详细错误信息'

            // 可选：发送邮件通知
            // emailext(
            //     subject: "构建失败: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
            //     body: "请查看构建日志: ${env.BUILD_URL}",
            //     to: "admin@example.com"
            // )
        }
        always {
            echo 'Pipeline 执行完毕，清理工作区...'
            // 可选：删除虚拟环境释放空间
            // bat 'if exist venv rmdir /s /q venv'
        }
    }
}