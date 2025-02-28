# 在x86机器上打包arm64包：
## 启用 Docker 的多架构支持
启用对 ARM64 的支持：
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes

设置 Docker 支持多架构的目标平台：
docker buildx create --use


## 打 ARM64 镜像包
#### 第一步：打python的base镜像包：

    docker buildx build --platform linux/arm64 -f install/docker/Dockerfile-base . -t docker.io/crofi/kubeflow-dashboard:base-python3.9-20250228-v1.2-ubuntu-arm --push

#### 第二步：打后端包：
    1）修改 install/docker/Dockerfile-arm64 文件，把FROM 的基础镜像换成第一步打的版本号

    2）执行打包：
     docker buildx build --platform linux/arm64 -f install/docker/Dockerfile-arm64 . -t docker.io/crofi/kubeflow-dashboard:20250228-ubuntu-arm --push

#### 第三步：打前端包
    docker buildx build --platform linux/arm64 -f install/docker/dockerFrontend/Dockerfile . -t docker.io/crofi/kubeflow-dashboard-frontend:20250228-ubuntu-arm --push
